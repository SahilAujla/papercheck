"""Command line entry point: papercheck paper.pdf [more.pdf ...] --out reports/"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .checks import run_all
from .extract import extract_means, extract_sample_sizes, extract_stats
from .pdf import load_pdf, load_text
from .report import build_payload, to_json, to_markdown


def analyze(path: str, items: int = 1) -> dict:
    p = Path(path)
    pages = load_text(p.read_text(errors="replace")) if p.suffix.lower() in (".txt", ".md") else load_pdf(str(p))
    stats = extract_stats(pages)
    means = extract_means(pages)
    sizes = extract_sample_sizes(pages)
    flags = run_all(stats, means, sizes, items=items)
    return build_payload(p.name, stats, means, sizes, flags, len(pages))


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="papercheck",
                                 description="Check reported statistics in a paper for internal consistency.")
    ap.add_argument("paths", nargs="+", help="PDF files (or .txt files with extracted text)")
    ap.add_argument("--out", default="reports", help="output directory (default: reports/)")
    ap.add_argument("--items", type=int, default=1, help="items per scale for GRIM (default 1)")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args(argv)
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    rc = 0
    for path in args.paths:
        try:
            payload = analyze(path, items=args.items)
        except Exception as exc:  # keep going with the other papers
            print(f"{path}: failed: {exc}", file=sys.stderr)
            rc = 1
            continue
        stem = Path(path).stem
        (out / f"{stem}.md").write_text(to_markdown(payload), encoding="utf-8")
        (out / f"{stem}.json").write_text(to_json(payload), encoding="utf-8")
        s = payload["summary"]
        if not args.quiet:
            sev = s["flags_by_severity"]
            print(f"{Path(path).name}: {s['statistics_extracted']} statistics, {s['means_extracted']} means, "
                  f"{s['flags_total']} flags (errors {sev.get('error', 0)}, warnings {sev.get('warning', 0)}, "
                  f"info {sev.get('info', 0)}) -> {out / (stem + '.md')}")
    return rc
