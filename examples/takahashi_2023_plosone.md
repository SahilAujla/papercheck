# papercheck report: takahashi_2023_plosone.pdf

Generated 2026-11-08 with papercheck 0.1.0. 16 pages, 23 test statistics with p values, 35 reported means (0 with a usable N for GRIM).

## Summary

| Check | Items examined | Errors | Warnings | Info |
|---|---:|---:|---:|---:|
| p value recomputation (statcheck style) | 23 | 0 | 2 | 0 |
| GRIM (means of integer data) | 0 | 0 | 0 | 0 |
| GRIMMER (SDs of integer data) | 0 | 0 | 0 | 0 |
| Degrees of freedom vs reported N | 23 | 0 | 2 | 1 |
| Duplicated statistics | 23 | 0 | 0 | 0 |
| Unverifiable statements (ps < .05, statistics without p, p without statistic) | 3 | 0 | 0 | 3 |
| 95% CI vs point estimate | 0 | 0 | 0 | 0 |
| Regression coefficient vs SE and p | 0 | 0 | 0 | 0 |

Total flags: 8 (errors 0, warnings 4, info 4).

Severity: an error is a reported vs recomputed p value on different sides of .05 (the conclusion about significance would change). A warning is a numeric inconsistency that does not change the decision, or a GRIM failure. Info items are worth a look but have common benign explanations.

## Flagged items

### 1. [WARNING] p value recomputation (statcheck style), page 9

Reported: `F(2, 296) = 5.12, p = .004`

Sentence: "Although the effect of gender was not significant, F(1, 296) = 0.001, p = .977, ηp 2 < .001, we found an unexpected condition × gender interaction effect, F(2, 296) = 5.12, p = .004, ηp 2 = .036."

Reported F(2, 296) = 5.12, p = .004. Recomputed p = 0.0065 (range 0.0065 to 0.0065 given rounding of the test statistic) does not match the reported p. The significance decision is unchanged.

Recomputed p = 0.006516 (interval [0.006485, 0.006548]); consistent if one-tailed: False; decision error: False.

### 2. [WARNING] p value recomputation (statcheck style), page 10

Reported: `r(286) = .15, p = .037`

Sentence: "...ified as "fiction." Although this is mere speculation, it should be noted that once the literary fiction condition was removed, the correlation between fiction reading time and FS became significant, r(286) = .15, p = .037...."

Reported r(286) = .15, p = .037. Recomputed p = 0.0108 (range 0.0084 to 0.0138 given rounding of the test statistic) does not match the reported p. The significance decision is unchanged.

Recomputed p = 0.010805 (interval [0.008415, 0.013776]); consistent if one-tailed: False; decision error: False.

### 3. [WARNING] Degrees of freedom vs reported N, page 10

Reported: `r(378) = .09, p = .094`

Sentence: "Even FS was not significantly correlated with fiction reading time, r(378) = .09, p = .094."

The degrees of freedom in r(378) = 0.09 imply at least 380 participants under the usual design, but the largest sample size mentioned in the paper is 338. Reported vs implied N differ; could be a repeated-measures design, trials as the unit of analysis, or a typo in the df.

### 4. [WARNING] Degrees of freedom vs reported N, page 11

Reported: `r(378) = .16, p = .002`

Sentence: "We included a vocabulary test in Study 2 and found that fiction reading time was significantly correlated with the vocabulary test score, r(378) = .16, p = .002."

The degrees of freedom in r(378) = 0.16 imply at least 380 participants under the usual design, but the largest sample size mentioned in the paper is 338. Reported vs implied N differ; could be a repeated-measures design, trials as the unit of analysis, or a typo in the df.

### 5. [INFO] Degrees of freedom vs reported N, page 10

Reported: `F(3, 400) = 1.02, p = .382`

Sentence: "When the new data were combined with the original Study 2 data, there was no significant effect of the four conditions (i.e., original "calculation" control, new "no task" control, literary fiction, and nonfiction conditions) on ΔRMET: F(3, 400) = 1.02, p = .382, η2 = .008."

