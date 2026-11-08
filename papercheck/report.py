"""Markdown and JSON reports."""
from __future__ import annotations

import json
import re
from collections import Counter
from datetime import date
from typing import Any

from . import __version__
from .checks import p_interval
from .models import Flag, MeanSD, Stat

CHECK_NAMES = {
    "p_recompute": "p value recomputation (statcheck style)",
    "grim": "GRIM (means of integer data)",
    "grimmer": "GRIMMER (SDs of integer data)",
    "df_vs_n": "Degrees of freedom vs reported N",
    "duplicate": "Duplicated statistics",
    "unverifiable": "Unverifiable statements (ps < .05, statistics without p, p without statistic)",
    "ci_symmetry": "95% CI vs point estimate",
    "regression": "Regression coefficient vs SE and p",
}

DISCLAIMER = (
    "This report lists places where a value reported in the paper differs from the value recomputed from other "
    "reported numbers. A difference is not evidence of misconduct. Common benign causes are rounding, typos, "
    "one-tailed tests, corrections for multiple comparisons, adjusted degrees of freedom, non-integer scales "
    "(which make GRIM and GRIMMER inapplicable) and PDF text-extraction errors. Each flag should be read in the "
    "paper before drawing any conclusion.")


def build_payload(paper: str, stats: list[Stat], means: list[MeanSD], sample_sizes: list[dict],
                  flags: list[Flag], pages: int) -> dict[str, Any]:
    sev = Counter(f.severity for f in flags)
    by_check = Counter(f.check for f in flags)
    examined = {"p_recompute": len([s for s in stats if s.p_comparator]),
                "grim": len([m for m in means if m.n]),
                "grimmer": len([m for m in means if m.n and m.sd is not None]),
                "df_vs_n": len(stats), "duplicate": len(stats),
                "unverifiable": len([f for f in flags if f.check == "unverifiable"]),
                "ci_symmetry": len([f for f in flags if f.check == "ci_symmetry"]),
                "regression": len([f for f in flags if f.check == "regression"])}
    enriched = []
    for s in stats:
        d = s.to_dict()
        iv = p_interval(s)
        d["p_recomputed"] = round(iv[1], 6) if iv else None
        enriched.append(d)
    return {
        "paper": paper, "pages": pages, "papercheck_version": __version__, "date": date.today().isoformat(),
        "summary": {"statistics_extracted": len(stats), "means_extracted": len(means),
                    "means_with_n": examined["grim"], "flags_total": len(flags),
                    "flags_by_severity": dict(sev), "flags_by_check": dict(by_check), "examined": examined},
        "flags": [f.to_dict() for f in flags],
        "statistics": enriched,
        "means": [m.to_dict() for m in means],
        "sample_sizes": sample_sizes,
        "disclaimer": DISCLAIMER,
    }


def to_markdown(payload: dict[str, Any]) -> str:
    s = payload["summary"]
    lines = [f"# papercheck report: {payload['paper']}", "",
             f"Generated {payload['date']} with papercheck {payload['papercheck_version']}. "
             f"{payload['pages']} pages, {s['statistics_extracted']} test statistics with p values, "
             f"{s['means_extracted']} reported means ({s['means_with_n']} with a usable N for GRIM).", "",
             "## Summary", "", "| Check | Items examined | Errors | Warnings | Info |", "|---|---:|---:|---:|---:|"]
    flags = payload["flags"]
    for key, name in CHECK_NAMES.items():
        fl = [f for f in flags if f["check"] == key]
        c = Counter(f["severity"] for f in fl)
        lines.append(f"| {name} | {s['examined'].get(key, 0)} | {c.get('error', 0)} | {c.get('warning', 0)} | "
                     f"{c.get('info', 0)} |")
    sev = s["flags_by_severity"]
    lines += ["", f"Total flags: {s['flags_total']} (errors {sev.get('error', 0)}, warnings {sev.get('warning', 0)}, "
              f"info {sev.get('info', 0)}).", "",
              "Severity: an error is a reported vs recomputed p value on different sides of .05 (the conclusion about "
              "significance would change). A warning is a numeric inconsistency that does not change the decision, or a "
              "GRIM failure. Info items are worth a look but have common benign explanations.", ""]
    lines += ["## Flagged items", ""]
    if not flags:
        lines.append("No inconsistencies found by the automated checks.")
    for i, f in enumerate(flags, 1):
        lines += [f"### {i}. [{f['severity'].upper()}] {CHECK_NAMES.get(f['check'], f['check'])}, page {f['page']}", "",
                  f"Reported: `{f['raw']}`", "", f"Sentence: \"{f['sentence']}\"", "", f"{f['explanation']}", ""]
        det = f.get("details") or {}
        if f["check"] == "p_recompute":
            lines.append(f"Recomputed p = {det.get('p_recomputed')} (interval {det.get('p_recomputed_interval')}); "
                         f"consistent if one-tailed: {det.get('consistent_if_one_tailed')}; "
                         f"decision error: {det.get('decision_error')}.")
            lines.append("")
    lines += ["## All extracted test statistics", "",
              "| Page | Statistic | Reported p | Recomputed p | Status |", "|---:|---|---|---|---|"]
    flagged_raw = {(f["page"], f["raw"]) for f in flags if f["check"] == "p_recompute"}
    for st in payload["statistics"]:
        rp = (f"p {st['p_comparator']} {st['p_reported']}" if st["p_comparator"] != "ns" else "ns")
        status = "flagged" if (st["page"], st["raw"]) in flagged_raw else "ok"
        lines.append(f"| {st['page']} | {_label(st)} | {rp} | {st['p_recomputed']} | {status} |")
    lines += ["", "## Notes and limitations", "", DISCLAIMER, "",
              "GRIM and GRIMMER assume every score is a whole number and that the N in the same sentence or "
              "parenthesis is the N behind that mean; both assumptions fail for averaged multi-item scales, "
              "continuous measures and subgroup means. The df vs N check only flags tests whose df imply more "
              "participants than the paper mentions anywhere. Duplicated statistics are usually legitimate repetition.",
              ""]
    return "\n".join(lines)


