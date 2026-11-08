# papercheck report: yan_2018_plosone.pdf

Generated 2026-11-08 with papercheck 0.1.0. 24 pages, 30 test statistics with p values, 59 reported means (11 with a usable N for GRIM).

## Summary

| Check | Items examined | Errors | Warnings | Info |
|---|---:|---:|---:|---:|
| p value recomputation (statcheck style) | 30 | 0 | 1 | 0 |
| GRIM (means of integer data) | 11 | 0 | 0 | 4 |
| GRIMMER (SDs of integer data) | 11 | 0 | 0 | 0 |
| Degrees of freedom vs reported N | 30 | 0 | 0 | 0 |
| Duplicated statistics | 30 | 0 | 0 | 0 |
| Unverifiable statements (ps < .05, statistics without p, p without statistic) | 37 | 0 | 0 | 37 |
| 95% CI vs point estimate | 0 | 0 | 0 | 0 |
| Regression coefficient vs SE and p | 0 | 0 | 0 | 0 |

Total flags: 42 (errors 0, warnings 1, info 41).

Severity: an error is a reported vs recomputed p value on different sides of .05 (the conclusion about significance would change). A warning is a numeric inconsistency that does not change the decision, or a GRIM failure. Info items are worth a look but have common benign explanations.

## Flagged items

### 1. [WARNING] p value recomputation (statcheck style), page 18

Reported: `χ2(1, N = 89) = 5.00, p = 0.042`

Sentence: "The effect of mindset switching was significant, χ2(1, N = 89) = 5.00, p = 0.042."

Reported χ2(1, N = 89) = 5.00, p = 0.042. Recomputed p = 0.0253 (range 0.0253 to 0.0254 given rounding of the test statistic) does not match the reported p. The significance decision is unchanged. For a 2 x 2 table, a continuity-corrected chi-square or Fisher's exact test gives a different p from the uncorrected statistic, which is a common benign explanation.

Recomputed p = 0.025347 (interval [0.025274, 0.025421]); consistent if one-tailed: False; decision error: False.

### 2. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 8

Reported: `p = 0.005`

Sentence: "The average effort and task difficulty for the mindset-switching group (M = 4.52, SD = 1.27) is significantly greater than that of the non-switching group (M = 3.77, SD = 1.23, p = 0.005)."

'p = 0.005' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 3. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 8

Reported: `p = 0.842`

Sentence: "Post hoc comparisons using the Tukey HSD test indicate that the individualist group (M = 3.86, SD = 1.21) and the collectivist group (M = 3.67, SD = 1.28) have no significant difference (p = 0.842)."

'p = 0.842' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 4. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 8

Reported: `p = 0.019`

Sentence: "The intention of the mindsetswitching group (M = 5.49, SD = 1.31) is significantly greater than that of the overall nonswitching group (M = 4.74, SD = 1.63, p = 0.019)."

'p = 0.019' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 5. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 8

Reported: `p = 0.355`

Sentence: "Tukey HSD comparisons indicate that the individualist group (M = 5.04, SD = 1.49) and the collectivist group (M = 4.46, SD = 1.73) have no significant difference (p = 0.355)."

'p = 0.355' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 6. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 8

Reported: `p = 0.014`

Sentence: "The SMW score of the mindset-switching group (M = -1.59, SD = 2.60) was significantly lower than that of the overall non-mindset switching group (M = -0.28, SD = 2.38, p = 0.014)."

'p = 0.014' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 7. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 8

Reported: `p = 0.233`

Sentence: "Tukey HSD comparisons showed that the individualist group (M = -0.87, SD = 2.33) and the collectivist group (M = 0.27, SD = 2.34) had no significant difference (p = 0.233)."

'p = 0.233' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 8. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 9

Reported: `p < .10`

Sentence: "...2 (Age) f2 -0.03 0.07 g2 0.00 0.11 g'2 0.01 0.12 C3 (Gender) f3 -0.13 0.29 g3 -2.10 0.52 g'3 -2.05 0.52 Constant i1 4.58 1.52 i2 -2.88 2.73 i3 1.29 2.84 R2 0.09# 0.24 0.27 F 2.17 6.67 6.14 #p < .10 p < .05 p < .01 https://doi.org/10.1371/journal.pone.0196269.t002 Mindset switching increases the appeal of wants over shoulds PLOS ONE | https://doi.org/10.1371/journal.pone.0196269 April..."

'p < .10' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 9. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 9

Reported: `p < .05`

Sentence: "...2 -0.03 0.07 g2 0.00 0.11 g'2 0.01 0.12 C3 (Gender) f3 -0.13 0.29 g3 -2.10 0.52 g'3 -2.05 0.52 Constant i1 4.58 1.52 i2 -2.88 2.73 i3 1.29 2.84 R2 0.09# 0.24 0.27 F 2.17 6.67 6.14 #p < .10 p < .05 p < .01 https://doi.org/10.1371/journal.pone.0196269.t002 Mindset switching increases the appeal of wants over shoulds PLOS ONE | https://doi.org/10.1371/journal.pone.0196269 April 30, 2018..."

