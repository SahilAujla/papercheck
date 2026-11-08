# papercheck report: takayama_2023_plosone.pdf

Generated 2026-11-08 with papercheck 0.1.0. 22 pages, 18 test statistics with p values, 4 reported means (0 with a usable N for GRIM).

## Summary

| Check | Items examined | Errors | Warnings | Info |
|---|---:|---:|---:|---:|
| p value recomputation (statcheck style) | 18 | 0 | 0 | 0 |
| GRIM (means of integer data) | 0 | 0 | 0 | 0 |
| GRIMMER (SDs of integer data) | 0 | 0 | 0 | 0 |
| Degrees of freedom vs reported N | 18 | 0 | 13 | 0 |
| Duplicated statistics | 18 | 0 | 0 | 0 |

Total flags: 13 (errors 0, warnings 13, info 0).

Severity: an error is a reported vs recomputed p value on different sides of .05 (the conclusion about significance would change). A warning is a numeric inconsistency that does not change the decision, or a GRIM failure. Info items are worth a look but have common benign explanations.

## Flagged items

### 1. [WARNING] Degrees of freedom vs reported N, page 6

Reported: `F (2, 56) = 1.84, p = .17`

Sentence: "There were no significant main effects of experimental days on arousal and valence (arousal: F (2, 56) = 1.84, p = .17, ηp 2 = .06; valence: F (2, 56) = 1.91, p = .16, ηp 2 = .06)."

The degrees of freedom in F(2, 56) = 1.84 imply at least 59 participants under the usual design, but the largest sample size mentioned in the paper is 29. Reported vs implied N differ; could be a repeated-measures design, trials as the unit of analysis, or a typo in the df.

### 2. [WARNING] Degrees of freedom vs reported N, page 6

Reported: `F (2, 56) = 1.91, p = .16`

Sentence: "There were no significant main effects of experimental days on arousal and valence (arousal: F (2, 56) = 1.84, p = .17, ηp 2 = .06; valence: F (2, 56) = 1.91, p = .16, ηp 2 = .06)."

The degrees of freedom in F(2, 56) = 1.91 imply at least 59 participants under the usual design, but the largest sample size mentioned in the paper is 29. Reported vs implied N differ; could be a repeated-measures design, trials as the unit of analysis, or a typo in the df.

### 3. [WARNING] Degrees of freedom vs reported N, page 6

Reported: `F (2, 56) = 4.71, p = .01`

Sentence: "However, there was a significant main effect of experimental days on HR (F (2, 56) = 4.71, p = .01, ηp 2 = .14), and it was lower on day 1 than on days 2 and 3."

The degrees of freedom in F(2, 56) = 4.71 imply at least 59 participants under the usual design, but the largest sample size mentioned in the paper is 29. Reported vs implied N differ; could be a repeated-measures design, trials as the unit of analysis, or a typo in the df.

### 4. [WARNING] Degrees of freedom vs reported N, page 6

Reported: `t (86) = 5.99, p < .001`

Sentence: "The one-sample t-test on arousal and valence in the seated upright posture showed significantly smaller values for arousal (M = -3.15, SD = 4.91, t (86) = 5.99, p < .001, d = .64) and significantly larger values for valence (M = 4.69, SD = 3.56, t (86) = 12.23, p < .001, d = 1.31)."

The degrees of freedom in t(86) = 5.99 imply at least 87 participants under the usual design, but the largest sample size mentioned in the paper is 29. Reported vs implied N differ; could be a repeated-measures design, trials as the unit of analysis, or a typo in the df.

### 5. [WARNING] Degrees of freedom vs reported N, page 6

Reported: `t (86) = 12.23, p < .001`

Sentence: "The one-sample t-test on arousal and valence in the seated upright posture showed significantly smaller values for arousal (M = -3.15, SD = 4.91, t (86) = 5.99, p < .001, d = .64) and significantly larger values for valence (M = 4.69, SD = 3.56, t (86) = 12.23, p < .001, d = 1.31)."

The degrees of freedom in t(86) = 12.23 imply at least 87 participants under the usual design, but the largest sample size mentioned in the paper is 29. Reported vs implied N differ; could be a repeated-measures design, trials as the unit of analysis, or a typo in the df.

### 6. [WARNING] Degrees of freedom vs reported N, page 10

Reported: `F (11, 18) = 16.77, p < .001`

Sentence: "A MANOVA of posture (12) was performed on the arousal and valence scores of the TDMS. Posture had a significant main effect (F (11, 18) = 16.77, p < .001, ηp 2 = .91)."