def _label(st: dict) -> str:
    def fmt(x):
        if x is None:
            return "?"
        return str(int(x)) if float(x).is_integer() else str(x)
    k = st["kind"]
    if k == "F":
        return f"F({fmt(st['df1'])}, {fmt(st['df2'])}) {st['value_comparator']} {st['value']}"
    if k == "z":
        return f"z {st['value_comparator']} {st['value']}"
    if k == "chi2" and st.get("n"):
        return f"chi2({fmt(st['df1'])}, N = {st['n']}) {st['value_comparator']} {st['value']}"
    return f"{k}({fmt(st['df1'])}) {st['value_comparator']} {st['value']}"


def to_json(payload: dict[str, Any]) -> str:
    return json.dumps(payload, indent=2, ensure_ascii=False)


# ---------------------------------------------------------------- HTML (same content as the Markdown)

_HTML_HEAD = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>
:root {{ --fg: #1b1b1b; --bg: #ffffff; --muted: #5a5a5a; --line: #d9d9d9; --err: #a4262c; --warn: #8a5a00; --info: #2a5d8f; }}
@media (prefers-color-scheme: dark) {{ :root {{ --fg: #e6e6e6; --bg: #141414; --muted: #a0a0a0; --line: #333; --err: #ff8a8a; --warn: #f0c060; --info: #8ab8ff; }} }}
body {{ font: 15px/1.5 -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; color: var(--fg); background: var(--bg); max-width: 60rem; margin: 0 auto; padding: 1rem 16px; }}
table {{ border-collapse: collapse; width: 100%; margin: 0.75rem 0; display: block; overflow-x: auto; }}
th, td {{ border: 1px solid var(--line); padding: 0.3rem 0.6rem; text-align: left; vertical-align: top; }}
th {{ background: rgba(127,127,127,0.08); }}
code {{ font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 0.92em; }}
h1, h2, h3 {{ line-height: 1.25; }} h3 {{ margin-top: 1.5rem; }}
.sev-error {{ color: var(--err); }} .sev-warning {{ color: var(--warn); }} .sev-info {{ color: var(--info); }}
p.muted {{ color: var(--muted); }}
</style></head><body>
"""


def _esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def _inline(s: str) -> str:
    s = _esc(s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\[(ERROR|WARNING|INFO)\]", lambda m: f'<span class="sev-{m.group(1).lower()}">[{m.group(1)}]</span>', s)
    return s


def to_html(payload: dict[str, Any]) -> str:
    """Render the Markdown report as a standalone HTML page (headings, tables, paragraphs, code spans)."""
    md = to_markdown(payload)
    out = [_HTML_HEAD.format(title=_esc(f"papercheck report: {payload['paper']}"))]
    lines = md.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            rows = [r for r in rows if not all(re.fullmatch(r":?-+:?", c) for c in r)]
            out.append("<table>")
            for r_i, r in enumerate(rows):
                tag = "th" if r_i == 0 else "td"
                out.append("<tr>" + "".join(f"<{tag}>{_inline(c)}</{tag}>" for c in r) + "</tr>")
            out.append("</table>")
            continue
        m = re.match(r"^(#{1,3}) (.*)$", line)
        if m:
            out.append(f"<h{len(m.group(1))}>{_inline(m.group(2))}</h{len(m.group(1))}>")
        elif line.strip():
            out.append(f"<p>{_inline(line)}</p>")
        i += 1
    out.append("</body></html>\n")
    return "\n".join(out)