The degrees of freedom in F(3, 400) = 1.02 imply at least 404 participants under the usual design, but the largest sample size mentioned in the paper is 338. Reported vs implied N differ; could be a repeated-measures design, trials as the unit of analysis, or a typo in the df.

### 6. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 10

Reported: `all ps > .40`

Sentence: "Fiction reading time was not significantly correlated with the three variants of the RMET score: r(378) = .003, .006, and .006 for the RMET-A, RMET-B, and total RMET (i.e., RMET-A + RMET-B) scores, respectively (all ps > .40)."

'all ps > .40' is a blanket p statement covering several tests at once. It cannot be checked against a specific test statistic.

### 7. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 12

Reported: `r(402) = .30`

Sentence: "In fact, the correlation between RMET-A and RMET-B was low: r(402) = .30."

'r(402) = .30' is reported without a p value in the same sentence, so it cannot be verified. The statistic implies a two-tailed p = 7.58e-10.

### 8. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 12

Reported: `p = .049`

Sentence: "Moreover, RMET performance is known to be positively associated with vocabulary (our measure of vocabulary was also significantly, but weakly, correlated with RMET score: r402 = .098, p = .049)."

'p = .049' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

## All extracted test statistics

| Page | Statistic | Reported p | Recomputed p | Status |
|---:|---|---|---|---|
| 4 | r(315) = 0.21 | p < 0.001 | 0.000166 | ok |
| 4 | r(315) = 0.11 | p = 0.052 | 0.050383 | ok |
| 5 | t(337) = 4.25 | p < 0.001 | 2.8e-05 | ok |
| 6 | r(335) = 0.11 | p = 0.042 | 0.043596 | ok |
| 6 | r(336) = -0.12 | p = 0.032 | 0.027386 | ok |
| 6 | r(336) = 0.15 | p = 0.006 | 0.005725 | ok |
| 6 | r(336) = 0.19 | p < 0.001 | 0.000444 | ok |
| 6 | r(335) = 0.14 | p = 0.012 | 0.010076 | ok |
| 7 | t(337) = 0.34 | ns | 0.734068 | ok |
| 9 | F(2, 301) = 1.05 | p = 0.353 | 0.351216 | ok |
| 9 | F(2, 301) = 1.43 | p = 0.242 | 0.24093 | ok |
| 9 | F(2, 296) = 1.47 | p = 0.232 | 0.231599 | ok |
| 9 | F(1, 296) = 0.001 | p = 0.977 | 0.974794 | ok |
| 9 | F(2, 296) = 5.12 | p = 0.004 | 0.006516 | flagged |
| 10 | t(100) = -2.8 | p = 0.006 | 0.006134 | ok |
| 10 | t(101) = -3.62 | p < 0.001 | 0.000462 | ok |
| 10 | t(100) = -1.2 | p = 0.234 | 0.232975 | ok |
| 10 | F(2, 301) = 0.93 | p = 0.398 | 0.395684 | ok |
| 10 | t(99) = -2.36 | p = 0.02 | 0.020236 | ok |
| 10 | F(3, 400) = 1.02 | p = 0.382 | 0.383653 | ok |
| 10 | r(378) = 0.09 | p = 0.094 | 0.079739 | ok |
| 10 | r(286) = 0.15 | p = 0.037 | 0.010805 | flagged |
| 11 | r(378) = 0.16 | p = 0.002 | 0.001755 | ok |

## Notes and limitations

This report lists places where a value reported in the paper differs from the value recomputed from other reported numbers. A difference is not evidence of misconduct. Common benign causes are rounding, typos, one-tailed tests, corrections for multiple comparisons, adjusted degrees of freedom, non-integer scales (which make GRIM and GRIMMER inapplicable) and PDF text-extraction errors. Each flag should be read in the paper before drawing any conclusion.

GRIM and GRIMMER assume every score is a whole number and that the N in the same sentence or parenthesis is the N behind that mean; both assumptions fail for averaged multi-item scales, continuous measures and subgroup means. The df vs N check only flags tests whose df imply more participants than the paper mentions anywhere. Duplicated statistics are usually legitimate repetition.
