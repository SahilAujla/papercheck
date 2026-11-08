# papercheck report: michelkrohler_2023_plosone.pdf

Generated 2026-11-08 with papercheck 0.1.0. 34 pages, 86 test statistics with p values, 191 reported means (7 with a usable N for GRIM).

## Summary

| Check | Items examined | Errors | Warnings | Info |
|---|---:|---:|---:|---:|
| p value recomputation (statcheck style) | 86 | 0 | 5 | 0 |
| GRIM (means of integer data) | 7 | 0 | 1 | 3 |
| GRIMMER (SDs of integer data) | 7 | 0 | 0 | 0 |
| Degrees of freedom vs reported N | 86 | 0 | 0 | 0 |
| Duplicated statistics | 86 | 0 | 0 | 2 |

Total flags: 11 (errors 0, warnings 6, info 5).

Severity: an error is a reported vs recomputed p value on different sides of .05 (the conclusion about significance would change). A warning is a numeric inconsistency that does not change the decision, or a GRIM failure. Info items are worth a look but have common benign explanations.

## Flagged items

### 1. [WARNING] GRIM (means of integer data), page 6

Reported: `9.42 (3.02)`

Sentence: "...6) n = 20 (f = 14, m = 6) Age 24.35 (7.52) 25.37 (4.47) 24.60 (3.47) PTQ .94 25.40 (10.96) [20.27, 30.53] 26.31(11.61) [20.72, 31.91] 26.10 (10.59) [21.14, 31.05] RSQ-B .77 9.70 (2.99) [8.30, 11.10] 9.42 (3.02) [7.96, 10.88] 9.60 (2.64) [8.36, 10.83] RSQ-R .67 10.40 (3.22) [8.89, 11.91] 10.00 (2.31) [8.89, 11.11] 9.55 (3.00) [8.15, 10.95] GSE .83 29.10 (4.13) [27.17, 31.03] 28.47 (3.73) [26.67, 3..."

GRIM: a mean of 9.42 with n = 20 (N taken from the same sentence) is not possible if each score is a whole number (for example a single Likert item or a count). The nearest possible means are 9.40, 9.45. This only matters if the measure is integer-valued; averaged multi-item scales or continuous measures make GRIM inapplicable.

### 2. [WARNING] p value recomputation (statcheck style), page 14

Reported: `F(1,162) = 2.37, p = .12`

Sentence: "...62) = 83.04, p < .001.34 F(1,162) = 4.54, p = .03.03 Mood Energetic Arousal F(1,162) < 1 - F(1,162) < 1 - F(1,162) = 5.49, p = .02.03 Valence F(1,162) = 2.77, p = .10.02 F(1,162) = 29.87, p < .001.16 F(1,162) = 2.37, p = .12.01 Calmness F(1,162) < 1 F(1,162) = 19.45, p < .001.11 F(1,162) < 1 - Perceived strain F(1,162) = 4.13, p = .04.02 F(1,162) = 93.69, p < .001.37 F(1,162) = 2.54, p = .11.01 Ex..."

Reported F(1,162) = 2.37, p = .12. Recomputed p = 0.1256 (range 0.1252 to 0.1260 given rounding of the test statistic) does not match the reported p. The significance decision is unchanged.

Recomputed p = 0.125638 (interval [0.125243, 0.126035]); consistent if one-tailed: False; decision error: False.

### 3. [WARNING] p value recomputation (statcheck style), page 14

Reported: `F(2,56) = 3.55, p = .03`

Sentence: "....001.52 F(1,36) = 13.69, p < .001.27 F(2,36) = 5.19, p = .01.22 Exp. 1c State Rumination BSRI F(2,56) = 1.82, p = .17.06 F(1,56) = 6.66, p = .01.11 F(2,56) = 14.94, p < .001.35 Ruminative self-focus F(2,56) = 3.55, p = .03.11 F(1,56) = 20.83, p < .001.27 F(2,56) = 14.04, p < .001.33 Mood Energetic Arousal F(2,56) < 1 - F(2,56) < 1 - F(2,56) = 1.92, p = .15.06 Valence F(2,56) = 1.60, p = .21.05 F(..."

Reported F(2,56) = 3.55, p = .03. Recomputed p = 0.0354 (range 0.0352 to 0.0355 given rounding of the test statistic) does not match the reported p. The significance decision is unchanged.

Recomputed p = 0.035354 (interval [0.035198, 0.035512]); consistent if one-tailed: False; decision error: False.

### 4. [WARNING] p value recomputation (statcheck style), page 14

Reported: `F(2,56) = 1.92, p = .15`

