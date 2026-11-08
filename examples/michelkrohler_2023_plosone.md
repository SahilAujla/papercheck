# papercheck report: michelkrohler_2023_plosone.pdf

Generated 2026-11-08 with papercheck 0.1.0. 34 pages, 86 test statistics with p values, 458 reported means (7 with a usable N for GRIM).

## Summary

| Check | Items examined | Errors | Warnings | Info |
|---|---:|---:|---:|---:|
| p value recomputation (statcheck style) | 86 | 0 | 5 | 0 |
| GRIM (means of integer data) | 7 | 0 | 1 | 3 |
| GRIMMER (SDs of integer data) | 7 | 0 | 0 | 0 |
| Degrees of freedom vs reported N | 86 | 0 | 0 | 0 |
| Duplicated statistics | 86 | 0 | 0 | 2 |
| Unverifiable statements (ps < .05, statistics without p, p without statistic) | 19 | 0 | 0 | 19 |
| 95% CI vs point estimate | 0 | 0 | 0 | 0 |
| Regression coefficient vs SE and p | 0 | 0 | 0 | 0 |

Total flags: 30 (errors 0, warnings 6, info 24).

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

### 8. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 10

Reported: `p > .05`

Sentence: "We conducted a Shapiro-Wilk Test for testing the assumption of normality (p > .05) and a Levene's Test for testing the homogeneity of variance (p > .05)."

'p > .05' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 9. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 10

Reported: `p > .05`

Sentence: "We conducted a Shapiro-Wilk Test for testing the assumption of normality (p > .05) and a Levene's Test for testing the homogeneity of variance (p > .05)."

'p > .05' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 10. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 10

Reported: `p < .05`

Sentence: "In case of violation of sphericity, we used Mauchly's Test (p < .05) and applied a Greenhouse- Geisser correction for ANOVAs."

'p < .05' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 11. [INFO] Duplicated statistics, page 11

Reported: `F(1,162) = 4.13, p = .04`

Sentence: "We found no significant difference between the conditions in our experimental variables except for perceived strain, F(1,162) = 4.13, p = .04, ηp2 = .02, indicating higher values for participant in the EC1 compared to participants in the EC2."

The statistic F(1, 162) = 4.13 with the same p value appears 2 times (pages 11, 14). Often legitimate (abstract and results, or a table and the text), but identical statistics for different analyses deserve a check.

### 12. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 11

Reported: `F(1,162) < 1`

Sentence: "Furthermore, time effects were obtained in all variables used except for energetic arousal, F(1,162) < 1."

'F(1,162) < 1' is reported without a p value in the same sentence, so it cannot be verified. The statistic implies a two-tailed p = 0.3188.

### 13. [INFO] GRIM (means of integer data), page 14

Reported: `26.20 (SD = 6.79)`

Sentence: "The mean age was 26.20 (SD = 6.79), and participants received course credits for participating."

GRIM: a mean of 26.20 with n = 12 (N taken from the nearest preceding N on the page) is not possible if each score is a whole number (for example a single Likert item or a count). The nearest possible means are 26.17, 26.25. This only matters if the measure is integer-valued; averaged multi-item scales or continuous measures make GRIM inapplicable.

### 14. [INFO] Duplicated statistics, page 14

Reported: `F(1,36) = 6.08, p = .02`

Sentence: "...62) = 19.45, p < .001.11 F(1,162) < 1 - Perceived strain F(1,162) = 4.13, p = .04.02 F(1,162) = 93.69, p < .001.37 F(1,162) = 2.54, p = .11.01 Exp. 1b State Rumination BSRI F(2,36) = 3.28, p = .05.15 F(1,36) = 6.08, p = .02.14 F(2,36) = 1.97, p = .15.10 General rumination rating F(2,36) = 15.24, p < .001.46 F(1,36) = 6.08, p = .02.14 F(2,36) = 3.82, p = .03.17 Mood Energetic Arousal F(2,36) < 1 -..."

The statistic F(1, 36) = 6.08 with the same p value appears 2 times (pages 14). Often legitimate (abstract and results, or a table and the text), but identical statistics for different analyses deserve a check.

### 15. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 15

Reported: `p = .21`

Sentence: "...ts F-statistic Exp. 1a* M (SD) M (SD) Errors of commission Mean RT Experimental condition 1 FC(1,156) < 1 FC(1,156) < 1 Errors of commission 37.01(20.62) 39.98 (24.40) FM(1,156) < 1 FM(1,156) = 1.58, p = .21, ηp2 = .01 Mean RT 419.15 (84.33) 417.66 (86.63) FI(1,162) = 2.42, p = .12, ηp2 = .01 FI (1,156) = 2.54, p = .11, ηp2 = .02 Experimental condition 2 Errors of commission 41.29 (19.85) 40.46 (2..."

