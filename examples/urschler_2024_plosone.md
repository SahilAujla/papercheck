# papercheck report: urschler_2024_plosone.pdf

Generated 2026-11-08 with papercheck 0.1.0. 17 pages, 25 test statistics with p values, 18 reported means (0 with a usable N for GRIM).

## Summary

| Check | Items examined | Errors | Warnings | Info |
|---|---:|---:|---:|---:|
| p value recomputation (statcheck style) | 25 | 0 | 5 | 0 |
| GRIM (means of integer data) | 0 | 0 | 0 | 0 |
| GRIMMER (SDs of integer data) | 0 | 0 | 0 | 0 |
| Degrees of freedom vs reported N | 25 | 0 | 1 | 0 |
| Duplicated statistics | 25 | 0 | 0 | 0 |
| Unverifiable statements (ps < .05, statistics without p, p without statistic) | 2 | 0 | 0 | 2 |
| 95% CI vs point estimate | 0 | 0 | 0 | 0 |
| Regression coefficient vs SE and p | 0 | 0 | 0 | 0 |

Total flags: 8 (errors 0, warnings 6, info 2).

Severity: an error is a reported vs recomputed p value on different sides of .05 (the conclusion about significance would change). A warning is a numeric inconsistency that does not change the decision, or a GRIM failure. Info items are worth a look but have common benign explanations.

## Flagged items

### 1. [WARNING] p value recomputation (statcheck style), page 7

Reported: `t(278) = 1.02, p = .312`

Sentence: "However, responsibility did not significantly affect people's willingness to intervene in the moral courage situation (not responsible: M = 5.68, SD = 1.21; responsible: M = 5.41, SD = 1.45), t(278) = 1.02, p = .312."

Reported t(278) = 1.02, p = .312. Recomputed p = 0.3086 (range 0.3063 to 0.3110 given rounding of the test statistic) does not match the reported p. The significance decision is unchanged.

Recomputed p = 0.308615 (interval [0.306254, 0.310988]); consistent if one-tailed: False; decision error: False.

### 2. [WARNING] p value recomputation (statcheck style), page 7

Reported: `t(278) = -0.91, p = .358`

Sentence: "Similar results could be overserved for the more-severe situation (not responsible: M = 6.17, SD = 1.25; responsible: M = 6.41, SD = 0.72, t(278) = -0.91, p = .358)."

Reported t(278) = -0.91, p = .358. Recomputed p = 0.3636 (range 0.3610 to 0.3662 given rounding of the test statistic) does not match the reported p. The significance decision is unchanged.

Recomputed p = 0.363611 (interval [0.360985, 0.366249]); consistent if one-tailed: False; decision error: False.

### 3. [WARNING] p value recomputation (statcheck style), page 7

Reported: `F(1, 278) = 2.65, p = .073`

Sentence: "Neither the Severity by Kinship interaction, F(1, 278) = 2.65, p = .073, nor the Severity by Responsibility interaction, F(1, 278) = 2.10, p = .150, was significant (see Fig 1)."

Reported F(1, 278) = 2.65, p = .073. Recomputed p = 0.1047 (range 0.1044 to 0.1050 given rounding of the test statistic) does not match the reported p. The significance decision is unchanged.

Recomputed p = 0.104683 (interval [0.104357, 0.105009]); consistent if one-tailed: False; decision error: False.

### 4. [WARNING] p value recomputation (statcheck style), page 7

Reported: `F(1, 278) = 2.10, p = .150`

Sentence: "Neither the Severity by Kinship interaction, F(1, 278) = 2.65, p = .073, nor the Severity by Responsibility interaction, F(1, 278) = 2.10, p = .150, was significant (see Fig 1)."

Reported F(1, 278) = 2.10, p = .150. Recomputed p = 0.1484 (range 0.1479 to 0.1489 given rounding of the test statistic) does not match the reported p. The significance decision is unchanged.

Recomputed p = 0.148426 (interval [0.147946, 0.148908]); consistent if one-tailed: False; decision error: False.

### 5. [WARNING] p value recomputation (statcheck style), page 9

Reported: `F(1, 334) = 0.85, p = .427`

Sentence: "Neither the Severity by Kinship interaction, F(1, 334) = 0.85, p = .427, nor the Responsibility by Kinship interaction, F(1, 334) = 1.01, p = .316, was significant."

Reported F(1, 334) = 0.85, p = .427. Recomputed p = 0.3572 (range 0.3558 to 0.3586 given rounding of the test statistic) does not match the reported p. The significance decision is unchanged.

Recomputed p = 0.357218 (interval [0.355809, 0.358634]); consistent if one-tailed: False; decision error: False.

