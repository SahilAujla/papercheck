# papercheck report: takayama_2023_plosone.pdf

Generated 2026-11-08 with papercheck 0.1.0. 22 pages, 18 test statistics with p values, 52 reported means (0 with a usable N for GRIM).

## Summary

| Check | Items examined | Errors | Warnings | Info |
|---|---:|---:|---:|---:|
| p value recomputation (statcheck style) | 18 | 0 | 0 | 0 |
| GRIM (means of integer data) | 0 | 0 | 0 | 0 |
| GRIMMER (SDs of integer data) | 0 | 0 | 0 | 0 |
| Degrees of freedom vs reported N | 18 | 0 | 9 | 4 |
| Duplicated statistics | 18 | 0 | 0 | 0 |
| Unverifiable statements (ps < .05, statistics without p, p without statistic) | 23 | 0 | 0 | 23 |
| 95% CI vs point estimate | 0 | 0 | 0 | 0 |
| Regression coefficient vs SE and p | 0 | 0 | 0 | 0 |

Total flags: 36 (errors 0, warnings 9, info 27).

Severity: an error is a reported vs recomputed p value on different sides of .05 (the conclusion about significance would change). A warning is a numeric inconsistency that does not change the decision, or a GRIM failure. Info items are worth a look but have common benign explanations.

## Flagged items

### 1. [WARNING] Degrees of freedom vs reported N, page 6

Reported: `t (86) = 5.99, p < .001`

Sentence: "The one-sample t-test on arousal and valence in the seated upright posture showed significantly smaller values for arousal (M = -3.15, SD = 4.91, t (86) = 5.99, p < .001, d = .64) and significantly larger values for valence (M = 4.69, SD = 3.56, t (86) = 12.23, p < .001, d = 1.31)."

The degrees of freedom in t(86) = 5.99 imply at least 87 participants under the usual design, but the largest sample size mentioned in the paper is 29. Reported vs implied N differ; could be a repeated-measures design, trials as the unit of analysis, or a typo in the df.

### 2. [WARNING] Degrees of freedom vs reported N, page 6

Reported: `t (86) = 12.23, p < .001`

Sentence: "The one-sample t-test on arousal and valence in the seated upright posture showed significantly smaller values for arousal (M = -3.15, SD = 4.91, t (86) = 5.99, p < .001, d = .64) and significantly larger values for valence (M = 4.69, SD = 3.56, t (86) = 12.23, p < .001, d = 1.31)."

The degrees of freedom in t(86) = 12.23 imply at least 87 participants under the usual design, but the largest sample size mentioned in the paper is 29. Reported vs implied N differ; could be a repeated-measures design, trials as the unit of analysis, or a typo in the df.

### 3. [WARNING] Degrees of freedom vs reported N, page 10

Reported: `F (6.57, 34.15) = 35.09, p < .001`

Sentence: "Significant main effects were observed for arousal and valence (arousal: F (6.57, 34.15) = 35.09, p < .001, ηp 2 = .56; valence: F (5.85, 17.83) = 13.21, p < .001, ηp 2 = .32)."

The degrees of freedom in F(6.57, 34.15) = 35.09 imply at least 41 participants under the usual design, but the largest sample size mentioned in the paper is 29. Reported vs implied N differ; could be a repeated-measures design, trials as the unit of analysis, or a typo in the df.

### 4. [WARNING] Degrees of freedom vs reported N, page 11

Reported: `F (11, 335) = 3.14, p < .001`

Sentence: "The ANCOVA revealed a significant main effect (F (11, 335) = 3.14, p < .001, ηp 2 = .09)."

The degrees of freedom in F(11, 335) = 3.14 imply at least 347 participants under the usual design, but the largest sample size mentioned in the paper is 29. Reported vs implied N differ; could be a repeated-measures design, trials as the unit of analysis, or a typo in the df.

### 5. [WARNING] Degrees of freedom vs reported N, page 14

Reported: `t (49) = 6.77, p < .001`

Sentence: "The one-sample t-test on arousal and valence in the seated upright posture showed significantly smaller and larger values than the criterion of 0 for arousal (M = -4.78, SD = 4.99, t (49) = 6.77, p < .001, d = 0.96) and valence (M = 4.90, SD = 4.41, t (49) = 7.86, p < .001, d = 1.11), respectively, despite the exclusion of the phrase "medically correct posture" in the cover story."