'p = .21' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 16. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 15

Reported: `p = .12`

Sentence: "...ntal condition 1 FC(1,156) < 1 FC(1,156) < 1 Errors of commission 37.01(20.62) 39.98 (24.40) FM(1,156) < 1 FM(1,156) = 1.58, p = .21, ηp2 = .01 Mean RT 419.15 (84.33) 417.66 (86.63) FI(1,162) = 2.42, p = .12, ηp2 = .01 FI (1,156) = 2.54, p = .11, ηp2 = .02 Experimental condition 2 Errors of commission 41.29 (19.85) 40.46 (23.51) Mean RT 403.96 (79.27) 416.62 (93.00) Exp. 1b Experimental condition..."

'p = .12' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 17. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 15

Reported: `p = .11`

Sentence: "...6) < 1 Errors of commission 37.01(20.62) 39.98 (24.40) FM(1,156) < 1 FM(1,156) = 1.58, p = .21, ηp2 = .01 Mean RT 419.15 (84.33) 417.66 (86.63) FI(1,162) = 2.42, p = .12, ηp2 = .01 FI (1,156) = 2.54, p = .11, ηp2 = .02 Experimental condition 2 Errors of commission 41.29 (19.85) 40.46 (23.51) Mean RT 403.96 (79.27) 416.62 (93.00) Exp. 1b Experimental condition 1 FC(2,36) < 1 FC(2,36) < 1 Errors of..."

'p = .11' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 18. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 15

Reported: `p = .02`

Sentence: "...mmission 41.29 (19.85) 40.46 (23.51) Mean RT 403.96 (79.27) 416.62 (93.00) Exp. 1b Experimental condition 1 FC(2,36) < 1 FC(2,36) < 1 Errors of commission 38.40 (18.96) 40.10 (22.72) FT(1,36) = 5.70, p = .02, ηp2 = .14 FT(1,36) < 1 Mean RT 418.18 (83.89) 431.92 (88.18) FI(2,36) = 1.19, p = .31, ηp2 = .06 FI(2,36) = 2.54, p = .09, ηp2 = .12 Experimental condition 2 Errors of commission 37.55 (25.82..."

'p = .02' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 19. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 15

Reported: `p = .31`

Sentence: "...rimental condition 1 FC(2,36) < 1 FC(2,36) < 1 Errors of commission 38.40 (18.96) 40.10 (22.72) FT(1,36) = 5.70, p = .02, ηp2 = .14 FT(1,36) < 1 Mean RT 418.18 (83.89) 431.92 (88.18) FI(2,36) = 1.19, p = .31, ηp2 = .06 FI(2,36) = 2.54, p = .09, ηp2 = .12 Experimental condition 2 Errors of commission 37.55 (25.82) 41.78 (29.69) Mean RT 457.81 (83.82) 450.33 (78.86) Neutral control condition Errors..."

'p = .31' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 20. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 15

Reported: `p = .09`

Sentence: "...(2,36) < 1 Errors of commission 38.40 (18.96) 40.10 (22.72) FT(1,36) = 5.70, p = .02, ηp2 = .14 FT(1,36) < 1 Mean RT 418.18 (83.89) 431.92 (88.18) FI(2,36) = 1.19, p = .31, ηp2 = .06 FI(2,36) = 2.54, p = .09, ηp2 = .12 Experimental condition 2 Errors of commission 37.55 (25.82) 41.78 (29.69) Mean RT 457.81 (83.82) 450.33 (78.86) Neutral control condition Errors of commission 36.00 (18.93) 45.00 (2..."

'p = .09' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 21. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 15

Reported: `p = .15`

Sentence: "...l condition Errors of commission 36.00 (18.93) 45.00 (21.44) Mean RT 426.93 (129.35) 394.32 (97.62) Exp. 1c* Experimental condition 1 Errors of commission 47.68 (22.02) 48.21 (22.24) FC(2,50) = 1.93, p = .15, ηp2 = .07 FT(1,50) = 4.41, p = .04, ηp2 = .08 FI(2,50) < 1 FC(2,50) < 1 FT(1,50) = 2.86, p = .10, ηp2 = .05 FI(2,50) < 1 Mean RT 387.54 (64.44) 382.34 (67.93) Experimental condition 2 Errors..."

'p = .15' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 22. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 15

Reported: `p = .04`

Sentence: "...00 (18.93) 45.00 (21.44) Mean RT 426.93 (129.35) 394.32 (97.62) Exp. 1c* Experimental condition 1 Errors of commission 47.68 (22.02) 48.21 (22.24) FC(2,50) = 1.93, p = .15, ηp2 = .07 FT(1,50) = 4.41, p = .04, ηp2 = .08 FI(2,50) < 1 FC(2,50) < 1 FT(1,50) = 2.86, p = .10, ηp2 = .05 FI(2,50) < 1 Mean RT 387.54 (64.44) 382.34 (67.93) Experimental condition 2 Errors of commission 34.50 (17.30) 40.12 (1..."