The degrees of freedom in F(11, 18) = 16.77 imply at least 30 participants under the usual design, but the largest sample size mentioned in the paper is 29. Reported vs implied N differ; could be a repeated-measures design, trials as the unit of analysis, or a typo in the df.

### 7. [WARNING] Degrees of freedom vs reported N, page 10

Reported: `F (6.57, 34.15) = 35.09, p < .001`

Sentence: "Significant main effects were observed for arousal and valence (arousal: F (6.57, 34.15) = 35.09, p < .001, ηp 2 = .56; valence: F (5.85, 17.83) = 13.21, p < .001, ηp 2 = .32)."

The degrees of freedom in F(6.57, 34.15) = 35.09 imply at least 41 participants under the usual design, but the largest sample size mentioned in the paper is 29. Reported vs implied N differ; could be a repeated-measures design, trials as the unit of analysis, or a typo in the df.

### 8. [WARNING] Degrees of freedom vs reported N, page 11

Reported: `F (11, 335) = 3.14, p < .001`

Sentence: "The ANCOVA revealed a significant main effect (F (11, 335) = 3.14, p < .001, ηp 2 = .09)."

The degrees of freedom in F(11, 335) = 3.14 imply at least 347 participants under the usual design, but the largest sample size mentioned in the paper is 29. Reported vs implied N differ; could be a repeated-measures design, trials as the unit of analysis, or a typo in the df.

### 9. [WARNING] Degrees of freedom vs reported N, page 14

Reported: `t (49) = 6.77, p < .001`

Sentence: "The one-sample t-test on arousal and valence in the seated upright posture showed significantly smaller and larger values than the criterion of 0 for arousal (M = -4.78, SD = 4.99, t (49) = 6.77, p < .001, d = 0.96) and valence (M = 4.90, SD = 4.41, t (49) = 7.86, p < .001, d = 1.11), respectively, despite the exclusion of the phrase "medically correct posture" in the cover story."

The degrees of freedom in t(49) = 6.77 imply at least 50 participants under the usual design, but the largest sample size mentioned in the paper is 29. Reported vs implied N differ; could be a repeated-measures design, trials as the unit of analysis, or a typo in the df.

### 10. [WARNING] Degrees of freedom vs reported N, page 14

Reported: `t (49) = 7.86, p < .001`

Sentence: "The one-sample t-test on arousal and valence in the seated upright posture showed significantly smaller and larger values than the criterion of 0 for arousal (M = -4.78, SD = 4.99, t (49) = 6.77, p < .001, d = 0.96) and valence (M = 4.90, SD = 4.41, t (49) = 7.86, p < .001, d = 1.11), respectively, despite the exclusion of the phrase "medically correct posture" in the cover story."

The degrees of freedom in t(49) = 7.86 imply at least 50 participants under the usual design, but the largest sample size mentioned in the paper is 29. Reported vs implied N differ; could be a repeated-measures design, trials as the unit of analysis, or a typo in the df.

### 11. [WARNING] Degrees of freedom vs reported N, page 17

Reported: `F (5.85, 140.51) = 816.13, p < .001`

Sentence: "valence (arousal: F (5.85, 140.51) = 816.13, p < .001, ηp 2 = .50; valence: F (5.78, 158.98) = 6.86, p < .001, ηp 2 = .22)."

The degrees of freedom in F(5.85, 140.51) = 816.13 imply at least 146 participants under the usual design, but the largest sample size mentioned in the paper is 29. Reported vs implied N differ; could be a repeated-measures design, trials as the unit of analysis, or a typo in the df.

### 12. [WARNING] Degrees of freedom vs reported N, page 17

Reported: `F (5.78, 158.98) = 6.86, p < .001`

Sentence: "valence (arousal: F (5.85, 140.51) = 816.13, p < .001, ηp 2 = .50; valence: F (5.78, 158.98) = 6.86, p < .001, ηp 2 = .22)."

The degrees of freedom in F(5.78, 158.98) = 6.86 imply at least 164 participants under the usual design, but the largest sample size mentioned in the paper is 29. Reported vs implied N differ; could be a repeated-measures design, trials as the unit of analysis, or a typo in the df.

### 13. [WARNING] Degrees of freedom vs reported N, page 17

Reported: `F (6.13, 146.94) = 13.30, p < .001`

Sentence: "ANOVA revealed a significant main effect (F (6.13, 146.94) = 13.30, p < .001, ηp 2 = .36)."

The degrees of freedom in F(6.13, 146.94) = 13.3 imply at least 153 participants under the usual design, but the largest sample size mentioned in the paper is 29. Reported vs implied N differ; could be a repeated-measures design, trials as the unit of analysis, or a typo in the df.

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
