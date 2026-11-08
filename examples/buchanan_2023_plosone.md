# papercheck report: buchanan_2023_plosone.pdf

Generated 2026-11-08 with papercheck 0.1.0. 26 pages, 35 test statistics with p values, 0 reported means (0 with a usable N for GRIM).

## Summary

| Check | Items examined | Errors | Warnings | Info |
|---|---:|---:|---:|---:|
| p value recomputation (statcheck style) | 35 | 0 | 0 | 0 |
| GRIM (means of integer data) | 0 | 0 | 0 | 0 |
| GRIMMER (SDs of integer data) | 0 | 0 | 0 | 0 |
| Degrees of freedom vs reported N | 35 | 0 | 0 | 0 |
| Duplicated statistics | 35 | 0 | 0 | 0 |

Total flags: 0 (errors 0, warnings 0, info 0).

Severity: an error is a reported vs recomputed p value on different sides of .05 (the conclusion about significance would change). A warning is a numeric inconsistency that does not change the decision, or a GRIM failure. Info items are worth a look but have common benign explanations.

## Flagged items

No inconsistencies found by the automated checks.
## All extracted test statistics

| Page | Statistic | Reported p | Recomputed p | Status |
|---:|---|---|---|---|
| 5 | t(40) = -1.55 | p = 0.129 | 0.129018 | ok |
| 5 | t(34) = -0.11 | p = 0.911 | 0.913056 | ok |
| 6 | t(47) = 1.45 | p = 0.154 | 0.153699 | ok |
| 6 | t(42) = 2.29 | p = 0.027 | 0.027111 | ok |
| 9 | z = -2.58 | p = 0.01 | 0.00988 | ok |
| 9 | z = -2.62 | p = 0.009 | 0.008793 | ok |
| 9 | z = -5.28 | p < 0.001 | 0.0 | ok |
| 9 | z = 7.54 | p < 0.001 | 0.0 | ok |
| 9 | z = 0.28 | p = 0.779 | 0.779478 | ok |
| 9 | z = 1.65 | p = 0.099 | 0.098943 | ok |
| 9 | z = 4.64 | p < 0.001 | 3e-06 | ok |
| 11 | F(2, 208) = 23.98 | p < 0.001 | 0.0 | ok |
| 11 | F(3, 176) = 87.04 | p < 0.001 | 0.0 | ok |
| 11 | F(3, 236) = 75.47 | p < 0.001 | 0.0 | ok |
| 11 | F(5, 499) = 50.89 | p < 0.001 | 0.0 | ok |
| 11 | F(2, 208) = 4.02 | p = 0.019 | 0.019366 | ok |
| 11 | F(3, 176) = 8.24 | p < 0.001 | 3.7e-05 | ok |
| 12 | F(5, 499) = 35.15 | p < 0.001 | 0.0 | ok |
| 12 | z = 7.52 | p < 0.001 | 0.0 | ok |
| 12 | z = 3.05 | p = 0.002 | 0.002288 | ok |
| 12 | z = 13.92 | p < 0.001 | 0.0 | ok |
| 12 | z = 4.69 | p < 0.001 | 3e-06 | ok |
| 13 | t(175) = 6.31 | p < 0.001 | 0.0 | ok |
| 13 | t(175) = 14.97 | p < 0.001 | 0.0 | ok |
| 13 | t(158) = 7.9 | p < 0.001 | 0.0 | ok |
| 13 | t(171) = 8.46 | p < 0.001 | 0.0 | ok |
| 13 | t(168) = 5.76 | p < 0.001 | 0.0 | ok |
| 18 | F(5, 659) = 94.73 | p < 0.001 | 0.0 | ok |
| 18 | F(5, 659) = 5.73 | p < 0.001 | 3.5e-05 | ok |
| 19 | F(5, 659) = 119.2 | p < 0.001 | 0.0 | ok |
| 19 | t(223) = 8.74 | p < 0.001 | 0.0 | ok |
| 19 | t(225) = 26.33 | p < 0.001 | 0.0 | ok |
| 19 | t(225) = 14.23 | p < 0.001 | 0.0 | ok |
| 19 | t(216) = 10.77 | p < 0.001 | 0.0 | ok |
| 19 | t(214) = 3.99 | p < 0.001 | 9.1e-05 | ok |

## Notes and limitations

This report lists places where a value reported in the paper differs from the value recomputed from other reported numbers. A difference is not evidence of misconduct. Common benign causes are rounding, typos, one-tailed tests, corrections for multiple comparisons, adjusted degrees of freedom, non-integer scales (which make GRIM and GRIMMER inapplicable) and PDF text-extraction errors. Each flag should be read in the paper before drawing any conclusion.

GRIM and GRIMMER assume every score is a whole number and that the N in the same sentence or parenthesis is the N behind that mean; both assumptions fail for averaged multi-item scales, continuous measures and subgroup means. The df vs N check only flags tests whose df imply more participants than the paper mentions anywhere. Duplicated statistics are usually legitimate repetition.
