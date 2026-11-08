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
- 55 pytest tests passed at the end of phase 1 (87 after phase 2) (`.venv/bin/python -m pytest -q`).
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

## Phase 2 (04:00 to 04:30 EST)

- Table extraction (`papercheck/tables.py`): PyMuPDF `find_tables()` with cells rebuilt from positioned words, because
  `extract()` reorders characters in some PDFs (Yan 2018 page 9 reads "0.84" as "084 ."; a synthetic table read "3.51"
  as "351 ."). Handles M/SD/n columns, `M (SD)` cells under `Group (n = 23)` headers, and an n row. Table means count
  as strong N for GRIM. Fixture `tests/fixtures/yan_2018_p9_table.json` (a coefficient table, must yield no means) plus
  ruled-table PDFs generated in `tests/test_tables.py`. None of the 13 papers has a ruled M/SD/n table, so the real
  effect so far is zero extra GRIM coverage; the code path is tested on generated PDFs only.
- Evidence scaled to 13 PLOS ONE papers (`examples/SUMMARY.md`, `examples/SOURCES.md`): 418 statistics, 0 errors,
  36 warnings, 169 info. Triage of the 17 pre-fix p-recompute warnings: 8 true reported vs recomputed differences
  (all decision-preserving), 6 likely benign (one Bonferroni-style 6x p, continuity correction, rounding), 1 extraction
  mistake. Extraction false-positive estimate about 7 percent of triaged warnings before the fixes.
- Bugs fixed with regression tests: `t(334) < 0.01` comparator now bounds the recomputed p; table-like `M (SD)` cells no
  longer borrow the nearest preceding n; df vs N is info when the sentence has repeated-measures wording; sample-size
  regex rejects number tails ("0.016 with participants") and "Study 2 revealed". These removed or downgraded 2 extraction
  mistakes and 8 of 22 df vs N warnings.
- `docs/findings/yan-2018.md`: 2 x 2 table rebuilt two ways (percentages and the public S1 Data) as [[25, 8], [29, 27]];
  Pearson chi2 = 5.00, p = 0.0253; Yates p = 0.044; Fisher exact p = 0.0423 (rounds to the reported 0.042). Reading:
  the sentence pairs the Pearson statistic with the Fisher p. Significance at .05 holds under every test. The other two
  chi-squares in the paper reproduce exactly.
- New checks (`papercheck/extra_checks.py`, 21 tests): unverifiable statements (blanket ps, statistics without p, p
  without statistic, capped at 40), 95% CI symmetry (additive and ratio scales), regression b/SE/p consistency.
  On the 13 papers: 1 CI warning (`r = .23, SE = .05, CI95 = [.14, .21]`, buchanan 2023 page 12, where the point lies
  outside its own interval) plus four bootstrap mediation intervals downgraded to info because such intervals are
  asymmetric by design; 0 regression flags; 149 unverifiable info items.
- HTML report (`--html`): static page rendered from the Markdown, no scripts, system font, light and dark.
- 88 tests pass.

## Round 3 (04:19 to 04:42 EST): hand verification of the 8 true-inconsistency items

- `docs/findings/` now holds write-ups for gill 2023 (item 2), michelkrohler 2023 (items 4, 5 in one file, item 7 in
  `-item7.md`), urschler 2024 (items 12, 14) and the earlier yan 2018. Each re-reads the PDF page, recomputes two-tailed
  and one-tailed p with scipy from the printed statistic and df, searches the whole PDF for Bonferroni, Holm, FDR,
  Greenhouse-Geisser and one-tailed statements, gives rounding intervals, benign explanations, what would settle it, and
  closes with an explicit no-inference-about-conduct paragraph.
- Outcome: 8 of 8 items confirmed (6 at the time this paragraph was first written) as reported vs recomputed discrepancies with the significance conclusion
  unchanged in every case. No stated correction or one-tailed test explains any of them. Three (michelkrohler) are one
  unit in the last decimal, consistent with truncating software output; gill's p = .001 vs .0068 and urschler's
  .073 vs .105 and .427 vs .357 look like transcription slips from ANOVA tables; neighbouring tests in the same
  sentences recompute correctly.
- Items 8 and 9 (takahashi 2023, `docs/findings/takahashi_2023_plosone.md`) landed at 04:22 EST: both confirmed
  discrepancies, conclusions unchanged. Item 8 is informative: the reported eta-p2 = .036 agrees with an F of about
  5.5 and with the reported p = .004, so the printed F = 5.12 is the value that does not fit. Item 9: r(286) = .15 gives
  p = .011, not .037; the df matches the described sample, so r or p is the misprint. Final tally: 8 of 8 items are
  reported vs recomputed discrepancies with no stated correction or one-tailed test explaining them, and none changes a
  significance conclusion.
- `examples/SUMMARY.md` has a Hand-verified column; `docs/outreach.md` now links https://github.com/SahilAujla/papercheck
  and says the repo is private until Sahil makes it public.
- Caveat: all verification was done by agents on the same model family as the extractor; a second human read of each
  finding before citing it in outreach is still the right step.

## Left after phase 2

- df vs N still warns 14 times, mostly takayama 2023 (29 participants x 3 days, design wording not in the sentence);
  the downgrade should also look at the page or the Methods section, or detect df2 as a multiple of N - 1.
- The unverifiable list is long; group it per page in the report or make it opt-in (`--unverifiable`).
- Regression check has no real-paper hit yet; needs a paper with `b = x, SE = y, p = z` text to validate.

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
.venv/bin/papercheck data/*.pdf --out reports/ --html
diff <(sed 1,3d reports/yan_2018_plosone.md) <(sed 1,3d examples/yan_2018_plosone.md)   # regression check
git log --oneline
```
