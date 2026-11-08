# papercheck

Statistical consistency checks for research papers, in the spirit of statcheck and GRIM.
Give it a PDF; it extracts the APA-style test statistics and reported means, recomputes what
can be recomputed, and writes a Markdown and a JSON report that list every reported vs
recomputed difference with its page, sentence, severity and a plain-language explanation.

No API keys, no network access at run time. Python 3.10+, PyMuPDF, SciPy.

## What it checks

| Check | What it does | Severity |
|---|---|---|
| p value recomputation | For `t(df) = x, p = y`, `F(df1, df2) = x`, `chi2(df, N = n) = x`, `r(df) = x` and `z = x`, recompute the two-tailed p from the statistic and compare it with the reported p, allowing for rounding of both numbers (statcheck's rule). | warning; **error** when reported and recomputed p sit on opposite sides of .05; info when a one-tailed p would be consistent |
| GRIM | For a reported mean with decimals and a sample size, test whether any whole-number data set of that size can produce that mean. | warning when N comes from the same sentence; info when N is the nearest preceding N on the page |
| GRIMMER | For a mean that passes GRIM, test whether the reported SD is possible for whole-number data (Allard's parity refinement included). | info |
| df vs N | Flag tests whose degrees of freedom imply more participants than the paper mentions anywhere; flag a chi-square N that appears nowhere else. | warning / info |
| Duplicates | The same statistic with the same p value reported more than once. | info |

Severities are deliberately conservative. Every flag is a "reported vs recomputed" difference,
not a judgement about the authors. See the limitations section at the end of every report.

## Install and run

```bash
cd ~/code/papercheck
uv venv .venv --python 3.12          # or: python3 -m venv .venv
uv pip install --python .venv/bin/python -e ".[dev]"   # or: .venv/bin/pip install -e ".[dev]"

.venv/bin/papercheck path/to/paper.pdf --out reports/
.venv/bin/papercheck data/*.pdf --out reports/            # several papers at once
.venv/bin/papercheck paper.pdf --items 3                  # GRIM for 3-item averaged scales
.venv/bin/python -m pytest -q                             # 55 tests
```

`.txt` files are accepted as well as PDFs (handy for tests and for text you have cleaned by hand).
Each run writes `<paper>.md` and `<paper>.json` into `--out`.

## Examples

`examples/` holds reports for three open-access PLOS ONE papers (CC BY 4.0); `examples/SOURCES.md`
has the citations. The PDFs themselves live in `data/`, which is not committed; fetch them with

```bash
curl -sL -A 'papercheck/0.1' -o data/yan_2018_plosone.pdf \
  'https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0196269&type=printable'
```

and likewise for the DOIs listed in `examples/SOURCES.md`.

## Layout

```
papercheck/pdf.py      PDF text (PyMuPDF), normalization, sentence lookup
papercheck/extract.py  regexes for t, F, chi2, r, z with p; means with SD and N; sample sizes
papercheck/checks.py   p recomputation, GRIM/GRIMMER drivers, df vs N, duplicates
papercheck/grim.py     GRIM and GRIMMER (exact rational arithmetic, stdlib only)
papercheck/report.py   Markdown and JSON output
papercheck/cli.py      command line
tests/                 pytest suite
docs/outreach.md       ERROR project eligibility, draft email, other outlets
```

## Known false-positive sources

- GRIM and GRIMMER assume integer data. Averaged multi-item scales, reaction times, percentages and
  difference scores are not integer data; use `--items` for averaged scales or ignore those flags.
- When no N is in the same sentence, GRIM uses the nearest preceding `N =` or `n =` on the page. For
  subgroup means this is the wrong N. Those flags are marked info and name their N source.
- df vs N assumes a between-subjects design. Trials-as-unit analyses, repeated measures, pooled
  samples and multilevel models have df that do not map onto participants.
- One-tailed tests, corrected p values (Bonferroni, Greenhouse-Geisser) and Welch df make the
  recomputed p differ legitimately. One-tailed consistency is reported in each flag.
- PDF text extraction can split or reorder numbers, especially in tables and two-column layouts.
  The sentence shown in each flag is there so the reader can check the original.
- Statistics without a p value, and p values without a statistic (`ps < .05`), are not extracted.