The degrees of freedom in t(49) = 6.77 imply at least 50 participants under the usual design, but the largest sample size mentioned in the paper is 29. Reported vs implied N differ; could be a repeated-measures design, trials as the unit of analysis, or a typo in the df.

### 6. [WARNING] Degrees of freedom vs reported N, page 14

Reported: `t (49) = 7.86, p < .001`

Sentence: "The one-sample t-test on arousal and valence in the seated upright posture showed significantly smaller and larger values than the criterion of 0 for arousal (M = -4.78, SD = 4.99, t (49) = 6.77, p < .001, d = 0.96) and valence (M = 4.90, SD = 4.41, t (49) = 7.86, p < .001, d = 1.11), respectively, despite the exclusion of the phrase "medically correct posture" in the cover story."

The degrees of freedom in t(49) = 7.86 imply at least 50 participants under the usual design, but the largest sample size mentioned in the paper is 29. Reported vs implied N differ; could be a repeated-measures design, trials as the unit of analysis, or a typo in the df.

### 7. [WARNING] Degrees of freedom vs reported N, page 17

Reported: `F (5.85, 140.51) = 816.13, p < .001`

Sentence: "valence (arousal: F (5.85, 140.51) = 816.13, p < .001, ηp 2 = .50; valence: F (5.78, 158.98) = 6.86, p < .001, ηp 2 = .22)."

The degrees of freedom in F(5.85, 140.51) = 816.13 imply at least 146 participants under the usual design, but the largest sample size mentioned in the paper is 29. Reported vs implied N differ; could be a repeated-measures design, trials as the unit of analysis, or a typo in the df.

### 8. [WARNING] Degrees of freedom vs reported N, page 17

Reported: `F (5.78, 158.98) = 6.86, p < .001`

Sentence: "valence (arousal: F (5.85, 140.51) = 816.13, p < .001, ηp 2 = .50; valence: F (5.78, 158.98) = 6.86, p < .001, ηp 2 = .22)."

The degrees of freedom in F(5.78, 158.98) = 6.86 imply at least 164 participants under the usual design, but the largest sample size mentioned in the paper is 29. Reported vs implied N differ; could be a repeated-measures design, trials as the unit of analysis, or a typo in the df.

### 9. [WARNING] Degrees of freedom vs reported N, page 17

Reported: `F (6.13, 146.94) = 13.30, p < .001`

Sentence: "ANOVA revealed a significant main effect (F (6.13, 146.94) = 13.30, p < .001, ηp 2 = .36)."

The degrees of freedom in F(6.13, 146.94) = 13.3 imply at least 153 participants under the usual design, but the largest sample size mentioned in the paper is 29. Reported vs implied N differ; could be a repeated-measures design, trials as the unit of analysis, or a typo in the df.

### 10. [INFO] Degrees of freedom vs reported N, page 6

Reported: `F (2, 56) = 1.84, p = .17`

Sentence: "There were no significant main effects of experimental days on arousal and valence (arousal: F (2, 56) = 1.84, p = .17, ηp 2 = .06; valence: F (2, 56) = 1.91, p = .16, ηp 2 = .06)."

The degrees of freedom in F(2, 56) = 1.84 imply at least 59 participants under the usual design, but the largest sample size mentioned in the paper is 29. Reported vs implied N differ; could be a repeated-measures design, trials as the unit of analysis, or a typo in the df.

### 11. [INFO] Degrees of freedom vs reported N, page 6

Reported: `F (2, 56) = 1.91, p = .16`

Sentence: "There were no significant main effects of experimental days on arousal and valence (arousal: F (2, 56) = 1.84, p = .17, ηp 2 = .06; valence: F (2, 56) = 1.91, p = .16, ηp 2 = .06)."

The degrees of freedom in F(2, 56) = 1.91 imply at least 59 participants under the usual design, but the largest sample size mentioned in the paper is 29. Reported vs implied N differ; could be a repeated-measures design, trials as the unit of analysis, or a typo in the df.