Sentence: "..., p = .01.11 F(2,56) = 14.94, p < .001.35 Ruminative self-focus F(2,56) = 3.55, p = .03.11 F(1,56) = 20.83, p < .001.27 F(2,56) = 14.04, p < .001.33 Mood Energetic Arousal F(2,56) < 1 - F(2,56) < 1 - F(2,56) = 1.92, p = .15.06 Valence F(2,56) = 1.60, p = .21.05 F(2,56) < 1 - F(2,56) = 1.46, p = .24.05 Calmness F(2,56) < 1 - F(2,56) < 1 - F(2,56) < 1 - Perceived strain F(2,56) = 2.99, p = .06.09 F(..."

Reported F(2,56) = 1.92, p = .15. Recomputed p = 0.1561 (range 0.1554 to 0.1569 given rounding of the test statistic) does not match the reported p. The significance decision is unchanged.

Recomputed p = 0.156135 (interval [0.155406, 0.156867]); consistent if one-tailed: False; decision error: False.

### 5. [WARNING] p value recomputation (statcheck style), page 15

Reported: `F(2,36) = 0.02, p = .97`

Sentence: "Moreover, participants in the three conditions did not significantly differ in their level of trait rumination, F(2,36) = 0.02, p = .97, ηp2 < .01."

Reported F(2,36) = 0.02, p = .97. Recomputed p = 0.9802 (range 0.9753 to 0.9851 given rounding of the test statistic) does not match the reported p. The significance decision is unchanged.

Recomputed p = 0.98021 (interval [0.975327, 0.985118]); consistent if one-tailed: False; decision error: False.

### 6. [WARNING] p value recomputation (statcheck style), page 25

Reported: `F(1,201) = 2.70, p = .11`

Sentence: "Finally, results of the 4 x 2 ANOVA for calmness indicated a significant effect for condition, F (3,201) = 3.04, p = .03, ηp2 = .04, and for the time x condition interaction, F(3,201) = 6.77, p < .001, ηp2 = .09, but not for time, F(1,201) = 2.70, p = .11, ηp2 = .01."

Reported F(1,201) = 2.70, p = .11. Recomputed p = 0.1019 (range 0.1016 to 0.1022 given rounding of the test statistic) does not match the reported p. The significance decision is unchanged.

Recomputed p = 0.101912 (interval [0.101597, 0.102227]); consistent if one-tailed: False; decision error: False.

### 7. [INFO] GRIM (means of integer data), page 5

Reported: `28.68 (SD = 13.11)`

Sentence: "The mean age was 28.68 (SD = 13.11)."

GRIM: a mean of 28.68 with n = 61 (N taken from the nearest preceding N on the page) is not possible if each score is a whole number (for example a single Likert item or a count). The nearest possible means are 28.67, 28.69. This only matters if the measure is integer-valued; averaged multi-item scales or continuous measures make GRIM inapplicable.

### 8. [INFO] Duplicated statistics, page 11

Reported: `F(1,162) = 4.13, p = .04`

Sentence: "We found no significant difference between the conditions in our experimental variables except for perceived strain, F(1,162) = 4.13, p = .04, ηp2 = .02, indicating higher values for participant in the EC1 compared to participants in the EC2."

The statistic F(1, 162) = 4.13 with the same p value appears 2 times (pages 11, 14). Often legitimate (abstract and results, or a table and the text), but identical statistics for different analyses deserve a check.

### 9. [INFO] GRIM (means of integer data), page 14

Reported: `26.20 (SD = 6.79)`

Sentence: "The mean age was 26.20 (SD = 6.79), and participants received course credits for participating."

GRIM: a mean of 26.20 with n = 12 (N taken from the nearest preceding N on the page) is not possible if each score is a whole number (for example a single Likert item or a count). The nearest possible means are 26.17, 26.25. This only matters if the measure is integer-valued; averaged multi-item scales or continuous measures make GRIM inapplicable.

### 10. [INFO] Duplicated statistics, page 14

Reported: `F(1,36) = 6.08, p = .02`

Sentence: "...62) = 19.45, p < .001.11 F(1,162) < 1 - Perceived strain F(1,162) = 4.13, p = .04.02 F(1,162) = 93.69, p < .001.37 F(1,162) = 2.54, p = .11.01 Exp. 1b State Rumination BSRI F(2,36) = 3.28, p = .05.15 F(1,36) = 6.08, p = .02.14 F(2,36) = 1.97, p = .15.10 General rumination rating F(2,36) = 15.24, p < .001.46 F(1,36) = 6.08, p = .02.14 F(2,36) = 3.82, p = .03.17 Mood Energetic Arousal F(2,36) < 1 -..."

The statistic F(1, 36) = 6.08 with the same p value appears 2 times (pages 14). Often legitimate (abstract and results, or a table and the text), but identical statistics for different analyses deserve a check.

### 11. [INFO] GRIM (means of integer data), page 21

