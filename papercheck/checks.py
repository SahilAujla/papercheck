"""Consistency checks: p recomputation (statcheck style), GRIM, GRIMMER, df vs N, duplicates."""
from __future__ import annotations

import math
import re
from collections import defaultdict
from typing import Optional

from scipy import stats as sps

from .grim import count_decimals, grim_test, grimmer_test
from .models import Flag, MeanSD, Stat

ALPHA = 0.05


# ---------------------------------------------------------------- p values

def compute_p(kind: str, value: float, df1: Optional[float], df2: Optional[float]) -> Optional[float]:
    """Two-tailed p for a test statistic. Returns None when it cannot be computed."""
    try:
        if kind == "t":
            if not df1 or df1 <= 0:
                return None
            return float(2 * sps.t.sf(abs(value), df1))
        if kind == "F":
            if not df1 or not df2 or df1 <= 0 or df2 <= 0 or value < 0:
                return None
            return float(sps.f.sf(value, df1, df2))
        if kind == "chi2":
            if not df1 or df1 <= 0 or value < 0:
                return None
            return float(sps.chi2.sf(value, df1))
        if kind == "r":
            if not df1 or df1 <= 0 or abs(value) >= 1:
                return None if abs(value) > 1 else 0.0
            t = value * math.sqrt(df1 / (1 - value ** 2))
            return float(2 * sps.t.sf(abs(t), df1))
        if kind == "z":
            return float(2 * sps.norm.sf(abs(value)))
    except (ValueError, ZeroDivisionError, OverflowError):
        return None
    return None


def p_interval(stat: Stat) -> Optional[tuple[float, float, float]]:
    """(p_low, p_point, p_high): recomputed p for the rounding interval of the reported statistic."""
    half = 0.5 * 10 ** (-stat.value_decimals)
    lo_v, hi_v = stat.value - half, stat.value + half
    if stat.kind in ("F", "chi2"):
        lo_v = max(lo_v, 0.0)
    if stat.kind == "r":
        lo_v, hi_v = max(lo_v, -1.0), min(hi_v, 1.0)
    point = compute_p(stat.kind, stat.value, stat.df1, stat.df2)
    p_a = compute_p(stat.kind, lo_v, stat.df1, stat.df2)
    p_b = compute_p(stat.kind, hi_v, stat.df1, stat.df2)
    if point is None:
        return None
    cands = [p for p in (p_a, p_b, point) if p is not None]
    if stat.kind in ("t", "z", "r") and lo_v < 0 < hi_v:
        cands.append(1.0)  # the statistic may be ~0
    if stat.value_comparator == "<":      # "t(334) < 0.01": the true statistic is smaller, so p is at least this
        return min(cands), point, 1.0
    if stat.value_comparator == ">":      # "F(2, 40) > 10": p is at most this
        return 0.0, point, max(cands)
    return min(cands), point, max(cands)


def _reported_p_bounds(stat: Stat) -> tuple[Optional[float], Optional[float]]:
    """Bounds [lo, hi] that the recomputed p must fall in to be consistent."""
    cmp_, p, d = stat.p_comparator, stat.p_reported, stat.p_decimals
    if cmp_ == "ns":
        return ALPHA, 1.0
    if p is None:
        return None, None
    if cmp_ == "=":
        if p == 0:  # "p = .000" means p < half a unit in the last place
            return 0.0, 0.5 * 10 ** (-d)
        half = 0.5 * 10 ** (-d)
        return max(0.0, p - half), min(1.0, p + half)
    if cmp_ == "<":
        return 0.0, p
    if cmp_ == ">":
        return p, 1.0
    return None, None


