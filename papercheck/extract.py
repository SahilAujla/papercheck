"""Regex extraction of APA-style test statistics and reported means from text."""
from __future__ import annotations

import re
from typing import Iterable, Optional

from .models import MeanSD, Stat
from .pdf import Page, sentence_at

NUM = r"-?\s?(?:\d+(?:[.,]\d+)?|[.,]\d+)"
DF = r"\d+(?:\.\d+)?"
CMP = r"(?:<=|>=|[=<>])"
# optional extra clauses between the statistic and the p value, e.g. ", MSE = 2.10" or ", d = 0.5"
EXTRA = (r"(?:\s*[,;](?!\s*p\s*" + CMP + r")(?!\s*n\.?s\b)\s*[A-Za-z\u03b7\u00b2'\s0-9_%]{1,25}?\s*" + CMP
         + r"\s*-?\s?[\d.]+(?:\s*\[[^\]]{0,40}\])?%?"
         r"|\s*[,;]\s*\d{2}%?\s*CIs?\s*[=:]?\s*[\[(][^\])]{0,40}[\])])*")
P = (r"\s*[,;]\s*(?:p\s*(?P<pcmp>" + CMP + r")\s*(?P<p>" + NUM + r"|ns|n\.s\.)"
     r"|(?P<ns>ns|n\.s\.))")

T_RE = re.compile(
    r"\bt\s*\(\s*(?P<df1>" + DF + r")\s*\)\s*(?P<vcmp>" + CMP + r")\s*(?P<val>" + NUM + r")" + EXTRA + P,
    re.IGNORECASE)
F_RE = re.compile(
    r"\bF\s*\(\s*(?P<df1>" + DF + r")\s*,\s*(?P<df2>" + DF + r")\s*\)\s*(?P<vcmp>" + CMP + r")\s*(?P<val>"
    + NUM + r")" + EXTRA + P)
CHI_RE = re.compile(
    r"(?:χ\s?2|chi[- ]?squared?|chi2|\bX\s?2|\bx\s?2)\s*\(\s*(?P<df1>" + DF
    + r")\s*(?:[,;]\s*N\s*=\s*(?P<n>\d[\d,]*))?\s*\)\s*(?P<vcmp>" + CMP + r")\s*(?P<val>" + NUM + r")" + EXTRA + P,
    re.IGNORECASE)
R_RE = re.compile(
    r"\br\s*\(\s*(?P<df1>" + DF + r")\s*\)\s*(?P<vcmp>" + CMP + r")\s*(?P<val>" + NUM + r")" + EXTRA + P)
Z_RE = re.compile(
    r"\b[zZ]\s*(?P<vcmp>" + CMP + r")\s*(?P<val>" + NUM + r")" + EXTRA + P)

MEAN_RE = re.compile(
    r"\b(?:M|Mean|mean)\s*=\s*(?P<mean>" + NUM + r")"
    r"(?:\s*[,;]?\s*(?:SD|S\.D\.|sd)\s*=\s*(?P<sd>" + NUM + r"))?"
    r"(?:\s*[,;]?\s*[nN]\s*=\s*(?P<n>\d[\d,]*))?")
# "33.18 (SD = 9.88)" style
MEAN_PAREN_RE = re.compile(r"(?<![\d.\-=])(?P<mean>\d{1,4}\.\d{1,3})\s*\(\s*SD\s*=\s*(?P<sd>" + NUM + r")\s*\)")
_ONES = {w: i for i, w in enumerate("zero one two three four five six seven eight nine ten eleven twelve thirteen "
                                    "fourteen fifteen sixteen seventeen eighteen nineteen".split())}
_TENS = {w: i * 10 for i, w in enumerate("_ _ twenty thirty forty fifty sixty seventy eighty ninety".split()) if w != "_"}
_WORDNUM = r"(?:(?:" + "|".join(list(_ONES) + list(_TENS)) + r"|hundred|thousand|and)[\s-]*){1,6}"
WORDNUM_RE = re.compile(r"\b(?P<w>" + _WORDNUM + r")(?=\s*(?:\(|participants|students|respondents|subjects|"
                        r"undergraduates|adults|children|individuals|people|volunteers|patients|women|men|"
                        r"workers|employees|MTurk|Mechanical))", re.IGNORECASE)
