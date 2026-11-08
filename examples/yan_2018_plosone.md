# papercheck report: yan_2018_plosone.pdf

Generated 2026-11-08 with papercheck 0.1.0. 24 pages, 30 test statistics with p values, 59 reported means (11 with an N in the same sentence).

## Summary

| Check | Items examined | Errors | Warnings | Info |
|---|---:|---:|---:|---:|
| p value recomputation (statcheck style) | 30 | 0 | 1 | 0 |
| GRIM (means of integer data) | 11 | 0 | 0 | 4 |
| GRIMMER (SDs of integer data) | 11 | 0 | 0 | 0 |
| Degrees of freedom vs reported N | 30 | 0 | 0 | 0 |
| Duplicated statistics | 30 | 0 | 0 | 0 |

Total flags: 5 (errors 0, warnings 1, info 4).

Severity: an error is a reported vs recomputed p value on different sides of .05 (the conclusion about significance would change). A warning is a numeric inconsistency that does not change the decision, or a GRIM failure. Info items are worth a look but have common benign explanations.

## Flagged items

### 1. [WARNING] p value recomputation (statcheck style), page 18

Reported: `χ2(1, N = 89) = 5.00, p = 0.042`

Sentence: "The effect of mindset switching was significant, χ2(1, N = 89) = 5.00, p = 0.042."

Reported χ2(1, N = 89) = 5.00, p = 0.042. Recomputed p = 0.0253 (range 0.0253 to 0.0254 given rounding of the test statistic) does not match the reported p. The significance decision is unchanged.

Recomputed p = 0.025347 (interval [0.025274, 0.025421]); consistent if one-tailed: False; decision error: False.

### 2. [INFO] GRIM (means of integer data), page 18

Reported: `M = 5.68, SD = 1.36`

Sentence: "The want choice of the English/Chinese-language switching group (M = 6.06, SD = 1.07) was higher than that of the Chinese-language group (M = 5.68, SD = 1.36) and the English group (M = 5.64, SD = 1.25)."

GRIM: a mean of 5.68 with n = 89 (N taken from the nearest preceding N on the page) is not possible if each score is a whole number (for example a single Likert item or a count). The nearest possible means are 5.69, 5.67. This only matters if the measure is integer-valued; averaged multi-item scales or continuous measures make GRIM inapplicable.

### 3. [INFO] GRIM (means of integer data), page 18

Reported: `M = -0.50, SD = 2.41`

Sentence: "The SMW score of the language switching group (M = -2.06, SD = 2.54) is significantly lower than that of the non-switching group (M = -0.50, SD = 2.41, p = 0.005)."

GRIM: a mean of -0.50 with n = 89 (N taken from the nearest preceding N on the page) is not possible if each score is a whole number (for example a single Likert item or a count). The nearest possible means are -0.51, -0.49. This only matters if the measure is integer-valued; averaged multi-item scales or continuous measures make GRIM inapplicable.

### 4. [INFO] GRIM (means of integer data), page 18

Reported: `M = -0.32, SD = 2.34`

Sentence: "A Tukey HSD test indicates that the Chinese-language group (M = -0.32, SD = 2.34) and the English group (M = -0.68, SD = 2.51) had no significant difference (p = 0.852)."

GRIM: a mean of -0.32 with n = 89 (N taken from the nearest preceding N on the page) is not possible if each score is a whole number (for example a single Likert item or a count). The nearest possible means are -0.31, -0.33. This only matters if the measure is integer-valued; averaged multi-item scales or continuous measures make GRIM inapplicable.

### 5. [INFO] GRIM (means of integer data), page 18

Reported: `M = -0.68, SD = 2.51`

Sentence: "A Tukey HSD test indicates that the Chinese-language group (M = -0.32, SD = 2.34) and the English group (M = -0.68, SD = 2.51) had no significant difference (p = 0.852)."