'p = .04' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 23. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 15

Reported: `p = .10`

Sentence: "...) Exp. 1c* Experimental condition 1 Errors of commission 47.68 (22.02) 48.21 (22.24) FC(2,50) = 1.93, p = .15, ηp2 = .07 FT(1,50) = 4.41, p = .04, ηp2 = .08 FI(2,50) < 1 FC(2,50) < 1 FT(1,50) = 2.86, p = .10, ηp2 = .05 FI(2,50) < 1 Mean RT 387.54 (64.44) 382.34 (67.93) Experimental condition 2 Errors of commission 34.50 (17.30) 40.12 (17.52) Mean RT 411.36 (57.24) 402.46 (67.18) Neutral control co..."

'p = .10' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 24. [INFO] GRIM (means of integer data), page 21

Reported: `24.28 (SD = 5.70)`

Sentence: "The mean age was 24.28 (SD = 5.70)."

GRIM: a mean of 24.28 with n = 2 (N taken from the nearest preceding N on the page) is not possible if each score is a whole number (for example a single Likert item or a count). The nearest possible means are 24.50, 24.00. This only matters if the measure is integer-valued; averaged multi-item scales or continuous measures make GRIM inapplicable.

### 25. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 24

Reported: `F(1,201) < 1`

Sentence: "The effect for time was not significant, F(1,201) < 1."

'F(1,201) < 1' is reported without a p value in the same sentence, so it cannot be verified. The statistic implies a two-tailed p = 0.3185.

### 26. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 25

Reported: `F(1,201) < 1`

Sentence: "The effect for time was not significant, F(1,201) < 1."

'F(1,201) < 1' is reported without a p value in the same sentence, so it cannot be verified. The statistic implies a two-tailed p = 0.3185.

### 27. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 26

Reported: `p = .02`

Sentence: "Block 1 Block 2 Results F-statistic M (SD) M (SD) Errors of commission Mean RT Experimental condition 1 FC(3,187) = 3.30, p = .02, ηp2 = .05 FT(1,187) = 7.36, p < .01, ηp2 = .04 FI(3,187) = 2.04, p = .11, ηp2 = .03 FC(3,187) < 1 FT(1,187) = 6.26, p = .01, ηp2 = .03 FI(3,187) < 1 Errors of commission 51.48 (17.08) 58.96 (22.27) Mean RT 377.35 (71.88) 390.32 (94.19) Experimental condition 2 Errors o..."

'p = .02' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 28. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 26

Reported: `p < .01`

Sentence: "Block 1 Block 2 Results F-statistic M (SD) M (SD) Errors of commission Mean RT Experimental condition 1 FC(3,187) = 3.30, p = .02, ηp2 = .05 FT(1,187) = 7.36, p < .01, ηp2 = .04 FI(3,187) = 2.04, p = .11, ηp2 = .03 FC(3,187) < 1 FT(1,187) = 6.26, p = .01, ηp2 = .03 FI(3,187) < 1 Errors of commission 51.48 (17.08) 58.96 (22.27) Mean RT 377.35 (71.88) 390.32 (94.19) Experimental condition 2 Errors o..."

'p < .01' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 29. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 26

Reported: `p = .11`

Sentence: "Block 1 Block 2 Results F-statistic M (SD) M (SD) Errors of commission Mean RT Experimental condition 1 FC(3,187) = 3.30, p = .02, ηp2 = .05 FT(1,187) = 7.36, p < .01, ηp2 = .04 FI(3,187) = 2.04, p = .11, ηp2 = .03 FC(3,187) < 1 FT(1,187) = 6.26, p = .01, ηp2 = .03 FI(3,187) < 1 Errors of commission 51.48 (17.08) 58.96 (22.27) Mean RT 377.35 (71.88) 390.32 (94.19) Experimental condition 2 Errors o..."

'p = .11' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 30. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 26

Reported: `p = .01`

Sentence: "...D) Errors of commission Mean RT Experimental condition 1 FC(3,187) = 3.30, p = .02, ηp2 = .05 FT(1,187) = 7.36, p < .01, ηp2 = .04 FI(3,187) = 2.04, p = .11, ηp2 = .03 FC(3,187) < 1 FT(1,187) = 6.26, p = .01, ηp2 = .03 FI(3,187) < 1 Errors of commission 51.48 (17.08) 58.96 (22.27) Mean RT 377.35 (71.88) 390.32 (94.19) Experimental condition 2 Errors of commission 46.42 (21.29) 47.28 (22.32) Mean R..."

'p = .01' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

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