# "3.42 (1.10)" style cells, only used when the surrounding text announces an M (SD) layout
CELL_RE = re.compile(r"(?<![\d.\-])(?P<mean>\d{1,3}\.\d{1,2})\s*\(\s*(?P<sd>\d{1,3}\.\d{1,2})\s*\)(?![\d.%])")
N_RE = re.compile(r"\b[nN]\s*=\s*(?P<n>\d[\d,]*)")
SAMPLE_RE = re.compile(
    r"\b(?P<n>\d{1,3}(?:,\d{3})*|\d+)\s+(?:(?:[A-Za-z-]+\s+){0,2})?"
    r"(?:participants|students|respondents|subjects|undergraduates|adults|children|individuals|"
    r"people|volunteers|patients|women|men|infants|workers|employees)\b", re.IGNORECASE)


def _num(s: str) -> float:
    return float(s.replace(" ", "").replace(",", "."))


def _decimals(s: str) -> int:
    s = s.strip().replace(" ", "").replace(",", ".")
    return len(s.split(".")[1]) if "." in s else 0


def _int(s: Optional[str]) -> Optional[int]:
    if s is None:
        return None
    return int(s.replace(",", ""))


def _p_parts(m: re.Match) -> tuple[Optional[float], Optional[str], int]:
    gd = m.groupdict()
    if gd.get("ns"):
        return None, "ns", 2
    p_txt = gd.get("p")
    if p_txt is None:
        return None, None, 2
    if p_txt.lower().startswith("n"):
        return None, "ns", 2
    cmp_ = gd.get("pcmp") or "="
    cmp_ = {"<=": "<", ">=": ">"}.get(cmp_, cmp_)
    return _num(p_txt), cmp_, _decimals(p_txt)


def _stat(kind: str, m: re.Match, page: Page) -> Optional[Stat]:
    gd = m.groupdict()
    try:
        val = _num(gd["val"])
    except ValueError:
        return None
    p, pcmp, pdec = _p_parts(m)
    vcmp = {"<=": "<", ">=": ">"}.get(gd.get("vcmp") or "=", gd.get("vcmp") or "=")
    df1 = float(gd["df1"]) if gd.get("df1") else None
    df2 = float(gd["df2"]) if gd.get("df2") else None
    if kind == "r" and abs(val) > 1:
        return None
    if kind == "z" and _looks_like_zscore_noise(page.text, m.start()):
        return None
    return Stat(kind=kind, value=val, value_decimals=_decimals(gd["val"]), df1=df1, df2=df2,
                n=_int(gd.get("n")), value_comparator=vcmp, p_reported=p, p_comparator=pcmp,
                p_decimals=pdec, raw=re.sub(r"\s+", " ", m.group(0)).strip(), page=page.number,
                sentence=sentence_at(page.text, m.start()), pos=m.start())


def _looks_like_zscore_noise(text: str, pos: int) -> bool:
    """Skip 'z = ' when preceded by a letter (e.g. 'Hz = ' or variable names)."""
    return pos > 0 and text[pos - 1].isalnum()


def extract_stats(pages: Iterable[Page]) -> list[Stat]:
    stats: list[Stat] = []
    for page in pages:
        taken: list[tuple[int, int]] = []
        for kind, rx in (("F", F_RE), ("chi2", CHI_RE), ("t", T_RE), ("r", R_RE), ("z", Z_RE)):
            for m in rx.finditer(page.text):
                span = (m.start(), m.end())
                if any(a < span[1] and span[0] < b for a, b in taken):
                    continue
                s = _stat(kind, m, page)
                if s is not None:
                    stats.append(s)
                    taken.append(span)
    stats.sort(key=lambda s: (s.page, s.pos))
    return stats