### 6. [WARNING] Degrees of freedom vs reported N, page 14

Reported: `t(634) = 1.08, p = .282`

Sentence: "to intervene, t(634) = 1.08, p = .282, d = 0.09, 95% CI [-0.07, 0.24]."

The degrees of freedom in t(634) = 1.08 imply at least 635 participants under the usual design, but the largest sample size mentioned in the paper is 346. Reported vs implied N differ; could be a repeated-measures design, trials as the unit of analysis, or a typo in the df.

### 7. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 11

Reported: `p < .05`

Sentence: "PC = perceived costs for intervening, D1 = difference between the less-severe and moral courage situation; D2 = difference between less-severe and more-severe situation, WTI = willingness to intervene. *p < .05 **p < .001. https://doi.org/10.1371/journal.pone.0307740.g003 PLOS ONE Standing-up against moral violations PLOS ONE | https://doi.org/10.1371/journal.pone.0307740 August 12, 2024 11 / 17"

'p < .05' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 8. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 11

Reported: `p < .001`

Sentence: "PC = perceived costs for intervening, D1 = difference between the less-severe and moral courage situation; D2 = difference between less-severe and more-severe situation, WTI = willingness to intervene. *p < .05 **p < .001. https://doi.org/10.1371/journal.pone.0307740.g003 PLOS ONE Standing-up against moral violations PLOS ONE | https://doi.org/10.1371/journal.pone.0307740 August 12, 2024 11 / 17"

'p < .001' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

## All extracted test statistics

| Page | Statistic | Reported p | Recomputed p | Status |
|---:|---|---|---|---|
| 6 | t(288) = 13.38 | p < 0.001 | 0.0 | ok |
| 6 | chi2(29) = 13.99 | p = 0.991 | 0.991428 | ok |
| 6 | F(1, 278) = 8.59 | p = 0.004 | 0.003661 | ok |
| 6 | F(2, 278) = 14.96 | p < 0.001 | 1e-06 | ok |
| 6 | F(1, 278) = 3.58 | p = 0.059 | 0.059518 | ok |
| 7 | F(2, 278) = 9.06 | p < 0.001 | 0.000154 | ok |
| 7 | t(278) = 4.98 | p < 0.001 | 1e-06 | ok |
| 7 | t(278) = 1.02 | p = 0.312 | 0.308615 | flagged |
| 7 | t(278) = -0.91 | p = 0.358 | 0.363611 | flagged |
| 7 | F(1, 278) = 2.65 | p = 0.073 | 0.104683 | flagged |
| 7 | F(1, 278) = 2.1 | p = 0.15 | 0.148426 | flagged |
| 7 | F(2, 278) = 0.78 | p = 0.457 | 0.459407 | ok |
| 9 | t(344) = 14.47 | p < 0.001 | 0.0 | ok |
| 9 | chi2(18) = 11.52 | p = 0.871 | 0.871003 | ok |
| 9 | F(2, 334) = 27.65 | p < 0.001 | 0.0 | ok |
| 9 | F(1, 334) = 0.1 | p = 0.752 | 0.752027 | ok |
| 9 | F(1, 334) = 1.78 | p = 0.183 | 0.183058 | ok |
| 9 | F(2, 334) = 5.84 | p = 0.003 | 0.003214 | ok |
| 9 | t(334) = 3.45 | p < 0.001 | 0.000632 | ok |
| 9 | t(334) = -1.21 | p = 0.227 | 0.227135 | ok |
| 9 | t(334) < 0.01 | p = 0.999 | 0.992027 | ok |
| 9 | F(1, 334) = 0.85 | p = 0.427 | 0.357218 | flagged |
| 9 | F(1, 334) = 1.01 | p = 0.316 | 0.31563 | ok |
| 10 | F(2, 334) = 1.49 | p = 0.227 | 0.226867 | ok |
| 14 | t(634) = 1.08 | p = 0.282 | 0.280553 | ok |

## Notes and limitations

This report lists places where a value reported in the paper differs from the value recomputed from other reported numbers. A difference is not evidence of misconduct. Common benign causes are rounding, typos, one-tailed tests, corrections for multiple comparisons, adjusted degrees of freedom, non-integer scales (which make GRIM and GRIMMER inapplicable) and PDF text-extraction errors. Each flag should be read in the paper before drawing any conclusion.

GRIM and GRIMMER assume every score is a whole number and that the N in the same sentence or parenthesis is the N behind that mean; both assumptions fail for averaged multi-item scales, continuous measures and subgroup means. The df vs N check only flags tests whose df imply more participants than the paper mentions anywhere. Duplicated statistics are usually legitimate repetition.
