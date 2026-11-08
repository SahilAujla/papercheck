# papercheck report: moyal_2020_plosone.pdf

Generated 2026-11-08 with papercheck 0.1.0. 16 pages, 26 test statistics with p values, 22 reported means (11 with an N in the same sentence).

## Summary

| Check | Items examined | Errors | Warnings | Info |
|---|---:|---:|---:|---:|
| p value recomputation (statcheck style) | 26 | 0 | 0 | 0 |
| GRIM (means of integer data) | 11 | 0 | 0 | 0 |
| GRIMMER (SDs of integer data) | 11 | 0 | 0 | 0 |
| Degrees of freedom vs reported N | 26 | 0 | 0 | 0 |
| Duplicated statistics | 26 | 0 | 0 | 0 |

Total flags: 0 (errors 0, warnings 0, info 0).

Severity: an error is a reported vs recomputed p value on different sides of .05 (the conclusion about significance would change). A warning is a numeric inconsistency that does not change the decision, or a GRIM failure. Info items are worth a look but have common benign explanations.

## Flagged items

No inconsistencies found by the automated checks.
## All extracted test statistics

| Page | Statistic | Reported p | Recomputed p | Status |
|---:|---|---|---|---|
| 4 | t(355) = 0.69 | p = 0.49 | 0.490645 | ok |
| 4 | F(2, 354) = 5.93 | p = 0.003 | 0.00293 | ok |
| 4 | t(354) = -2.78 | p = 0.006 | 0.005726 | ok |
| 4 | t(354) = 2.04 | p = 0.04 | 0.042092 | ok |
| 4 | t(354) = -3.42 | p = 0.001 | 0.000699 | ok |
| 4 | t(354) = -1.36 | p = 0.17 | 0.174695 | ok |
| 6 | F(2, 360) = 0.17 | p = 0.85 | 0.843733 | ok |
| 6 | t(360) = 0.56 | p = 0.57 | 0.575828 | ok |
| 6 | t(360) = 0.13 | p = 0.89 | 0.896639 | ok |
| 7 | t(108) = 15.28 | p < 0.001 | 0.0 | ok |
| 7 | t(108) = 21.08 | p < 0.001 | 0.0 | ok |
| 7 | t(108) = 17.0 | p < 0.001 | 0.0 | ok |
| 7 | t(220) = 18.26 | p < 0.001 | 0.0 | ok |
| 7 | t(220) = 21.39 | p < 0.001 | 0.0 | ok |
| 7 | t(220) = 18.17 | p < 0.001 | 0.0 | ok |
| 9 | t(367) = 0.99 | p = 0.32 | 0.322826 | ok |
| 9 | F(2, 366) = 3.71 | p = 0.03 | 0.025403 | ok |
| 9 | t(366) = -1.96 | p = 0.05 | 0.050754 | ok |
| 9 | t(366) = 1.88 | p = 0.06 | 0.060902 | ok |
| 9 | t(366) = -2.64 | p = 0.01 | 0.008645 | ok |
| 9 | t(366) = -0.76 | p = 0.45 | 0.447744 | ok |
| 11 | F(1, 436) = 0.37 | p = 0.54 | 0.543321 | ok |
| 11 | F(1, 436) = 3.34 | p = 0.07 | 0.068298 | ok |
| 11 | F(1, 436) = 5.24 | p = 0.02 | 0.022551 | ok |
| 11 | t(217) = 1.22 | p = 0.22 | 0.223789 | ok |
| 11 | t(219) = -2.0 | p = 0.047 | 0.046736 | ok |

## Notes and limitations

This report lists places where a value reported in the paper differs from the value recomputed from other reported numbers. A difference is not evidence of misconduct. Common benign causes are rounding, typos, one-tailed tests, corrections for multiple comparisons, adjusted degrees of freedom, non-integer scales (which make GRIM and GRIMMER inapplicable) and PDF text-extraction errors. Each flag should be read in the paper before drawing any conclusion.

GRIM and GRIMMER assume every score is a whole number and that the N in the same sentence or parenthesis is the N behind that mean; both assumptions fail for averaged multi-item scales, continuous measures and subgroup means. The df vs N check only flags tests whose df imply more participants than the paper mentions anywhere. Duplicated statistics are usually legitimate repetition.