'p < .05' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 10. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 9

Reported: `p < .01`

Sentence: "...07 g2 0.00 0.11 g'2 0.01 0.12 C3 (Gender) f3 -0.13 0.29 g3 -2.10 0.52 g'3 -2.05 0.52 Constant i1 4.58 1.52 i2 -2.88 2.73 i3 1.29 2.84 R2 0.09# 0.24 0.27 F 2.17 6.67 6.14 #p < .10 p < .05 p < .01 https://doi.org/10.1371/journal.pone.0196269.t002 Mindset switching increases the appeal of wants over shoulds PLOS ONE | https://doi.org/10.1371/journal.pone.0196269 April 30, 2018 9 / 24..."

'p < .01' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 11. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 11

Reported: `p = 0.002`

Sentence: "The average for the ego depletion items for the mindset-switching group (M = 5.22, SD = 1.33) was significantly higher than that of the two non-switching conditions (M = 4.50, SD = 1.34, p = 0.002)."

'p = 0.002' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 12. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 11

Reported: `p = 0.874`

Sentence: "Post hoc comparisons using the Tukey HSD test indicated that the concrete mindset group (M = 4.58, SD = 1.58) and the abstract mindset group (M = 4.43, SD = 1.08) had no significant difference in scores (p = 0.874)."

'p = 0.874' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 13. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 11

Reported: `p = 0.001`

Sentence: "The should intention of the mindset-switching group (M = 2.53, SD = 1.33) was significantly lower than that of the overall non-switching group (M = 3.48, SD = 1.74, p = 0.001)."

'p = 0.001' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 14. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 11

Reported: `p = 0.109`

Sentence: "Post hoc comparisons using Tukey HSD indicated that the abstract mindset group (M = 3.14, SD = 1.35) and the concrete mindset group (M = 3.84, SD = 2.03) had no significant difference (p = 0.109)."

'p = 0.109' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 15. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 12

Reported: `p = 0.011`

Sentence: "group (M = 4.31, SD = 1.74, p = 0.011)."

'p = 0.011' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 16. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 12

Reported: `p = 0.778`

Sentence: "The Tukey HSD comparison showed that the abstract mindset group (M = 4.20, SD = 1.38) and the concrete mindset group (M = 4.42, SD = 1.30) had no significant difference (p = 0.778)."

'p = 0.778' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 17. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 12

Reported: `p < 0.001`

Sentence: "The SMW score of the mindset-switching group (M = -2.45, SD = 1.84) was significantly lower than that of the overall non-switching group (M = -0.82, SD = 2.45, p < 0.001)."

'p < 0.001' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 18. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 12

Reported: `p = 0.596`

Sentence: "A Tukey HSD comparison showed that the abstract mindset group (M = -1.06, SD = 1.91) and the concrete mindset group (M = -0.59, SD = 2.91) had no significant difference (p = 0.596)."

'p = 0.596' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 19. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 12

Reported: `p < .05`

Sentence: "...0.48 C2 (Age) f2 -0.04 0.05 g2 0.00 0.09 g'2 -0.01 0.09 C3 (Gender) f3 0.13 0.23 g3 0.07 0.38 g'3 0.07 0.37 Constant i1 5.19 1.12 i2 -1.15 1.87 i3 1.25 1.94 R2 0.07 0.12 0.19 F 2.58 4.66 6.24 p < .05 p < .01 https://doi.org/10.1371/journal.pone.0196269.t003 Mindset switching increases the appeal of wants over shoulds PLOS ONE | https://doi.org/10.1371/journal.pone.0196269 April 30, 2018..."

'p < .05' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 20. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 12

Reported: `p < .01`

Sentence: "...ge) f2 -0.04 0.05 g2 0.00 0.09 g'2 -0.01 0.09 C3 (Gender) f3 0.13 0.23 g3 0.07 0.38 g'3 0.07 0.37 Constant i1 5.19 1.12 i2 -1.15 1.87 i3 1.25 1.94 R2 0.07 0.12 0.19 F 2.58 4.66 6.24 p < .05 p < .01 https://doi.org/10.1371/journal.pone.0196269.t003 Mindset switching increases the appeal of wants over shoulds PLOS ONE | https://doi.org/10.1371/journal.pone.0196269 April 30, 2018 12 / 24..."

'p < .01' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 21. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 15

Reported: `p = 0.006`

Sentence: "of ego depletion was significantly higher in the language-switching group (M = 5.53, SD = 1.11) than that of the two non-switching groups (M = 4.70, SD = 1.59, p = 0.006)."

