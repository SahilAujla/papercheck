# NOTES

Working notes for the papercheck build (2026-11-08, 03:42 to 04:35 EST session).

## Done

- Repo at `~/code/papercheck`, Python 3.12 venv in `.venv` via `uv`, `pyproject.toml` with a `papercheck` console script.
- Extractor (`papercheck/extract.py`): t, F, chi-square (chi2, χ2, chi-square spelled out, with optional `N =`), r, z,
  each with `p =`, `p <`, `p >`, `ns`; tolerates `MSE = `, `d = `, `ηp2 = `, `95% CI [..]` clauses between the statistic
  and the p value, unicode minus, `.05` and `0.05`, missing spaces. Means via `M = x, SD = y, n = z`; N fallbacks: same
  parenthesis, same sentence, nearest preceding N on the page. Sample-size candidates from `N = `, `n = ` and
  `<number> participants/students/...`.
- Checks (`papercheck/checks.py`): statcheck-style p recomputation with rounding intervals, decision-error severity,
  one-tailed caveat, `p = .000` handled as `p <`; GRIM and GRIMMER (`papercheck/grim.py`, exact Fractions, tested by
  brute force on 1 to 7 scales); df vs N; duplicates.
- Reports (`papercheck/report.py`): Markdown with summary table, flagged items (page, sentence, severity, explanation),
  full table of extracted statistics with recomputed p, limitations; JSON with the same payload.
- CLI: `papercheck paper.pdf --out reports/` (also `.txt` input, `--items`, `--quiet`).
- 55 pytest tests pass (`.venv/bin/python -m pytest -q`).
- Three real runs, reports committed under `examples/` (PDFs in gitignored `data/`, citations in `examples/SOURCES.md`):
  - Yan, Zhang and Xu 2018 (PLOS ONE): 30 statistics, 59 means, 5 flags. 1 warning: reported χ2(1, N = 89) = 5.00,
    p = 0.042 vs recomputed p = 0.025 (significance decision unchanged). 4 info GRIM flags on page 18 that use the
    study N = 89 for subgroup means, so they are expected false positives.
  - Bernstein et al. 2018 (PLOS ONE): 16 statistics, 35 means, 0 flags. All 16 reported p values match recomputation.
    A first run produced 4 df vs N warnings (t(233) and t(223) vs a largest reported N of 146); hand-checking page 13
    showed the sample is written as "Two-hundred and thirty-five", which the extractor could not read. Spelled-out
    numbers are now parsed and the warnings disappeared, which is the intended behaviour.
  - Moyal and Ritov 2020 (PLOS ONE): 26 statistics, 22 means (11 with an N), 0 flags. All 26 reported p values match
    recomputation and no GRIM or GRIMMER failures.
- Smoke-tested on a fourth paper not in the examples (Hayran et al. 2020, PLOS ONE, CC0, kept in `data/` only):
  27 statistics, 4 means, 2 warnings (F(1, 65) = 6.30 reported p = .02 vs recomputed .015; F(1, 66) = .82 reported
  p = .34 vs recomputed .37), no crashes. Coverage check: on all four papers every `t(`, `F(`, `r(` or `χ2(` followed by
  a value was extracted.
- Console script `.venv/bin/papercheck` works from any directory (the editable install had to be refreshed after
  `__init__.py` was added; `uv pip install -e .` fixes "cannot import name __version__").
- `docs/outreach.md`: what ERROR says about reviewer eligibility and pay, sign-up form, draft email, three other outlets
  (Institute for Replication, Black Spatula Project, PubPeer), next actions.

## Half done or known gaps

- Means in tables (`3.42 (1.10)` cells) are only picked up on pages that announce an `M (SD)` layout, and they rarely get
  an N, so GRIM coverage in tables is thin. Bernstein got no GRIM coverage (its means have no `N =` on the same page; the N is spelled out in the Methods).
- GRIMMER is implemented for `items = 1` only and uses the sample (N-1) SD formula.
- df vs N only fires when the implied N exceeds every N in the paper; it does not try to match group sizes.
- No table-structure parsing (PyMuPDF `find_tables` was not used); two-column layouts are read in text order.
- The outreach email cites a public repo that does not exist yet (local commits only, no GitHub push).
- Science and Nature coverage of ERROR could not be fetched (paywall or 403); the outreach doc marks those claims as
  unverified search snippets.

## Next three steps

1. Hand-check the Yan 2018 χ2 flag and the Bernstein df flags against the PDFs, then write the findings in the
   "reported vs recomputed" style (PubPeer-ready), since those two are the evidence for the ERROR email.
2. Add table extraction with `page.find_tables()` so means with SDs and group ns in tables feed GRIM/GRIMMER with the
   right N, and add `ps < .05` style and effect-size-only statistics to the extractor's coverage report.
3. Push the repo to GitHub (SahilAujla/papercheck), fill the links into `docs/outreach.md`, register on the ERROR expert
   form (https://errorsignup.formr.org/) and send the email.

## Exact commands

```bash
cd ~/code/papercheck
.venv/bin/python -m pytest -q
.venv/bin/papercheck data/*.pdf --out reports/
diff <(sed 1,3d reports/yan_2018_plosone.md) <(sed 1,3d examples/yan_2018_plosone.md)   # regression check
git log --oneline
```