### 12. [INFO] Degrees of freedom vs reported N, page 6

Reported: `F (2, 56) = 4.71, p = .01`

Sentence: "However, there was a significant main effect of experimental days on HR (F (2, 56) = 4.71, p = .01, ηp 2 = .14), and it was lower on day 1 than on days 2 and 3."

The degrees of freedom in F(2, 56) = 4.71 imply at least 59 participants under the usual design, but the largest sample size mentioned in the paper is 29. Reported vs implied N differ; could be a repeated-measures design, trials as the unit of analysis, or a typo in the df.

### 13. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 7

Reported: `p < .05`

Sentence: "....36 P10 3.31 3.30 5.31 < .001*** 0.99 P11 1.17 3.71 1.67.13 0.31 P12 4.03 3.61 5.91 < .001*** 1.10 Adjusted p-value indicates the p-value corrected using the Benjamini-Hochberg (BH) method. * denotes p < .05, ** denotes p < .01, *** denotes p < .001...."

'p < .05' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 14. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 7

Reported: `p < .01`

Sentence: "...31 < .001*** 0.99 P11 1.17 3.71 1.67.13 0.31 P12 4.03 3.61 5.91 < .001*** 1.10 Adjusted p-value indicates the p-value corrected using the Benjamini-Hochberg (BH) method. * denotes p < .05, ** denotes p < .01, *** denotes p < .001...."

'p < .01' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 15. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 7

Reported: `p < .001`

Sentence: "...1.17 3.71 1.67.13 0.31 P12 4.03 3.61 5.91 < .001*** 1.10 Adjusted p-value indicates the p-value corrected using the Benjamini-Hochberg (BH) method. * denotes p < .05, ** denotes p < .01, *** denotes p < .001...."

'p < .001' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 16. [INFO] Degrees of freedom vs reported N, page 10

Reported: `F (11, 18) = 16.77, p < .001`

Sentence: "A MANOVA of posture (12) was performed on the arousal and valence scores of the TDMS. Posture had a significant main effect (F (11, 18) = 16.77, p < .001, ηp 2 = .91)."

The degrees of freedom in F(11, 18) = 16.77 imply at least 30 participants under the usual design, but the largest sample size mentioned in the paper is 29. Reported vs implied N differ; could be a repeated-measures design, trials as the unit of analysis, or a typo in the df.

### 17. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 10

Reported: `ps < .05`

Sentence: "The multiple comparison test showed that, P2, 3, and 5 had higher arousal scores than P1 and 6-12 (ps < .05), and P4 had higher scores than P7 and 9-12 (ps < .05)."

'ps < .05' is a blanket p statement covering several tests at once. It cannot be checked against a specific test statistic.

### 18. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 10

Reported: `ps < .05`

Sentence: "The multiple comparison test showed that, P2, 3, and 5 had higher arousal scores than P1 and 6-12 (ps < .05), and P4 had higher scores than P7 and 9-12 (ps < .05)."

'ps < .05' is a blanket p statement covering several tests at once. It cannot be checked against a specific test statistic.

### 19. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 10

Reported: `ps < .05`

Sentence: "Moreover, P6 and 8 had higher scores than P9 and 11 (ps < .05), and P1, 7, 10, and 12 had higher scores than P11 (ps < .05)."

'ps < .05' is a blanket p statement covering several tests at once. It cannot be checked against a specific test statistic.

### 20. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 10

Reported: `ps < .05`

Sentence: "Moreover, P6 and 8 had higher scores than P9 and 11 (ps < .05), and P1, 7, 10, and 12 had higher scores than P11 (ps < .05)."

'ps < .05' is a blanket p statement covering several tests at once. It cannot be checked against a specific test statistic.

### 21. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 10

Reported: `ps < .05`

Sentence: "The valence scores of P5 and 10 were higher than those of P1-3 and 6-9 (ps < .05); P11 was higher than that of P3 (p < .05); and P12 was higher than that of P1-4 and 6-9 (ps < .05)."

'ps < .05' is a blanket p statement covering several tests at once. It cannot be checked against a specific test statistic.

### 22. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 10

Reported: `p < .05`