'p = 0.006' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 22. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 15

Reported: `p = 0.614`

Sentence: "The Tukey HSD test indicated that the Chinese-writing group (M = 4.54, SD = 1.77) and the English-writing group (M = 4.87, SD = 1.39) had no significant difference (p = 0.614)."

'p = 0.614' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 23. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 15

Reported: `p = 0.012`

Sentence: "The intention of the language-switching group (M = 6.00, SD = 0.82) was significantly higher than that of the two non-switching groups (M = 5.37, SD = 1.37, p = 0.012)."

'p = 0.012' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 24. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 15

Reported: `p = 0.288`

Sentence: "Multiple comparisons using the Tukey HSD test showed that the Chinese-writing group (M = 5.58, SD = 1.23) and the English-writing group (M = 5.15, SD = 1.50) had no significant difference (p = 0.288)."

'p = 0.288' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 25. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 15

Reported: `p = 0.017`

Sentence: "The SMW score of the switching group (M = -2.57, SD = 1.83) was significantly lower than that of the overall non-switching group (M = -1.43, SD = 2.52, p = 0.017)."

'p = 0.017' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 26. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 15

Reported: `p = 0.519`

Sentence: "The Tukey HSD test indicated that the Chinese-writing group (M = -1.72, SD = 2.36) and the English-writing group (M = -1.12, SD = 2.68) had no significant difference (p = 0.519)."

'p = 0.519' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 27. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 15

Reported: `p < .10`

Sentence: "...3 0.62# 0.36 g3 -0.72 0.56 g'3 -0.17 0.47 C4 (Need for Cognition) f4 -0.02 0.22 g4 0.79 0.35 g'4 0.77 0.28 Constant i1 2.69 1.63 i2 -1.77 2.56 i3 0.66 2.12 R2 0.11 0.13 0.42 F 2.47 2.99 11.96 #p < .10 p < .05 p < .01 https://doi.org/10.1371/journal.pone.0196269.t004 Mindset switching increases the appeal of wants over shoulds PLOS ONE | https://doi.org/10.1371/journal.pone.0196269 April..."

'p < .10' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 28. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 15

Reported: `p < .05`

Sentence: "....36 g3 -0.72 0.56 g'3 -0.17 0.47 C4 (Need for Cognition) f4 -0.02 0.22 g4 0.79 0.35 g'4 0.77 0.28 Constant i1 2.69 1.63 i2 -1.77 2.56 i3 0.66 2.12 R2 0.11 0.13 0.42 F 2.47 2.99 11.96 #p < .10 p < .05 p < .01 https://doi.org/10.1371/journal.pone.0196269.t004 Mindset switching increases the appeal of wants over shoulds PLOS ONE | https://doi.org/10.1371/journal.pone.0196269 April 30, 2018..."

'p < .05' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 29. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 15

Reported: `p < .01`

Sentence: "...72 0.56 g'3 -0.17 0.47 C4 (Need for Cognition) f4 -0.02 0.22 g4 0.79 0.35 g'4 0.77 0.28 Constant i1 2.69 1.63 i2 -1.77 2.56 i3 0.66 2.12 R2 0.11 0.13 0.42 F 2.47 2.99 11.96 #p < .10 p < .05 p < .01 https://doi.org/10.1371/journal.pone.0196269.t004 Mindset switching increases the appeal of wants over shoulds PLOS ONE | https://doi.org/10.1371/journal.pone.0196269 April 30, 2018 15 / 24..."

'p < .01' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 30. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 17

Reported: `p = 0.003`

Sentence: "The average for the switching group (M = 5.04, SD = 1.47) was significantly higher than that of the overall nonswitching group (M = 4.05, SD = 1.49, p = 0.003)."

'p = 0.003' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 31. [INFO] GRIM (means of integer data), page 18

Reported: `M = 5.68, SD = 1.36`

Sentence: "The want choice of the English/Chinese-language switching group (M = 6.06, SD = 1.07) was higher than that of the Chinese-language group (M = 5.68, SD = 1.36) and the English group (M = 5.64, SD = 1.25)."

GRIM: a mean of 5.68 with n = 89 (N taken from the nearest preceding N on the page) is not possible if each score is a whole number (for example a single Likert item or a count). The nearest possible means are 5.69, 5.67. This only matters if the measure is integer-valued; averaged multi-item scales or continuous measures make GRIM inapplicable.

### 32. [INFO] GRIM (means of integer data), page 18

Reported: `M = -0.50, SD = 2.41`

Sentence: "The SMW score of the language switching group (M = -2.06, SD = 2.54) is significantly lower than that of the non-switching group (M = -0.50, SD = 2.41, p = 0.005)."

GRIM: a mean of -0.50 with n = 89 (N taken from the nearest preceding N on the page) is not possible if each score is a whole number (for example a single Likert item or a count). The nearest possible means are -0.51, -0.49. This only matters if the measure is integer-valued; averaged multi-item scales or continuous measures make GRIM inapplicable.