def check_p_values(stat: Stat) -> Optional[Flag]:
    """statcheck-style comparison of the reported p with the p recomputed from the statistic."""
    iv = p_interval(stat)
    if iv is None or stat.p_comparator is None:
        return None
    p_lo, p_point, p_hi = iv
    lo, hi = _reported_p_bounds(stat)
    if lo is None:
        return None
    eps = 1e-9
    # consistent if the recomputed interval overlaps the reported bounds
    if p_hi >= lo - eps and p_lo <= hi + eps:
        return None
    details = {"stat": stat.label(), "p_reported": stat.p_reported, "p_comparator": stat.p_comparator,
               "p_recomputed": round(p_point, 6), "p_recomputed_interval": [round(p_lo, 6), round(p_hi, 6)]}
    # one-tailed caveat: would a one-tailed p have been consistent?
    one_lo, one_hi = p_lo / 2, p_hi / 2
    one_tailed_ok = one_hi >= lo - eps and one_lo <= hi + eps
    details["consistent_if_one_tailed"] = one_tailed_ok
    # decision error across .05?
    reported_sig = _reported_significant(stat)
    recomputed_sig = p_hi < ALPHA if p_hi < ALPHA else (False if p_lo >= ALPHA else None)
    decision_error = reported_sig is not None and recomputed_sig is not None and reported_sig != recomputed_sig
    details["decision_error"] = decision_error
    if one_tailed_ok and not decision_error:
        sev = "info"
        text = (f"Reported {stat.raw}. Recomputed two-tailed p = {_fp(p_point)}, which does not match the reported value, "
                f"but a one-tailed test would give p = {_fp(p_point / 2)}, which does. Check whether the paper states a "
                f"one-tailed test.")
    elif decision_error:
        sev = "error"
        text = (f"Reported {stat.raw}. Recomputed p = {_fp(p_point)} (range {_fp(p_lo)} to {_fp(p_hi)} given rounding of "
                f"the test statistic). The reported p and the recomputed p fall on different sides of .05, so the "
                f"conclusion about significance would change. Reported vs recomputed values differ; the cause could be a "
                f"typo in the statistic, the df or the p, or a one-tailed test"
                + (" (a one-tailed p would be consistent)." if one_tailed_ok else "."))
    else:
        sev = "warning"
        text = (f"Reported {stat.raw}. Recomputed p = {_fp(p_point)} (range {_fp(p_lo)} to {_fp(p_hi)} given rounding of "
                f"the test statistic) does not match the reported p. The significance decision is unchanged.")
    if stat.kind == "chi2" and stat.df1 == 1:
        text += (" For a 2 x 2 table, a continuity-corrected chi-square or Fisher's exact test gives a different p from "
                 "the uncorrected statistic, which is a common benign explanation.")
    return Flag(check="p_recompute", severity=sev, page=stat.page, sentence=stat.sentence, raw=stat.raw,
                explanation=text, details=details)


def _reported_significant(stat: Stat) -> Optional[bool]:
    cmp_, p = stat.p_comparator, stat.p_reported
    if cmp_ == "ns":
        return False
    if p is None:
        return None
    if cmp_ == "<":
        return True if p <= ALPHA else None
    if cmp_ == ">":
        return False if p >= ALPHA else None
    return p < ALPHA  # '='; statcheck treats p = .05 as not significant


def _fp(p: float) -> str:
    if p < 0.001:
        return f"{p:.2e}"
    return f"{p:.4f}"


# ---------------------------------------------------------------- GRIM / GRIMMER

def check_grim(m: MeanSD, items: int = 1) -> list[Flag]:
    flags: list[Flag] = []
    if m.n is None or m.n < 2:
        return flags
    dec = count_decimals(m.mean_text)
    if dec == 0:
        return flags
    g = grim_test(m.mean, m.n, dec, items=items)
    if g.note:
        return flags
    strong_n = m.n_source in ("same parenthesis", "same sentence", "table n column", "table column header",
                              "table n row")
    if not g.consistent:
        near = ", ".join(f"{x:.{dec}f}" for x in g.nearest_possible)
        flags.append(Flag(
            check="grim", severity="warning" if strong_n else "info", page=m.page, sentence=m.sentence, raw=m.raw,
            explanation=(f"GRIM: a mean of {m.mean_text} with n = {m.n} (N taken from the {m.n_source}) is not possible if "
                         f"each score is a whole number (for example a single Likert item or a count). The nearest possible "
                         f"means are {near}. This only matters if the measure is integer-valued; averaged multi-item scales "
                         f"or continuous measures make GRIM inapplicable."),
            details={"mean": m.mean, "n": m.n, "decimals": dec, "nearest_possible": g.nearest_possible,
                     "n_source": m.n_source}))
        return flags
    if m.sd is not None and m.sd_text:
        sd_dec = count_decimals(m.sd_text)
        gr = grimmer_test(m.mean, m.sd, m.n, dec, sd_dec, items=items)
        if gr.grim_consistent and not gr.consistent and not gr.note:
            flags.append(Flag(
                check="grimmer", severity="info", page=m.page, sentence=m.sentence, raw=m.raw,
                explanation=(f"GRIMMER: the mean {m.mean_text} passes GRIM, but no whole-number data set of n = {m.n} "
                             f"(N from the {m.n_source}) has this mean together with SD = {m.sd_text}. Applies only if the "
                             f"measure is integer-valued; treat as a prompt to check, not a conclusion."),
                details={"mean": m.mean, "sd": m.sd, "n": m.n, "n_source": m.n_source}))
    return flags