Sentence: "The valence scores of P5 and 10 were higher than those of P1-3 and 6-9 (ps < .05); P11 was higher than that of P3 (p < .05); and P12 was higher than that of P1-4 and 6-9 (ps < .05)."

'p < .05' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 23. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 10

Reported: `ps < .05`

Sentence: "The valence scores of P5 and 10 were higher than those of P1-3 and 6-9 (ps < .05); P11 was higher than that of P3 (p < .05); and P12 was higher than that of P1-4 and 6-9 (ps < .05)."

'ps < .05' is a blanket p statement covering several tests at once. It cannot be checked against a specific test statistic.

### 24. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 11

Reported: `ps < .05`

Sentence: "The multiple comparison test showed that HR was higher for P3 than for P9 and 11 (ps < .05) and for P5 than for P11 (ps < .05), indicating that P3 and 5 were postures with relatively high physical strain, such as not leaning on the backrest, placing hands on the head, raising shoulders, or placing hands on the lower back and expanding the chest."

'ps < .05' is a blanket p statement covering several tests at once. It cannot be checked against a specific test statistic.

### 25. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 11

Reported: `ps < .05`

Sentence: "The multiple comparison test showed that HR was higher for P3 than for P9 and 11 (ps < .05) and for P5 than for P11 (ps < .05), indicating that P3 and 5 were postures with relatively high physical strain, such as not leaning on the backrest, placing hands on the head, raising shoulders, or placing hands on the lower back and expanding the chest."

'ps < .05' is a blanket p statement covering several tests at once. It cannot be checked against a specific test statistic.

### 26. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 15

Reported: `p < .05`

Sentence: "...0.01 P9' -0.40 4.14 0.48.69 0.10 P10 2.92 3.65 4.00.002** 0.80 P11' 1.68 3.58 2.35.06 0.47 P12 4.24 3.72 5.70 < .001*** 1.14 Adjusted p indicates the p-value corrected using the BH method. * denotes p < .05, ** denotes p < .01, **** denotes p < .001...."

'p < .05' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 27. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 15

Reported: `p < .01`

Sentence: "...0.48.69 0.10 P10 2.92 3.65 4.00.002** 0.80 P11' 1.68 3.58 2.35.06 0.47 P12 4.24 3.72 5.70 < .001*** 1.14 Adjusted p indicates the p-value corrected using the BH method. * denotes p < .05, ** denotes p < .01, **** denotes p < .001...."

'p < .01' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 28. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 15

Reported: `p < .001`

Sentence: "...3.65 4.00.002** 0.80 P11' 1.68 3.58 2.35.06 0.47 P12 4.24 3.72 5.70 < .001*** 1.14 Adjusted p indicates the p-value corrected using the BH method. * denotes p < .05, ** denotes p < .01, **** denotes p < .001...."

'p < .001' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 29. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 17

Reported: `ps < .05`

Sentence: "The multiple comparison test showed that, P1', 2, 3', 4', 5, 6', and 9' had higher arousal scores than P7, 8, 10, 11', and 12 (ps < .05)."

'ps < .05' is a blanket p statement covering several tests at once. It cannot be checked against a specific test statistic.

### 30. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 17

Reported: `ps < .05`

Sentence: "The valence scores of P5 and 6' were higher than those of P2 and 3' (ps < .05), P10 was higher than that of P2 (p < .05), and P12 was higher than those of P1', 2, 3', 7, 8, and 9' (ps < .05)."

'ps < .05' is a blanket p statement covering several tests at once. It cannot be checked against a specific test statistic.

### 31. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 17

Reported: `p < .05`

Sentence: "The valence scores of P5 and 6' were higher than those of P2 and 3' (ps < .05), P10 was higher than that of P2 (p < .05), and P12 was higher than those of P1', 2, 3', 7, 8, and 9' (ps < .05)."

'p < .05' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 32. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 17

Reported: `ps < .05`

Sentence: "The valence scores of P5 and 6' were higher than those of P2 and 3' (ps < .05), P10 was higher than that of P2 (p < .05), and P12 was higher than those of P1', 2, 3', 7, 8, and 9' (ps < .05)."

'ps < .05' is a blanket p statement covering several tests at once. It cannot be checked against a specific test statistic.

