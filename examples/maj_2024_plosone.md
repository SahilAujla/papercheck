# papercheck report: maj_2024_plosone.pdf

Generated 2026-11-08 with papercheck 0.1.0. 19 pages, 23 test statistics with p values, 60 reported means (7 with a usable N for GRIM).

## Summary

| Check | Items examined | Errors | Warnings | Info |
|---|---:|---:|---:|---:|
| p value recomputation (statcheck style) | 23 | 0 | 0 | 0 |
| GRIM (means of integer data) | 7 | 0 | 0 | 2 |
| GRIMMER (SDs of integer data) | 7 | 0 | 0 | 1 |
| Degrees of freedom vs reported N | 23 | 0 | 0 | 0 |
| Duplicated statistics | 23 | 0 | 0 | 0 |

Total flags: 3 (errors 0, warnings 0, info 3).

Severity: an error is a reported vs recomputed p value on different sides of .05 (the conclusion about significance would change). A warning is a numeric inconsistency that does not change the decision, or a GRIM failure. Info items are worth a look but have common benign explanations.

## Flagged items

### 1. [INFO] GRIMMER (SDs of integer data), page 13

Reported: `M = 1.54, SD = 1.44`

Sentence: "User experience of intervention users was rated as moderate (UEQ) [51] assessed above average in the dimension of Perspicuity (M = 1.54, SD = 1.44) and below average in the dimensions of Dependability (M = 0.99, SD = 0.72), Stimulation (M = 0.67, SD = 1.12), Attractiveness (M = 1.18, SD = 1.15) and Efficiency (M = 0.99, SD = 0.97) and Novelty (M = 0.22, SD = 0.72) against the benchmarks provided b..."

GRIMMER: the mean 1.54 passes GRIM, but no whole-number data set of n = 41 (N from the nearest preceding N on the page) has this mean together with SD = 1.44. Applies only if the measure is integer-valued; treat as a prompt to check, not a conclusion.

### 2. [INFO] GRIM (means of integer data), page 13

Reported: `M = 0.99, SD = 0.72`

Sentence: "...er experience of intervention users was rated as moderate (UEQ) [51] assessed above average in the dimension of Perspicuity (M = 1.54, SD = 1.44) and below average in the dimensions of Dependability (M = 0.99, SD = 0.72), Stimulation (M = 0.67, SD = 1.12), Attractiveness (M = 1.18, SD = 1.15) and Efficiency (M = 0.99, SD = 0.97) and Novelty (M = 0.22, SD = 0.72) against the benchmarks provided by..."

GRIM: a mean of 0.99 with n = 41 (N taken from the nearest preceding N on the page) is not possible if each score is a whole number (for example a single Likert item or a count). The nearest possible means are 1.00, 0.98. This only matters if the measure is integer-valued; averaged multi-item scales or continuous measures make GRIM inapplicable.

### 3. [INFO] GRIM (means of integer data), page 13

Reported: `M = 0.67, SD = 1.12`

Sentence: "...was rated as moderate (UEQ) [51] assessed above average in the dimension of Perspicuity (M = 1.54, SD = 1.44) and below average in the dimensions of Dependability (M = 0.99, SD = 0.72), Stimulation (M = 0.67, SD = 1.12), Attractiveness (M = 1.18, SD = 1.15) and Efficiency (M = 0.99, SD = 0.97) and Novelty (M = 0.22, SD = 0.72) against the benchmarks provided by Schrepp et al. [58] based on data f..."

GRIM: a mean of 0.67 with n = 41 (N taken from the nearest preceding N on the page) is not possible if each score is a whole number (for example a single Likert item or a count). The nearest possible means are 0.66, 0.68. This only matters if the measure is integer-valued; averaged multi-item scales or continuous measures make GRIM inapplicable.

## All extracted test statistics

| Page | Statistic | Reported p | Recomputed p | Status |
|---:|---|---|---|---|
| 10 | t(131.99) = -1.77 | p = 0.08 | 0.079036 | ok |
| 10 | t(155) = -1.17 | p = 0.24 | 0.243797 | ok |
| 10 | t(156) = 0.47 | p = 0.64 | 0.639011 | ok |
| 10 | t(156) = 0.06 | p = 0.95 | 0.952232 | ok |
| 10 | t(156) = 0.67 | p = 0.5 | 0.503848 | ok |
| 10 | t(156) = -1.82 | p = 0.07 | 0.070676 | ok |
| 10 | t(156) = -1.64 | p = 0.1 | 0.10302 | ok |
| 10 | t(116.73) = -2.16 | p = 0.03 | 0.032817 | ok |
| 10 | t(152.46) = -2.05 | p = 0.04 | 0.042078 | ok |
| 10 | t(152.3) = -2.34 | p = 0.02 | 0.020581 | ok |
| 12 | F(1, 155) = 8.68 | p = 0.004 | 0.003714 | ok |
| 12 | F(1, 155) = 332.75 | p < 0.001 | 0.0 | ok |
| 12 | F(1, 155) = 0.27 | p = 0.61 | 0.604073 | ok |
| 12 | F(1, 155) = 333.06 | p < 0.001 | 0.0 | ok |
| 12 | F(1, 155) = 3.41 | p = 0.07 | 0.066709 | ok |
| 12 | F(1, 155) = 278.11 | p < 0.001 | 0.0 | ok |
| 12 | F(1, 155) = 5.87 | p = 0.017 | 0.016554 | ok |
| 12 | F(1, 155) = 3.23 | p = 0.07 | 0.074248 | ok |
| 12 | F(1, 155) = 0.01 | p = 0.92 | 0.920474 | ok |
| 13 | F(1, 155) = 157.98 | p < 0.001 | 0.0 | ok |
| 13 | F(1, 155) = 131.77 | p < 0.001 | 0.0 | ok |
| 13 | F(1, 155) = 1.67 | p = 0.2 | 0.198182 | ok |
| 13 | F(1, 155) = 285.35 | p < 0.001 | 0.0 | ok |

## Notes and limitations

This report lists places where a value reported in the paper differs from the value recomputed from other reported numbers. A difference is not evidence of misconduct. Common benign causes are rounding, typos, one-tailed tests, corrections for multiple comparisons, adjusted degrees of freedom, non-integer scales (which make GRIM and GRIMMER inapplicable) and PDF text-extraction errors. Each flag should be read in the paper before drawing any conclusion.

GRIM and GRIMMER assume every score is a whole number and that the N in the same sentence or parenthesis is the N behind that mean; both assumptions fail for averaged multi-item scales, continuous measures and subgroup means. The df vs N check only flags tests whose df imply more participants than the paper mentions anywhere. Duplicated statistics are usually legitimate repetition.