# ---------------------------------------------------------------- df vs N

def implied_n(stat: Stat) -> list[int]:
    """Sample sizes implied by the degrees of freedom under common designs."""
    out: set[int] = set()
    if stat.kind == "t" and stat.df1:
        out.update({int(stat.df1) + 1, int(stat.df1) + 2})       # paired/one-sample, independent
    elif stat.kind == "F" and stat.df1 and stat.df2:
        out.add(int(stat.df1) + int(stat.df2) + 1)               # one-way between subjects
    elif stat.kind == "r" and stat.df1:
        out.add(int(stat.df1) + 2)
    return sorted(out)


def check_df_vs_n(stats: list[Stat], sample_sizes: list[dict]) -> list[Flag]:
    """Flag tests whose df imply more participants than the paper ever reports."""
    flags: list[Flag] = []
    ns = [s["n"] for s in sample_sizes]
    if not ns:
        return flags
    max_n = max(ns)
    for st in stats:
        if st.kind == "chi2" and st.n:
            if st.n not in ns:
                flags.append(Flag(check="df_vs_n", severity="info", page=st.page, sentence=st.sentence, raw=st.raw,
                                  explanation=(f"The N = {st.n} inside the chi-square statistic does not appear anywhere "
                                               f"else in the paper as a sample size (reported sizes include "
                                               f"{_top(ns)}). May be a subsample; worth a look."),
                                  details={"n_in_stat": st.n, "reported_ns": sorted(set(ns))}))
            continue
        imp = implied_n(st)
        if not imp:
            continue
        # repeated-measures designs (F with df1 small, large df2) and Welch t can have fractional df
        if st.kind == "t" and st.df1 and not float(st.df1).is_integer():
            continue
        if min(imp) > max_n:
            design = _DESIGN_WORDS.search(st.sentence) is not None
            flags.append(Flag(check="df_vs_n", severity="info" if design else "warning", page=st.page,
                              sentence=st.sentence, raw=st.raw,
                              explanation=(f"The degrees of freedom in {st.label()} imply at least {min(imp)} "
                                           f"participants under the usual design, but the largest sample size "
                                           f"mentioned in the paper is {max_n}. Reported vs implied N differ; could be "
                                           f"a repeated-measures design, trials as the unit of analysis, or a typo in the df."),
                              details={"implied_n": imp, "max_reported_n": max_n}))
    return flags


_DESIGN_WORDS = re.compile(
    r"repeated|within[- ]subject|mixed|Wilks|Pillai|MANOVA|multivariate|trials?\b|sessions?\b|days?\b|blocks?\b|"
    r"pooled|combined|collapsed|across (?:all )?(?:studies|experiments|conditions)|items?\b|observations|"
    r"stimuli|ratings|unit of analysis", re.IGNORECASE)


def _top(ns: list[int]) -> str:
    uniq = sorted(set(ns), reverse=True)[:6]
    return ", ".join(str(n) for n in uniq)


# ---------------------------------------------------------------- duplicates

def check_duplicates(stats: list[Stat]) -> list[Flag]:
    groups: dict[tuple, list[Stat]] = defaultdict(list)
    for st in stats:
        key = (st.kind, st.df1, st.df2, st.value, st.p_comparator, st.p_reported)
        groups[key].append(st)
    flags: list[Flag] = []
    for key, items in groups.items():
        if len(items) < 2:
            continue
        pages = sorted({s.page for s in items})
        first = items[0]
        flags.append(Flag(check="duplicate", severity="info", page=first.page, sentence=first.sentence, raw=first.raw,
                          explanation=(f"The statistic {first.label()} with the same p value appears {len(items)} times "
                                       f"(pages {', '.join(map(str, pages))}). Often legitimate (abstract and results, "
                                       f"or a table and the text), but identical statistics for different analyses "
                                       f"deserve a check."),
                          details={"count": len(items), "pages": pages,
                                   "sentences": [s.sentence for s in items[1:]]}))
    return flags


# ---------------------------------------------------------------- driver

def run_all(stats: list[Stat], means: list[MeanSD], sample_sizes: list[dict], items: int = 1) -> list[Flag]:
    flags: list[Flag] = []
    for st in stats:
        f = check_p_values(st)
        if f:
            flags.append(f)
    for m in means:
        flags.extend(check_grim(m, items=items))
    flags.extend(check_df_vs_n(stats, sample_sizes))
    flags.extend(check_duplicates(stats))
    order = {"error": 0, "warning": 1, "info": 2}
    flags.sort(key=lambda f: (order.get(f.severity, 3), f.page))
    return flags