GRIM: a mean of -0.68 with n = 89 (N taken from the nearest preceding N on the page) is not possible if each score is a whole number (for example a single Likert item or a count). The nearest possible means are -0.69, -0.67. This only matters if the measure is integer-valued; averaged multi-item scales or continuous measures make GRIM inapplicable.

## All extracted test statistics

| Page | Statistic | Reported p | Recomputed p | Status |
|---:|---|---|---|---|
| 7 | t(90) = 27.77 | p < 0.001 | 0.0 | ok |
| 7 | chi2(1, N = 91) = 4.44 | p = 0.035 | 0.035106 | ok |
| 8 | F(2, 88) = 4.21 | p = 0.018 | 0.017943 | ok |
| 8 | F(2, 88) = 3.82 | p = 0.026 | 0.025651 | ok |
| 8 | F(2, 88) = 2.05 | p = 0.135 | 0.134838 | ok |
| 8 | F(2, 88) = 4.53 | p = 0.013 | 0.013411 | ok |
| 9 | F(2, 88) = 0.66 | p = 0.519 | 0.519391 | ok |
| 9 | F(2, 88) = 0.14 | p = 0.869 | 0.869551 | ok |
| 11 | F(2, 136) = 4.98 | p = 0.008 | 0.00818 | ok |
| 11 | F(2, 136) = 8.32 | p < 0.001 | 0.00039 | ok |
| 11 | F(2, 136) = 3.54 | p = 0.032 | 0.031716 | ok |
| 12 | F(2, 136) = 9.45 | p < 0.001 | 0.000144 | ok |
| 14 | t(90) = 24.48 | p < 0.001 | 0.0 | ok |
| 14 | chi2(1, N = 107) = 7.25 | p = 0.007 | 0.00709 | ok |
| 14 | F(2, 104) = 4.41 | p = 0.015 | 0.01451 | ok |
| 15 | F(2, 104) = 4.43 | p = 0.014 | 0.014245 | ok |
| 15 | F(2, 104) = 1.28 | p = 0.282 | 0.28238 | ok |
| 15 | F(2, 104) = 3.55 | p = 0.032 | 0.032255 | ok |
| 16 | F(2, 104) = 1.42 | p = 0.246 | 0.246361 | ok |
| 16 | F(2, 104) = 0.27 | p = 0.761 | 0.763913 | ok |
| 16 | F(2, 104) = 0.57 | p = 0.568 | 0.567282 | ok |
| 16 | F(2, 104) = 2.08 | p = 0.131 | 0.130097 | ok |
| 17 | F(2, 86) = 5.08 | p = 0.008 | 0.008216 | ok |
| 18 | chi2(1, N = 89) = 5.0 | p = 0.042 | 0.025347 | flagged |
| 18 | F(2, 86) = 5.0 | p = 0.009 | 0.008826 | ok |
| 18 | F(2, 86) = 1.1 | p = 0.337 | 0.337508 | ok |
| 18 | F(2, 86) = 5.96 | p = 0.004 | 0.003767 | ok |
| 19 | F(2, 86) = 0.09 | p = 0.911 | 0.914017 | ok |
| 19 | F(2, 86) = 0.05 | p = 0.95 | 0.951257 | ok |
| 19 | F(2, 86) = 1.51 | p = 0.227 | 0.226708 | ok |

## Notes and limitations

This report lists places where a value reported in the paper differs from the value recomputed from other reported numbers. A difference is not evidence of misconduct. Common benign causes are rounding, typos, one-tailed tests, corrections for multiple comparisons, adjusted degrees of freedom, non-integer scales (which make GRIM and GRIMMER inapplicable) and PDF text-extraction errors. Each flag should be read in the paper before drawing any conclusion.

GRIM and GRIMMER assume every score is a whole number and that the N in the same sentence or parenthesis is the N behind that mean; both assumptions fail for averaged multi-item scales, continuous measures and subgroup means. The df vs N check only flags tests whose df imply more participants than the paper mentions anywhere. Duplicated statistics are usually legitimate repetition.
