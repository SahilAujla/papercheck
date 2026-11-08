"""Extra checks: unverifiable statistics, confidence interval symmetry, regression coefficients.

Each public function takes an iterable of Page objects and returns a list of Flag objects.
"""
from __future__ import annotations

import math
import re
from typing import Iterable, Optional

from scipy import stats as sps

from .checks import compute_p
from .extract import CMP, DF, NUM, _decimals, _num
from .models import Flag
from .pdf import _SENT_BOUNDARY, Page, sentence_at

ALPHA = 0.05
MAX_UNVERIFIABLE = 40

# ---------------------------------------------------------------- helpers


def _fp(p: float) -> str:
    if p < 0.001:
        return f"{p:.2e}"
    return f"{p:.4f}"


def _clean(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def _sentence_start(text: str, pos: int) -> int:
    start = 0
    for m in _SENT_BOUNDARY.finditer(text, 0, pos):
        start = m.end()
    return start


def _overlaps(span: tuple[int, int], spans: list[tuple[int, int]]) -> bool:
    return any(a < span[1] and span[0] < b for a, b in spans)


def _reported_p_bounds(cmp_: str, p: float, d: int) -> tuple[float, float]:
    cmp_ = {"<=": "<", ">=": ">"}.get(cmp_, cmp_)
    if cmp_ == "<":
        return 0.0, p
    if cmp_ == ">":
        return p, 1.0
    half = 0.5 * 10 ** (-d)
    if p == 0:
        return 0.0, half
    return max(0.0, p - half), min(1.0, p + half)


def _reported_significant(cmp_: str, p: float) -> Optional[bool]:
    cmp_ = {"<=": "<", ">=": ">"}.get(cmp_, cmp_)
    if cmp_ == "<":
        return True if p <= ALPHA else None
    if cmp_ == ">":
        return False if p >= ALPHA else None
    return p < ALPHA


# ---------------------------------------------------------------- 1. unverifiable

BLANKET_P_RE = re.compile(
    r"\b(?:all\s+)?(?:ps|p\s*-?\s*values?)\s*(?P<cmp>" + CMP + r")\s*(?P<p>" + NUM + r")", re.IGNORECASE)

BARE_T_RE = re.compile(r"\bt\s*\(\s*(?P<df1>" + DF + r")\s*\)\s*(?P<vcmp>" + CMP + r")\s*(?P<val>" + NUM + r")",
                       re.IGNORECASE)
BARE_F_RE = re.compile(r"\bF\s*\(\s*(?P<df1>" + DF + r")\s*,\s*(?P<df2>" + DF + r")\s*\)\s*(?P<vcmp>" + CMP
                       + r")\s*(?P<val>" + NUM + r")")
BARE_R_RE = re.compile(r"\br\s*\(\s*(?P<df1>" + DF + r")\s*\)\s*(?P<vcmp>" + CMP + r")\s*(?P<val>" + NUM + r")")
BARE_CHI_RE = re.compile(
    r"(?:χ\s?2|chi[- ]?squared?|chi2|\bX\s?2|\bx\s?2)\s*\(\s*(?P<df1>" + DF
    + r")\s*(?:[,;]\s*N\s*=\s*(?P<n>\d[\d,]*))?\s*\)\s*(?P<vcmp>" + CMP + r")\s*(?P<val>" + NUM + r")",
    re.IGNORECASE)
BARE_Z_RE = re.compile(r"\b[zZ]\s*(?P<vcmp>" + CMP + r")\s*(?P<val>" + NUM + r")")

# any p value in a sentence: "p < .05", "ps < .05", "p values < .05", "ns"
P_IN_SENT_RE = re.compile(r"\bp\s*" + CMP + r"|\bps\s*" + CMP + r"|\bp\s*-?\s*values?\s*" + CMP + r"|\bn\.?s\.?\b",
                          re.IGNORECASE)
LONE_P_RE = re.compile(r"\bp\s*(?P<cmp>" + CMP + r")\s*(?P<p>" + NUM + r")")
# anything that looks like a test statistic or coefficient with a value
STAT_IN_SENT_RE = re.compile(
    r"(?:\b(?:t|F|r|z|Z|b|B|β|beta|OR|HR|RR|IRR|d|g|Wald|U|W|H|Q|G|rho|ρ|τ|tau|R2|f2|Rs|rs|LR)\b\s*(?:\([^)]{0,30}\))?\s*"
    + CMP + r"|(?:χ\s?2|chi[- ]?squared?|chi2|\bX\s?2|\bx\s?2|\bR\s?2|ΔR2)\s*(?:\([^)]{0,30}\))?\s*" + CMP + r")")


def _z_allowed(text: str, pos: int) -> bool:
    """'z = ' only counts when preceded by a comma, semicolon, parenthesis or sentence start."""
    i = pos - 1
    while i >= 0 and text[i] in " \t":
        i -= 1
    if i < 0:
        return True
    return text[i] in ",;(.\n:"


def check_unverifiable(pages: Iterable[Page],
                       known_spans: Optional[dict[int, list[tuple[int, int]]]] = None) -> list[Flag]:
    """Blanket p statements, test statistics with no p, and p values with no test statistic."""
    known_spans = known_spans or {}
    found: list[tuple[int, int, Flag]] = []  # (page, pos, flag)
    for page in pages:
        text = page.text
        spans = list(known_spans.get(page.number, []))
        taken: list[tuple[int, int]] = []
        # a. blanket p statements
        for m in BLANKET_P_RE.finditer(text):
            raw = _clean(m.group(0))
            found.append((page.number, m.start(), Flag(
                check="unverifiable", severity="info", page=page.number, sentence=sentence_at(text, m.start()),
                raw=raw, explanation=(f"'{raw}' is a blanket p statement covering several tests at once. It cannot be "
                                      f"checked against a specific test statistic."),
                details={"kind": "blanket_p", "p_comparator": m["cmp"], "p": _num(m["p"])})))
        # b. bare test statistics
        for kind, rx in (("F", BARE_F_RE), ("chi2", BARE_CHI_RE), ("t", BARE_T_RE), ("r", BARE_R_RE), ("z", BARE_Z_RE)):
            for m in rx.finditer(text):
                span = (m.start(), m.end())
                if _overlaps(span, spans) or _overlaps(span, taken):
                    continue
                if kind == "z" and not _z_allowed(text, m.start()):
                    continue
                sent = sentence_at(text, m.start())
                if P_IN_SENT_RE.search(sent):
                    continue
                try:
                    val = _num(m["val"])
                except ValueError:
                    continue
                gd = m.groupdict()
                df1 = float(gd["df1"]) if gd.get("df1") else None
                df2 = float(gd["df2"]) if gd.get("df2") else None
                if kind == "r" and abs(val) > 1:
                    continue
                implied = compute_p(kind, val, df1, df2)
                taken.append(span)
                raw = _clean(m.group(0))
                text_p = (f" The statistic implies a two-tailed p = {_fp(implied)}." if implied is not None
                          else " The implied p could not be computed.")
                found.append((page.number, m.start(), Flag(
                    check="unverifiable", severity="info", page=page.number, sentence=sent, raw=raw,
                    explanation=f"'{raw}' is reported without a p value in the same sentence, so it cannot be verified."
                                + text_p,
                    details={"kind": "stat_without_p", "stat": kind, "value": val, "df1": df1, "df2": df2,
                             "p_implied": None if implied is None else round(implied, 6)})))
        # c. p values without any test statistic in the sentence
        for m in LONE_P_RE.finditer(text):
            if _overlaps((m.start(), m.end()), spans):
                continue
            sent = sentence_at(text, m.start())
            if STAT_IN_SENT_RE.search(sent):
                continue
            raw = _clean(m.group(0))
            try:
                p = _num(m["p"])
            except ValueError:
                continue
            found.append((page.number, m.start(), Flag(
                check="unverifiable", severity="info", page=page.number, sentence=sent, raw=raw,
                explanation=f"'{raw}' is a p value without a test statistic in the same sentence, so it cannot be "
                            f"recomputed.",
                details={"kind": "p_without_stat", "p_comparator": m["cmp"], "p": p})))
    found.sort(key=lambda x: (x[0], x[1]))
    flags = [f for _, _, f in found]
    if len(flags) > MAX_UNVERIFIABLE:
        omitted = len(flags) - MAX_UNVERIFIABLE
        last = flags[MAX_UNVERIFIABLE]
        flags = flags[:MAX_UNVERIFIABLE]
        flags.append(Flag(check="unverifiable", severity="info", page=last.page, sentence="", raw="",
                          explanation=f"{omitted} more unverifiable statements were omitted (limit {MAX_UNVERIFIABLE}).",
                          details={"kind": "omitted", "omitted": omitted}))
    return flags


# ---------------------------------------------------------------- 2. CI symmetry

_SEP = r"\s*(?:[,;]|to)\s*"
CI_RE = re.compile(
    r"(?:(?P<lvl>\d{2}(?:\.\d)?)\s*%\s*CIs?|\bCI\s?(?P<lvl2>\d{2})\b|\bCIs?\b)\s*(?:[=:]\s*)?"
    r"(?:[\[(]\s*(?P<a>" + NUM + r")" + _SEP + r"(?P<b>" + NUM + r")\s*[\])]"
    r"|(?P<a2>" + NUM + r")" + _SEP + r"(?P<b2>" + NUM + r"))")
POINT_RE = re.compile(
    r"(?:\b(?P<name>Cohen'?s\s+d|Hedges'?\s+g|M\s?diff|Mdiff|mean\s+difference|difference|estimate|odds\s+ratio|"
    r"hazard\s+ratio|risk\s+ratio|rate\s+ratio|OR|RR|HR|IRR|M|d|g|b|B|β|beta|r)\s*" + CMP + r"\s*(?P<val>" + NUM + r")"
    r"|\b(?P<name2>difference|estimate|effect|OR|HR|RR|IRR|odds\s+ratio|hazard\s+ratio)\s+of\s+(?P<val2>" + NUM + r"))")
_RATIO_NAMES = {"or", "rr", "hr", "irr", "odds ratio", "hazard ratio", "risk ratio", "rate ratio"}


def _point_before(text: str, start: int, stop: int) -> Optional[tuple[str, str, int]]:
    """Nearest point estimate (name, value text, pos) in text[start:stop]."""
    last = None
    for m in POINT_RE.finditer(text, start, stop):
        name = m["name"] or m["name2"]
        val = m["val"] or m["val2"]
        last = (_clean(name), val, m.start())
    return last


def check_ci_symmetry(pages: Iterable[Page]) -> list[Flag]:
    """The point estimate should sit at the (geometric) midpoint of its confidence interval."""
    flags: list[Flag] = []
    for page in pages:
        text = page.text
        prev_end = 0
        for m in CI_RE.finditer(text):
            a_txt = m["a"] if m["a"] is not None else m["a2"]
            b_txt = m["b"] if m["b"] is not None else m["b2"]
            try:
                a, b = _num(a_txt), _num(b_txt)
            except ValueError:
                continue
            start = max(_sentence_start(text, m.start()), prev_end)
            prev_end = m.end()
            point = _point_before(text, start, m.start())
            if point is None:
                continue
            name, val_txt, _ = point
            try:
                val = _num(val_txt)
            except ValueError:
                continue
            sent = sentence_at(text, m.start())
            raw = _clean(text[point[2]:m.end()])
            ratio = name.lower() in _RATIO_NAMES
            ci_dec = min(_decimals(a_txt), _decimals(b_txt))
            dec = _decimals(val_txt)
            details = {"estimate": name, "point": val, "ci": [a, b], "ratio_scale": ratio}
            if a >= b:
                flags.append(Flag(check="ci_symmetry", severity="info", page=page.number, sentence=sent, raw=raw,
                                  explanation=f"The confidence interval [{a_txt.strip()}, {b_txt.strip()}] for "
                                              f"{name} = {val_txt.strip()} is reversed or has zero width (lower bound "
                                              f">= upper bound). Check the order of the bounds.",
                                  details={**details, "kind": "reversed"}))
                continue
            if ratio:
                if a <= 0 or b <= 0 or val <= 0:
                    continue
                mid = math.sqrt(a * b)
                diff_log = abs(math.log(val) - 0.5 * (math.log(a) + math.log(b)))
                slack = (math.log1p(0.5 * 10 ** (-dec) / val) + 0.5 * (math.log1p(0.5 * 10 ** (-ci_dec) / a)
                                                                       + math.log1p(0.5 * 10 ** (-ci_dec) / b))
                         + 0.02 * (math.log(b) - math.log(a)))
                if diff_log <= slack:
                    continue
                expl = (f"Reported {name} = {val_txt.strip()} with CI [{a_txt.strip()}, {b_txt.strip()}]. Ratio "
                        f"intervals are symmetric on the log scale, so the point estimate should be near the geometric "
                        f"midpoint sqrt({a_txt.strip()} x {b_txt.strip()}) = {mid:.{max(dec, 2)}f}. The reported value "
                        f"is {abs(val - mid):.{max(dec, 2)}f} away. The interval may belong to a different estimate, come "
                        f"from a different method, or contain a typo.")
            else:
                mid = (a + b) / 2
                slack = 0.5 * 10 ** (-dec) + 0.5 * 10 ** (-ci_dec) + 0.02 * (b - a)
                if abs(val - mid) <= slack:
                    continue
                expl = (f"Reported {name} = {val_txt.strip()} with CI [{a_txt.strip()}, {b_txt.strip()}]. For a "
                        f"symmetric interval the point estimate should be at the midpoint ({a_txt.strip()} + "
                        f"{b_txt.strip()}) / 2 = {mid:.{max(dec, 2)}f}, but the reported value is "
                        f"{abs(val - mid):.{max(dec, 2)}f} away. The interval may belong to a different estimate, be "
                        f"a bootstrap or otherwise asymmetric interval, or contain a typo.")
                if name == "r":
                    expl += " Correlation intervals from the Fisher z transform are asymmetric for large |r|."
            details.update({"midpoint": round(mid, 6), "difference": round(abs(val - mid), 6), "kind": "asymmetric"})
            # bootstrap, percentile and Fisher-z intervals are asymmetric by construction
            asym_by_design = re.search(r"bootstrap|percentile|bias[- ]corrected|BCa|Fisher|indirect effect|mediat",
                                       sent, re.IGNORECASE) is not None
            if asym_by_design:
                expl += " The sentence describes a bootstrap, percentile or mediation interval, which is asymmetric by design."
                details["asymmetric_by_design"] = True
            flags.append(Flag(check="ci_symmetry", severity="info" if asym_by_design else "warning",
                              page=page.number, sentence=sent, raw=raw,
                              explanation=expl, details=details))
    return flags


# ---------------------------------------------------------------- 3. regression coefficients

_SE = r"(?:SE|S\.E\.|s\.e\.|std\.?\s*err(?:or)?|standard\s+error)"
# clauses allowed between the coefficient/SE and the p value (not a p itself)
_MID = (r"(?:\s*[,;](?!\s*p\s*" + CMP + r")\s*[A-Za-zβη²'\s0-9_%().]{1,25}?\s*" + CMP
        + r"\s*-?\s?[\d.]+(?:\s*\[[^\]]{0,40}\])?%?"
        r"|\s*[,;]\s*\d{2}%?\s*CIs?\s*[=:]?\s*[\[(][^\])]{0,40}[\])])*")
COEF_RE = re.compile(
    r"\b(?P<name>b|B|β|beta|Beta|coefficient|Coefficient|estimate|Estimate|Est\.)\s*" + CMP + r"\s*(?P<b>" + NUM + r")"
    r"(?:\s*\(\s*(?P<se_lbl>" + _SE + r"\s*=\s*)?(?P<se_p>" + NUM + r")\s*\)"
    r"|\s*[,;]?\s*" + _SE + r"\s*=\s*(?P<se>" + NUM + r"))"
    r"(?P<mid>" + _MID + r")"
    r"\s*[,;]\s*p\s*(?P<pcmp>" + CMP + r")\s*(?P<p>" + NUM + r")")
TZ_RE = re.compile(r"\b(?P<tz>t|z|Z|Wald)\s*(?:\(\s*(?P<df>" + DF + r")\s*\))?\s*=\s*(?P<val>" + NUM + r")")
T_DF_RE = re.compile(r"\bt\s*\(\s*(?P<df>" + DF + r")\s*\)")
SE_MENTION_RE = re.compile(_SE, re.IGNORECASE)

_NOTE = (" Small-sample t distributions, robust or clustered standard errors, and one-tailed tests make the normal "
         "approximation differ from the reported p.")


def _p_from_ratio(z: float, df: Optional[float]) -> float:
    if math.isinf(z):
        return 0.0
    if df and df > 0:
        return float(2 * sps.t.sf(abs(z), df))
    return float(2 * sps.norm.sf(abs(z)))


def _ratio_interval(b: float, b_dec: int, se: float, se_dec: int) -> tuple[float, float, float]:
    """(min, point, max) of |b| / SE over the rounding corners of b and SE."""
    hb, hs = 0.5 * 10 ** (-b_dec), 0.5 * 10 ** (-se_dec)
    b_lo, b_hi = b - hb, b + hb
    abs_lo = 0.0 if b_lo < 0 < b_hi else min(abs(b_lo), abs(b_hi))
    abs_hi = max(abs(b_lo), abs(b_hi))
    se_lo, se_hi = se - hs, se + hs
    z_max = math.inf if se_lo <= 0 else abs_hi / se_lo
    z_min = abs_lo / se_hi
    return z_min, abs(b) / se, z_max


def check_regression(pages: Iterable[Page]) -> list[Flag]:
    """Recompute the p value of a regression coefficient from b / SE and compare it with the reported p."""
    flags: list[Flag] = []
    for page in pages:
        text = page.text
        for m in COEF_RE.finditer(text):
            sent = sentence_at(text, m.start())
            gd = m.groupdict()
            se_txt = gd["se"] if gd.get("se") is not None else gd["se_p"]
            if gd.get("se_p") is not None and not gd.get("se_lbl") and not SE_MENTION_RE.search(sent):
                continue  # "b = 0.42 (0.11)" only counts when the sentence talks about standard errors
            try:
                b, se, p_rep = _num(gd["b"]), _num(se_txt), _num(gd["p"])
            except ValueError:
                continue
            if se <= 0:
                continue
            raw = _clean(m.group(0))
            pcmp = {"<=": "<", ">=": ">"}.get(gd["pcmp"], gd["pcmp"])
            p_dec = _decimals(gd["p"])
            # t or z given alongside, and degrees of freedom if any
            tz = TZ_RE.search(gd["mid"] or "")
            df = None
            dfm = T_DF_RE.search(sent)
            if dfm:
                df = float(dfm["df"])
            if tz and tz["df"]:
                df = float(tz["df"])
            z_lo, z_pt, z_hi = _ratio_interval(b, _decimals(gd["b"]), se, _decimals(se_txt))
            p_lo, p_pt, p_hi = _p_from_ratio(z_hi, df), _p_from_ratio(z_pt, df), _p_from_ratio(z_lo, df)
            lo, hi = _reported_p_bounds(pcmp, p_rep, p_dec)
            dist = f"t({int(df) if float(df).is_integer() else df})" if df else "normal"
            details = {"estimate": gd["name"], "b": b, "se": se, "ratio": round(z_pt, 4),
                       "ratio_interval": [round(z_lo, 4), None if math.isinf(z_hi) else round(z_hi, 4)],
                       "distribution": dist, "p_reported": p_rep, "p_comparator": pcmp,
                       "p_recomputed": round(p_pt, 6), "p_recomputed_interval": [round(p_lo, 6), round(p_hi, 6)]}
            eps = 1e-9
            if not (p_hi >= lo - eps and p_lo <= hi + eps):
                rep_sig = _reported_significant(pcmp, p_rep)
                rec_sig = True if p_hi < ALPHA else (False if p_lo >= ALPHA else None)
                decision_error = rep_sig is not None and rec_sig is not None and rep_sig != rec_sig
                details["decision_error"] = decision_error
                sev = "error" if decision_error else "warning"
                expl = (f"Reported {raw}. The coefficient divided by its standard error is {z_pt:.2f}, which gives a "
                        f"two-tailed p = {_fp(p_pt)} (range {_fp(p_lo)} to {_fp(p_hi)} given rounding of b and SE) under "
                        f"the {dist} distribution. This does not match the reported p {pcmp} {gd['p'].strip()}.")
                if decision_error:
                    expl += " The reported and recomputed p fall on different sides of .05, so the significance decision would change."
                flags.append(Flag(check="regression", severity=sev, page=page.number, sentence=sent, raw=raw,
                                  explanation=expl + _NOTE, details={**details, "kind": "p_vs_b_over_se"}))
            if tz:
                try:
                    t_rep = abs(_num(tz["val"]))
                except ValueError:
                    continue
                half = 0.5 * 10 ** (-_decimals(tz["val"]))
                if not (t_rep + half >= z_lo - eps and t_rep - half <= z_hi + eps):
                    flags.append(Flag(
                        check="regression", severity="warning", page=page.number, sentence=sent, raw=raw,
                        explanation=(f"Reported {raw}. The reported {tz['tz']} = {tz['val'].strip()} does not match "
                                     f"b / SE = {z_pt:.2f} (range {z_lo:.2f} to "
                                     f"{'inf' if math.isinf(z_hi) else f'{z_hi:.2f}'} given rounding). One of the three "
                                     f"numbers is probably a typo, or the test statistic uses a different standard error."),
                        details={**details, "kind": "t_vs_b_over_se", "t_reported": t_rep}))
    return flags