### 33. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 18

Reported: `ps < .05`

Sentence: "was higher for P1' than for P8, 10, and 12 (ps < .05); for P3' and 6' than for P2, 5, 7, 9', 10, and 12 (ps < .05); for P4' than for P8 (p < .05); and for P11' than for P8, 10, and 12 (ps < .05)."

'ps < .05' is a blanket p statement covering several tests at once. It cannot be checked against a specific test statistic.

### 34. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 18

Reported: `ps < .05`

Sentence: "was higher for P1' than for P8, 10, and 12 (ps < .05); for P3' and 6' than for P2, 5, 7, 9', 10, and 12 (ps < .05); for P4' than for P8 (p < .05); and for P11' than for P8, 10, and 12 (ps < .05)."

'ps < .05' is a blanket p statement covering several tests at once. It cannot be checked against a specific test statistic.

### 35. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 18

Reported: `p < .05`

Sentence: "was higher for P1' than for P8, 10, and 12 (ps < .05); for P3' and 6' than for P2, 5, 7, 9', 10, and 12 (ps < .05); for P4' than for P8 (p < .05); and for P11' than for P8, 10, and 12 (ps < .05)."

'p < .05' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 36. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 18

Reported: `ps < .05`

Sentence: "was higher for P1' than for P8, 10, and 12 (ps < .05); for P3' and 6' than for P2, 5, 7, 9', 10, and 12 (ps < .05); for P4' than for P8 (p < .05); and for P11' than for P8, 10, and 12 (ps < .05)."

'ps < .05' is a blanket p statement covering several tests at once. It cannot be checked against a specific test statistic.

## All extracted test statistics

| Page | Statistic | Reported p | Recomputed p | Status |
|---:|---|---|---|---|
| 6 | F(2, 56) = 1.84 | p = 0.17 | 0.16829 | ok |
| 6 | F(2, 56) = 1.91 | p = 0.16 | 0.157603 | ok |
| 6 | F(2, 56) = 4.71 | p = 0.01 | 0.012864 | ok |
| 6 | t(86) = 5.99 | p < 0.001 | 0.0 | ok |
| 6 | t(86) = 12.23 | p < 0.001 | 0.0 | ok |
| 10 | F(11, 18) = 16.77 | p < 0.001 | 0.0 | ok |
| 10 | F(6.57, 34.15) = 35.09 | p < 0.001 | 0.0 | ok |
| 10 | F(5.85, 17.83) = 13.21 | p < 0.001 | 1.1e-05 | ok |
| 11 | F(11, 335) = 3.14 | p < 0.001 | 0.000469 | ok |
| 14 | t(24) = 1.12 | p = 0.28 | 0.273797 | ok |
| 14 | t(24) = 0.42 | p = 0.68 | 0.678222 | ok |
| 14 | t(24) = 0.15 | p = 0.88 | 0.882018 | ok |
| 14 | t(49) = 6.77 | p < 0.001 | 0.0 | ok |
| 14 | t(49) = 7.86 | p < 0.001 | 0.0 | ok |
| 16 | F(11, 14) = 5.97 | p = 0.001 | 0.001272 | ok |
| 17 | F(5.85, 140.51) = 816.13 | p < 0.001 | 0.0 | ok |
| 17 | F(5.78, 158.98) = 6.86 | p < 0.001 | 2e-06 | ok |
| 17 | F(6.13, 146.94) = 13.3 | p < 0.001 | 0.0 | ok |

## Notes and limitations

This report lists places where a value reported in the paper differs from the value recomputed from other reported numbers. A difference is not evidence of misconduct. Common benign causes are rounding, typos, one-tailed tests, corrections for multiple comparisons, adjusted degrees of freedom, non-integer scales (which make GRIM and GRIMMER inapplicable) and PDF text-extraction errors. Each flag should be read in the paper before drawing any conclusion.

GRIM and GRIMMER assume every score is a whole number and that the N in the same sentence or parenthesis is the N behind that mean; both assumptions fail for averaged multi-item scales, continuous measures and subgroup means. The df vs N check only flags tests whose df imply more participants than the paper mentions anywhere. Duplicated statistics are usually legitimate repetition.