def extract_means(pages: Iterable[Page]) -> list[MeanSD]:
    out: list[MeanSD] = []
    for page in pages:
        for m in MEAN_RE.finditer(page.text):
            gd = m.groupdict()
            n = _int(gd.get("n"))
            n_source = "same parenthesis" if n else ""
            sent = sentence_at(page.text, m.start())
            if n is None:
                n, n_source = _n_in_sentence(sent)
            if n is None:
                n, n_source = _n_preceding(page.text, m.start())
            sd = _num(gd["sd"]) if gd.get("sd") else None
            out.append(MeanSD(mean=_num(gd["mean"]), mean_text=gd["mean"].strip(), sd=sd,
                              sd_text=gd["sd"].strip() if gd.get("sd") else None, n=n, n_source=n_source,
                              raw=re.sub(r"\s+", " ", m.group(0)).strip(), page=page.number,
                              sentence=sent, pos=m.start()))
        for m in MEAN_PAREN_RE.finditer(page.text):
            sent = sentence_at(page.text, m.start())
            n, n_source = _n_in_sentence(sent)
            if n is None:
                n, n_source = _n_preceding(page.text, m.start())
            out.append(MeanSD(mean=_num(m["mean"]), mean_text=m["mean"], sd=_num(m["sd"]), sd_text=m["sd"].strip(),
                              n=n, n_source=n_source, raw=re.sub(r"\s+", " ", m.group(0)).strip(), page=page.number,
                              sentence=sent, pos=m.start()))
        if re.search(r"\bM\s*\(\s*SD\s*\)|Mean\s*\(\s*SD\s*\)|\bSD\s*in parentheses", page.text):
            for m in CELL_RE.finditer(page.text):
                sent = sentence_at(page.text, m.start())
                n, n_source = _n_in_sentence(sent)
                out.append(MeanSD(mean=_num(m["mean"]), mean_text=m["mean"], sd=_num(m["sd"]),
                                  sd_text=m["sd"], n=n, n_source=n_source,
                                  raw=m.group(0), page=page.number, sentence=sent, pos=m.start()))
    out.sort(key=lambda x: (x.page, x.pos))
    return out


def _n_in_sentence(sent: str) -> tuple[Optional[int], str]:
    ns = {_int(m["n"]) for m in N_RE.finditer(sent)}
    ns = {n for n in ns if n is not None}
    if len(ns) == 1:
        return ns.pop(), "same sentence"
    return None, ""


def _n_preceding(text: str, pos: int, window: int = 50000) -> tuple[Optional[int], str]:
    """Nearest 'n = X' or 'N = X' before pos on the same page (lower confidence than the same sentence)."""
    last = None
    for m in N_RE.finditer(text, max(0, pos - window), pos):
        last = m
    if last is None:
        return None, ""
    n = _int(last["n"])
    if n is None or n < 2:
        return None, ""
    return n, "nearest preceding N on the page"


def extract_sample_sizes(pages: Iterable[Page]) -> list[dict]:
    """Candidate sample sizes mentioned anywhere: 'N = 120', 'n = 40', '87 participants'."""
    found: list[dict] = []
    for page in pages:
        for m in N_RE.finditer(page.text):
            n = _int(m["n"])
            if n and 2 <= n <= 1_000_000:
                found.append({"n": n, "page": page.number, "raw": m.group(0), "kind": "N ="})
        for m in SAMPLE_RE.finditer(page.text):
            n = _int(m["n"])
            if n and 2 <= n <= 1_000_000:
                found.append({"n": n, "page": page.number, "raw": m.group(0), "kind": "count noun"})
        for m in WORDNUM_RE.finditer(page.text):
            n = words_to_int(m["w"])
            if n is not None and 2 <= n <= 100_000:
                found.append({"n": n, "page": page.number, "raw": m.group(0).strip(), "kind": "spelled out"})
    return found


def words_to_int(words: str) -> Optional[int]:
    """'Two-hundred and thirty-five' -> 235. Returns None for phrases that are not numbers."""
    total, current, seen = 0, 0, False
    for w in re.split(r"[\s-]+", words.strip().lower()):
        if not w or w == "and":
            continue
        if w in _ONES:
            current += _ONES[w]; seen = True
        elif w in _TENS:
            current += _TENS[w]; seen = True
        elif w == "hundred":
            current = (current or 1) * 100; seen = True
        elif w == "thousand":
            total += (current or 1) * 1000; current = 0; seen = True
        else:
            return None
    return total + current if seen else None
