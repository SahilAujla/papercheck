# papercheck report: choi_2024_plosone.pdf

Generated 2026-11-08 with papercheck 0.1.0. 21 pages, 33 test statistics with p values, 68 reported means (0 with a usable N for GRIM).

## Summary

| Check | Items examined | Errors | Warnings | Info |
|---|---:|---:|---:|---:|
| p value recomputation (statcheck style) | 33 | 0 | 1 | 0 |
| GRIM (means of integer data) | 0 | 0 | 0 | 0 |
| GRIMMER (SDs of integer data) | 0 | 0 | 0 | 0 |
| Degrees of freedom vs reported N | 33 | 0 | 0 | 0 |
| Duplicated statistics | 33 | 0 | 0 | 0 |

Total flags: 1 (errors 0, warnings 1, info 0).

Severity: an error is a reported vs recomputed p value on different sides of .05 (the conclusion about significance would change). A warning is a numeric inconsistency that does not change the decision, or a GRIM failure. Info items are worth a look but have common benign explanations.

## Flagged items

### 1. [WARNING] p value recomputation (statcheck style), page 15

Reported: `t(184.671) = 2.781, p = .036`

Sentence: "However, among targets described as being highly prosocial, while targets described as having a high desire for status were given less status (M = 5.00, 95% CI [4.78, 5.22]) than targets described as having a low desire for status (M = 5.42, 95% CI [5.22, 5.63], t(184.671) = 2.781, p = .036, d = .406), this difference was much smaller than among targets with unknown prosocial tendencies."

Reported t(184.671) = 2.781, p = .036. Recomputed p = 0.0060 (range 0.0060 to 0.0060 given rounding of the test statistic) does not match the reported p. The significance decision is unchanged.

Recomputed p = 0.005981 (interval [0.005972, 0.00599]); consistent if one-tailed: False; decision error: False.

## All extracted test statistics

| Page | Statistic | Reported p | Recomputed p | Status |
|---:|---|---|---|---|
| 4 | t(131.49) = -2.602 | p = 0.01 | 0.010331 | ok |
| 4 | t(121.89) = -7.629 | p < 0.001 | 0.0 | ok |
| 4 | t(122.3) = -1.772 | p = 0.079 | 0.078885 | ok |
| 4 | t(133.04) = -3.021 | p = 0.003 | 0.003022 | ok |
| 5 | t(419.65) = -3.918 | p < 0.001 | 0.000104 | ok |
| 5 | t(99.77) = -3.235 | p = 0.002 | 0.00165 | ok |
| 6 | t(192.24) = -4.194 | p < 0.001 | 4.2e-05 | ok |
| 6 | t(207.29) = -10.92 | p < 0.001 | 0.0 | ok |
| 6 | t(240.43) = -3.497 | p < 0.001 | 0.00056 | ok |
| 6 | t(945.66) = 3.074 | p = 0.002 | 0.002173 | ok |
| 6 | t(966) = -6.327 | p < 0.001 | 0.0 | ok |
| 6 | t(958) = -2.26 | p = 0.024 | 0.024045 | ok |
| 6 | t(196.26) = -4.316 | p < 0.001 | 2.5e-05 | ok |
| 6 | t(530.6) = -1.78 | p = 0.076 | 0.075648 | ok |
| 6 | t(136.06) = -5.99 | p < 0.001 | 0.0 | ok |
| 8 | F(2, 600) = 71.6 | p < 0.001 | 0.0 | ok |
| 8 | t(341.723) = 9.527 | p < 0.001 | 0.0 | ok |
| 8 | t(319.664) = 9.538 | p < 0.001 | 0.0 | ok |
| 8 | F(2, 600) = 0.475 | p = 0.622 | 0.622119 | ok |
| 8 | F(2, 600) = 2.095 | p = 0.124 | 0.12397 | ok |
| 8 | F(2, 600) = 2.27 | p = 0.104 | 0.104199 | ok |
| 8 | F(2, 600) = 106.868 | p < 0.001 | 0.0 | ok |
| 8 | F(2, 600) = 16.993 | p < 0.001 | 0.0 | ok |
| 11 | F(2, 294) = 26.745 | p < 0.001 | 0.0 | ok |
| 12 | F(2, 294) = 57.463 | p < 0.001 | 0.0 | ok |
| 12 | F(2, 294) = 6.583 | p = 0.002 | 0.001597 | ok |
| 14 | t(367.565) = 6.514 | p < 0.001 | 0.0 | ok |
| 15 | t(378.927) = 4.701 | p < 0.001 | 4e-06 | ok |
| 15 | F(1, 383) = 8.668 | p = 0.003 | 0.003436 | ok |
| 15 | t(185.835) = 6.588 | p < 0.001 | 0.0 | ok |
| 15 | t(184.671) = 2.781 | p = 0.036 | 0.005981 | flagged |
| 15 | F(1, 383) = 8.526 | p = 0.004 | 0.003708 | ok |
| 15 | F(1, 383) = 5.412 | p = 0.021 | 0.02052 | ok |

## Notes and limitations

This report lists places where a value reported in the paper differs from the value recomputed from other reported numbers. A difference is not evidence of misconduct. Common benign causes are rounding, typos, one-tailed tests, corrections for multiple comparisons, adjusted degrees of freedom, non-integer scales (which make GRIM and GRIMMER inapplicable) and PDF text-extraction errors. Each flag should be read in the paper before drawing any conclusion.

GRIM and GRIMMER assume every score is a whole number and that the N in the same sentence or parenthesis is the N behind that mean; both assumptions fail for averaged multi-item scales, continuous measures and subgroup means. The df vs N check only flags tests whose df imply more participants than the paper mentions anywhere. Duplicated statistics are usually legitimate repetition.
