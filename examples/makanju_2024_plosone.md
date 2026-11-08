# papercheck report: makanju_2024_plosone.pdf

Generated 2026-11-08 with papercheck 0.1.0. 34 pages, 28 test statistics with p values, 31 reported means (7 with a usable N for GRIM).

## Summary

| Check | Items examined | Errors | Warnings | Info |
|---|---:|---:|---:|---:|
| p value recomputation (statcheck style) | 28 | 0 | 1 | 0 |
| GRIM (means of integer data) | 7 | 0 | 0 | 0 |
| GRIMMER (SDs of integer data) | 7 | 0 | 0 | 0 |
| Degrees of freedom vs reported N | 28 | 0 | 3 | 0 |
| Duplicated statistics | 28 | 0 | 0 | 0 |

Total flags: 4 (errors 0, warnings 4, info 0).

Severity: an error is a reported vs recomputed p value on different sides of .05 (the conclusion about significance would change). A warning is a numeric inconsistency that does not change the decision, or a GRIM failure. Info items are worth a look but have common benign explanations.

## Flagged items

### 1. [WARNING] Degrees of freedom vs reported N, page 9

Reported: `F(6, 1156) = 22.09, p < .001`

Sentence: "Using Wilks' lambda, there was a significant effect of historical representation condition, λ = 0.81, F(6, 1156) = 22.09, p < .001, ηp 2 = .102."

The degrees of freedom in F(6, 1156) = 22.09 imply at least 1163 participants under the usual design, but the largest sample size mentioned in the paper is 950. Reported vs implied N differ; could be a repeated-measures design, trials as the unit of analysis, or a typo in the df.

### 2. [WARNING] Degrees of freedom vs reported N, page 10

Reported: `F(4, 1186) = 0.42, p = .792`

Sentence: "Using Wilks' lambda, there was a non-significant effect of historical representation, λ = 0.98, F(4, 1186) = 0.42, p = .792, ηp 2 = .001."

The degrees of freedom in F(4, 1186) = 0.42 imply at least 1191 participants under the usual design, but the largest sample size mentioned in the paper is 950. Reported vs implied N differ; could be a repeated-measures design, trials as the unit of analysis, or a typo in the df.

### 3. [WARNING] Degrees of freedom vs reported N, page 11

Reported: `F(6, 1158) = 1.55, p = .157`

Sentence: "Using Wilks' lambda, there was a non-significant effect of historical representation on group-based action, λ = 0.98, F(6, 1158) = 1.55, p = .157, ηp 2 = .008."

The degrees of freedom in F(6, 1158) = 1.55 imply at least 1165 participants under the usual design, but the largest sample size mentioned in the paper is 950. Reported vs implied N differ; could be a repeated-measures design, trials as the unit of analysis, or a typo in the df.

### 4. [WARNING] p value recomputation (statcheck style), page 24

Reported: `F(3, 240) = 0.08, p = .974`

Sentence: "up ANOVA main effects of consciousness-raising and collective political action; and (3) a null interaction effect of the subjective importance of African history and historical representations, λ = 1.00, F(3, 240) = 0.08, p = .974, ηp 2 = .001."

Reported F(3, 240) = 0.08, p = .974. Recomputed p = 0.9708 (range 0.9682 to 0.9734 given rounding of the test statistic) does not match the reported p. The significance decision is unchanged.

Recomputed p = 0.970822 (interval [0.968187, 0.973395]); consistent if one-tailed: False; decision error: False.

## All extracted test statistics

| Page | Statistic | Reported p | Recomputed p | Status |
|---:|---|---|---|---|
| 9 | F(6, 1156) = 22.09 | p < 0.001 | 0.0 | ok |
| 9 | F(2, 583) = 48.84 | p < 0.001 | 0.0 | ok |
| 9 | F(2, 583) = 4.7 | p = 0.009 | 0.009443 | ok |
| 10 | F(2, 583) = 1.91 | p = 0.149 | 0.149006 | ok |
| 10 | F(4, 1186) = 0.42 | p = 0.792 | 0.794306 | ok |
| 10 | F(2, 594) = 0.2 | p = 0.823 | 0.818786 | ok |
| 10 | F(2, 594) = 0.39 | p = 0.675 | 0.67723 | ok |
| 11 | F(6, 1158) = 1.55 | p = 0.157 | 0.158493 | ok |
| 11 | F(2, 581) = 3.13 | p = 0.044 | 0.044456 | ok |
| 11 | F(2, 581) = 1.61 | p = 0.201 | 0.200778 | ok |
| 11 | F(2, 581) = 2.6 | p = 0.075 | 0.075138 | ok |
| 21 | F(1, 266) = 5.24 | p = 0.023 | 0.022857 | ok |
| 21 | F(1, 266) = 1.71 | p = 0.192 | 0.192114 | ok |
| 22 | F(1, 252) = 9.08 | p = 0.003 | 0.002848 | ok |
| 22 | F(1, 252) = 7.2 | p = 0.008 | 0.007773 | ok |
| 22 | F(1, 265) = 61.6 | p < 0.001 | 0.0 | ok |
| 22 | F(1, 249) = 30.01 | p < 0.001 | 0.0 | ok |
| 22 | F(1, 266) = 3.23 | p = 0.073 | 0.073435 | ok |
| 22 | F(1, 266) = 1.36 | p = 0.245 | 0.244582 | ok |
| 23 | F(1, 253) = 4.21 | p = 0.041 | 0.041216 | ok |
| 23 | F(3, 264) = 1.19 | p = 0.313 | 0.313982 | ok |
| 23 | F(3, 264) = 1.74 | p = 0.159 | 0.159162 | ok |
| 23 | F(3, 264) = 1.85 | p = 0.138 | 0.138469 | ok |
| 23 | F(3, 240) = 0.19 | p = 0.906 | 0.903149 | ok |
| 23 | F(3, 240) = 3.75 | p = 0.012 | 0.011634 | ok |
| 24 | F(3, 240) = 0.08 | p = 0.974 | 0.970822 | flagged |
| 24 | F(1, 242) = 4.58 | p = 0.033 | 0.033347 | ok |
| 24 | F(1, 242) = 4.21 | p = 0.041 | 0.041263 | ok |

## Notes and limitations

This report lists places where a value reported in the paper differs from the value recomputed from other reported numbers. A difference is not evidence of misconduct. Common benign causes are rounding, typos, one-tailed tests, corrections for multiple comparisons, adjusted degrees of freedom, non-integer scales (which make GRIM and GRIMMER inapplicable) and PDF text-extraction errors. Each flag should be read in the paper before drawing any conclusion.

GRIM and GRIMMER assume every score is a whole number and that the N in the same sentence or parenthesis is the N behind that mean; both assumptions fail for averaged multi-item scales, continuous measures and subgroup means. The df vs N check only flags tests whose df imply more participants than the paper mentions anywhere. Duplicated statistics are usually legitimate repetition.