Reported: `24.28 (SD = 5.70)`

Sentence: "The mean age was 24.28 (SD = 5.70)."

GRIM: a mean of 24.28 with n = 2 (N taken from the nearest preceding N on the page) is not possible if each score is a whole number (for example a single Likert item or a count). The nearest possible means are 24.50, 24.00. This only matters if the measure is integer-valued; averaged multi-item scales or continuous measures make GRIM inapplicable.

## All extracted test statistics

| Page | Statistic | Reported p | Recomputed p | Status |
|---:|---|---|---|---|
| 5 | t(161.57) = -0.54 | p = 0.59 | 0.589941 | ok |
| 11 | F(1, 162) = 4.13 | p = 0.04 | 0.043763 | ok |
| 12 | t(35.34) = -0.29 | p = 0.77 | 0.773511 | ok |
| 12 | t(36.86) = -1.72 | p = 0.09 | 0.09382 | ok |
| 14 | F(1, 162) = 33.99 | p < 0.001 | 0.0 | ok |
| 14 | F(1, 162) = 1.63 | p = 0.2 | 0.20353 | ok |
| 14 | F(1, 162) = 3.37 | p = 0.07 | 0.068227 | ok |
| 14 | F(1, 162) = 83.04 | p < 0.001 | 0.0 | ok |
| 14 | F(1, 162) = 4.54 | p = 0.03 | 0.034621 | ok |
| 14 | F(1, 162) = 5.49 | p = 0.02 | 0.02034 | ok |
| 14 | F(1, 162) = 2.77 | p = 0.1 | 0.097979 | ok |
| 14 | F(1, 162) = 29.87 | p < 0.001 | 0.0 | ok |
| 14 | F(1, 162) = 2.37 | p = 0.12 | 0.125638 | flagged |
| 14 | F(1, 162) = 19.45 | p < 0.001 | 1.9e-05 | ok |
| 14 | F(1, 162) = 4.13 | p = 0.04 | 0.043763 | ok |
| 14 | F(1, 162) = 93.69 | p < 0.001 | 0.0 | ok |
| 14 | F(1, 162) = 2.54 | p = 0.11 | 0.112944 | ok |
| 14 | F(2, 36) = 3.28 | p = 0.05 | 0.049138 | ok |
| 14 | F(1, 36) = 6.08 | p = 0.02 | 0.018571 | ok |
| 14 | F(2, 36) = 1.97 | p = 0.15 | 0.154206 | ok |
| 14 | F(2, 36) = 15.24 | p < 0.001 | 1.6e-05 | ok |
| 14 | F(1, 36) = 6.08 | p = 0.02 | 0.018571 | ok |
| 14 | F(2, 36) = 3.82 | p = 0.03 | 0.031298 | ok |
| 14 | F(2, 36) = 5.88 | p < 0.01 | 0.00617 | ok |
| 14 | F(1, 36) = 2.94 | p = 0.09 | 0.095009 | ok |
| 14 | F(2, 36) = 14.77 | p < 0.001 | 2.1e-05 | ok |
| 14 | F(2, 36) = 3.26 | p = 0.05 | 0.049977 | ok |
| 14 | F(1, 36) = 1.38 | p = 0.25 | 0.247813 | ok |
| 14 | F(2, 36) = 2.31 | p = 0.11 | 0.113796 | ok |
| 14 | F(2, 36) = 19.38 | p < 0.001 | 2e-06 | ok |
| 14 | F(1, 36) = 13.69 | p < 0.001 | 0.000716 | ok |
| 14 | F(2, 36) = 5.19 | p = 0.01 | 0.010459 | ok |
| 14 | F(2, 56) = 1.82 | p = 0.17 | 0.171479 | ok |
| 14 | F(1, 56) = 6.66 | p = 0.01 | 0.012508 | ok |
| 14 | F(2, 56) = 14.94 | p < 0.001 | 6e-06 | ok |
| 14 | F(2, 56) = 3.55 | p = 0.03 | 0.035354 | flagged |
| 14 | F(1, 56) = 20.83 | p < 0.001 | 2.8e-05 | ok |
| 14 | F(2, 56) = 14.04 | p < 0.001 | 1.1e-05 | ok |
| 14 | F(2, 56) = 1.92 | p = 0.15 | 0.156135 | flagged |
| 14 | F(2, 56) = 1.6 | p = 0.21 | 0.210988 | ok |
| 14 | F(2, 56) = 1.46 | p = 0.24 | 0.24094 | ok |
| 14 | F(2, 56) = 2.99 | p = 0.06 | 0.058374 | ok |
| 14 | F(1, 56) = 36.66 | p < 0.001 | 0.0 | ok |
| 14 | F(2, 56) = 18.28 | p < 0.001 | 1e-06 | ok |
| 15 | F(2, 36) = 0.02 | p = 0.97 | 0.98021 | flagged |
| 16 | F(1, 36) = 5.7 | p = 0.02 | 0.022338 | ok |
| 18 | F(2, 56) = 0.04 | p = 0.96 | 0.960817 | ok |
| 18 | F(2, 56) = 1.49 | p = 0.23 | 0.23417 | ok |
| 19 | F(1, 57) = 4.41 | p = 0.04 | 0.040166 | ok |
| 21 | F(1, 203) = 0.07 | p = 0.79 | 0.791605 | ok |
| 22 | F(3, 201) = 1.61 | p = 0.19 | 0.188258 | ok |
| 22 | F(3, 201) = 4.14 | p = 0.01 | 0.00711 | ok |
| 22 | F(3, 201) = 3.45 | p = 0.02 | 0.017595 | ok |
| 23 | F(3, 201) = 3.86 | p = 0.01 | 0.010273 | ok |
| 23 | F(1, 201) = 11.22 | p = 0.001 | 0.000966 | ok |
| 23 | F(3, 201) = 8.94 | p < 0.001 | 1.4e-05 | ok |
| 23 | F(3, 201) = 4.75 | p < 0.01 | 0.003188 | ok |
| 23 | F(2, 149) = 162.9 | p < 0.001 | 0.0 | ok |
| 23 | F(2, 149) = 4.4 | p = 0.01 | 0.013913 | ok |
| 23 | F(2, 149) = 5.23 | p < 0.01 | 0.00638 | ok |
| 23 | F(2, 149) = 3.34 | p = 0.04 | 0.038109 | ok |
| 23 | F(2, 149) = 2.37 | p = 0.1 | 0.096996 | ok |
| 23 | F(2, 149) = 23.26 | p < 0.001 | 0.0 | ok |
| 23 | F(2, 149) = 1.47 | p = 0.23 | 0.23324 | ok |
| 23 | F(2, 149) = 2.98 | p = 0.05 | 0.053829 | ok |
| 24 | F(1, 201) = 1.35 | p = 0.25 | 0.246656 | ok |
| 24 | F(3, 201) = 16.54 | p < 0.001 | 0.0 | ok |
| 24 | F(1, 201) = 7.46 | p < 0.01 | 0.00687 | ok |
| 24 | F(3, 201) = 29.96 | p < 0.001 | 0.0 | ok |
| 24 | F(3, 201) = 9.88 | p < 0.001 | 4e-06 | ok |
| 24 | F(3, 201) = 13.82 | p < 0.001 | 0.0 | ok |
| 24 | F(3, 201) = 4.02 | p < 0.01 | 0.008325 | ok |
| 24 | F(3, 201) = 4.61 | p < 0.01 | 0.003832 | ok |
| 24 | F(1, 201) = 3.77 | p = 0.05 | 0.053577 | ok |
| 25 | F(3, 201) = 3.09 | p = 0.03 | 0.028182 | ok |
| 25 | F(1, 201) = 20.69 | p < 0.001 | 9e-06 | ok |
| 25 | F(3, 201) = 11.36 | p < 0.001 | 1e-06 | ok |
| 25 | F(3, 201) = 3.04 | p = 0.03 | 0.030083 | ok |
| 25 | F(3, 201) = 6.77 | p < 0.001 | 0.000226 | ok |
| 25 | F(1, 201) = 2.7 | p = 0.11 | 0.101912 | flagged |
| 25 | F(3, 201) = 11.68 | p < 0.001 | 0.0 | ok |
| 25 | F(3, 201) = 18.14 | p < 0.001 | 0.0 | ok |
| 25 | F(3, 187) = 3.3 | p = 0.02 | 0.021566 | ok |
| 25 | F(1, 187) = 7.36 | p < 0.01 | 0.007292 | ok |
| 25 | F(3, 187) = 2.04 | p = 0.11 | 0.109776 | ok |
| 25 | F(1, 187) = 6.26 | p = 0.01 | 0.013207 | ok |

## Notes and limitations

This report lists places where a value reported in the paper differs from the value recomputed from other reported numbers. A difference is not evidence of misconduct. Common benign causes are rounding, typos, one-tailed tests, corrections for multiple comparisons, adjusted degrees of freedom, non-integer scales (which make GRIM and GRIMMER inapplicable) and PDF text-extraction errors. Each flag should be read in the paper before drawing any conclusion.

GRIM and GRIMMER assume every score is a whole number and that the N in the same sentence or parenthesis is the N behind that mean; both assumptions fail for averaged multi-item scales, continuous measures and subgroup means. The df vs N check only flags tests whose df imply more participants than the paper mentions anywhere. Duplicated statistics are usually legitimate repetition.