### 33. [INFO] GRIM (means of integer data), page 18

Reported: `M = -0.32, SD = 2.34`

Sentence: "A Tukey HSD test indicates that the Chinese-language group (M = -0.32, SD = 2.34) and the English group (M = -0.68, SD = 2.51) had no significant difference (p = 0.852)."

GRIM: a mean of -0.32 with n = 89 (N taken from the nearest preceding N on the page) is not possible if each score is a whole number (for example a single Likert item or a count). The nearest possible means are -0.31, -0.33. This only matters if the measure is integer-valued; averaged multi-item scales or continuous measures make GRIM inapplicable.

### 34. [INFO] GRIM (means of integer data), page 18

Reported: `M = -0.68, SD = 2.51`

Sentence: "A Tukey HSD test indicates that the Chinese-language group (M = -0.32, SD = 2.34) and the English group (M = -0.68, SD = 2.51) had no significant difference (p = 0.852)."

GRIM: a mean of -0.68 with n = 89 (N taken from the nearest preceding N on the page) is not possible if each score is a whole number (for example a single Likert item or a count). The nearest possible means are -0.69, -0.67. This only matters if the measure is integer-valued; averaged multi-item scales or continuous measures make GRIM inapplicable.

### 35. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 18

Reported: `p = 0.640`

Sentence: "test indicated that the Chinese group (M = 3.87, SD = 1.53) and English group (M = 4.23, SD = 1.45) had no significant difference (p = 0.640)."

'p = 0.640' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 36. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 18

Reported: `p = 0.003`

Sentence: "The intention of the switching group (M = 4.00, SD = 1.92) was significantly lower than that of the non-switching groups (M = 5.16, SD = 1.62, p = 0.003)."

'p = 0.003' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 37. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 18

Reported: `p = 0.675`

Sentence: "The Tukey HSD test indicates that the Chinese group (M = 5.36, SD = 1.57) and the English group (M = 4.96, SD = 1.67) had no significant difference on their choice of M&Ms, the want behavior (p = 0.675)."

'p = 0.675' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 38. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 18

Reported: `p = 0.005`

Sentence: "The SMW score of the language switching group (M = -2.06, SD = 2.54) is significantly lower than that of the non-switching group (M = -0.50, SD = 2.41, p = 0.005)."

'p = 0.005' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 39. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 18

Reported: `p = 0.852`

Sentence: "A Tukey HSD test indicates that the Chinese-language group (M = -0.32, SD = 2.34) and the English group (M = -0.68, SD = 2.51) had no significant difference (p = 0.852)."

'p = 0.852' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 40. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 18

Reported: `p < .10`

Sentence: "...2 C2 (Age) f2 0.02 0.09 g2 0.23 0.15 g'2 0.24 0.15 C3 (Gender) f3 0.79 0.50 g3 -1.39# 0.83 g'3 -0.90 0.79 Constant i1 2.31 2.16 i2 -2.80 3.57 i3 -1.39 3.37 R2 0.13 0.14  0.25 F 3.21 3.31 5.66 #p < .10 p < .05 p < .01 https://doi.org/10.1371/journal.pone.0196269.t005 Mindset switching increases the appeal of wants over shoulds PLOS ONE | https://doi.org/10.1371/journal.pone.0196269 April..."

'p < .10' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 41. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 18

Reported: `p < .05`

Sentence: "...) f2 0.02 0.09 g2 0.23 0.15 g'2 0.24 0.15 C3 (Gender) f3 0.79 0.50 g3 -1.39# 0.83 g'3 -0.90 0.79 Constant i1 2.31 2.16 i2 -2.80 3.57 i3 -1.39 3.37 R2 0.13 0.14  0.25 F 3.21 3.31 5.66 #p < .10 p < .05 p < .01 https://doi.org/10.1371/journal.pone.0196269.t005 Mindset switching increases the appeal of wants over shoulds PLOS ONE | https://doi.org/10.1371/journal.pone.0196269 April 30, 2018..."

'p < .05' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 42. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 18

Reported: `p < .01`

Sentence: "...0.09 g2 0.23 0.15 g'2 0.24 0.15 C3 (Gender) f3 0.79 0.50 g3 -1.39# 0.83 g'3 -0.90 0.79 Constant i1 2.31 2.16 i2 -2.80 3.57 i3 -1.39 3.37 R2 0.13 0.14  0.25 F 3.21 3.31 5.66 #p < .10 p < .05 p < .01 https://doi.org/10.1371/journal.pone.0196269.t005 Mindset switching increases the appeal of wants over shoulds PLOS ONE | https://doi.org/10.1371/journal.pone.0196269 April 30, 2018 18 / 24..."

'p < .01' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

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
