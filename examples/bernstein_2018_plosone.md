# papercheck report: bernstein_2018_plosone.pdf

Generated 2026-11-08 with papercheck 0.1.0. 21 pages, 16 test statistics with p values, 35 reported means (0 with an N in the same sentence).

## Summary

| Check | Items examined | Errors | Warnings | Info |
|---|---:|---:|---:|---:|
| p value recomputation (statcheck style) | 16 | 0 | 0 | 0 |
| GRIM (means of integer data) | 0 | 0 | 0 | 0 |
| GRIMMER (SDs of integer data) | 0 | 0 | 0 | 0 |
| Degrees of freedom vs reported N | 16 | 0 | 0 | 0 |
| Duplicated statistics | 16 | 0 | 0 | 0 |

Total flags: 0 (errors 0, warnings 0, info 0).

Severity: an error is a reported vs recomputed p value on different sides of .05 (the conclusion about significance would change). A warning is a numeric inconsistency that does not change the decision, or a GRIM failure. Info items are worth a look but have common benign explanations.

## Flagged items

No inconsistencies found by the automated checks.
## All extracted test statistics

| Page | Statistic | Reported p | Recomputed p | Status |
|---:|---|---|---|---|
| 5 | t(117) = 13.2 | p < 0.001 | 0.0 | ok |
| 5 | t(117) = 6.38 | p < 0.001 | 0.0 | ok |
| 5 | t(117) = 2.22 | p = 0.028 | 0.028346 | ok |
| 7 | t(119) = 12.28 | p < 0.001 | 0.0 | ok |
| 7 | t(119) = 4.46 | p < 0.001 | 1.9e-05 | ok |
| 7 | t(119) = 4.47 | p < 0.001 | 1.8e-05 | ok |
| 9 | t(135) = 14.83 | p < 0.001 | 0.0 | ok |
| 9 | t(135) = 2.61 | p = 0.01 | 0.010076 | ok |
| 9 | t(135) = 3.82 | p < 0.001 | 0.000203 | ok |
| 11 | F(2, 143) = 46.01 | p < 0.001 | 0.0 | ok |
| 11 | F(2, 143) = 11.13 | p < 0.001 | 3.2e-05 | ok |
| 12 | F(2, 143) = 22.05 | p < 0.001 | 0.0 | ok |
| 13 | t(233) = 16.64 | p < 0.001 | 0.0 | ok |
| 13 | t(233) = 6.48 | p < 0.001 | 0.0 | ok |
| 13 | t(223) = 3.08 | p = 0.002 | 0.00233 | ok |
| 14 | t(223) = 6.27 | p < 0.001 | 0.0 | ok |

## Notes and limitations

This report lists places where a value reported in the paper differs from the value recomputed from other reported numbers. A difference is not evidence of misconduct. Common benign causes are rounding, typos, one-tailed tests, corrections for multiple comparisons, adjusted degrees of freedom, non-integer scales (which make GRIM and GRIMMER inapplicable) and PDF text-extraction errors. Each flag should be read in the paper before drawing any conclusion.

GRIM and GRIMMER assume every score is a whole number and that the N in the same sentence or parenthesis is the N behind that mean; both assumptions fail for averaged multi-item scales, continuous measures and subgroup means. The df vs N check only flags tests whose df imply more participants than the paper mentions anywhere. Duplicated statistics are usually legitimate repetition.
