# papercheck report: gill_2023_plosone.pdf

Generated 2026-11-08 with papercheck 0.1.0. 22 pages, 48 test statistics with p values, 9 reported means (0 with a usable N for GRIM).

## Summary

| Check | Items examined | Errors | Warnings | Info |
|---|---:|---:|---:|---:|
| p value recomputation (statcheck style) | 48 | 0 | 1 | 0 |
| GRIM (means of integer data) | 0 | 0 | 0 | 0 |
| GRIMMER (SDs of integer data) | 0 | 0 | 0 | 0 |
| Degrees of freedom vs reported N | 48 | 0 | 2 | 0 |
| Duplicated statistics | 48 | 0 | 0 | 0 |

Total flags: 3 (errors 0, warnings 3, info 0).

Severity: an error is a reported vs recomputed p value on different sides of .05 (the conclusion about significance would change). A warning is a numeric inconsistency that does not change the decision, or a GRIM failure. Info items are worth a look but have common benign explanations.

## Flagged items

### 1. [WARNING] p value recomputation (statcheck style), page 12

Reported: `t(92.83) = 2.77, p = .001`

Sentence: "And, compassion was higher in narrative-affirm history than in narrative-neutral, t(92.83) = 2.77, p = .001."

Reported t(92.83) = 2.77, p = .001. Recomputed p = 0.0068 (range 0.0067 to 0.0069 given rounding of the test statistic) does not match the reported p. The significance decision is unchanged.

Recomputed p = 0.00677 (interval [0.006675, 0.006867]); consistent if one-tailed: False; decision error: False.

### 2. [WARNING] Degrees of freedom vs reported N, page 13

Reported: `t(267) = .65, p = .516`

Sentence: "As can be seen there, and as described above, jury groups within the deed only and narrative-neutral conditions did not differ in their perceptions of Robert Harris' freedom of action, t(267) = .65, p = .516."

The degrees of freedom in t(267) = 0.65 imply at least 268 participants under the usual design, but the largest sample size mentioned in the paper is 192. Reported vs implied N differ; could be a repeated-measures design, trials as the unit of analysis, or a typo in the df.

### 3. [WARNING] Degrees of freedom vs reported N, page 13

Reported: `t(267) = -4.52, p < .001`

Sentence: "In contrast, the narrative-neutral condition resulted in lower perceptions of control of self-formation compared to deed only, t(267) = -4.52, p < .001."

The degrees of freedom in t(267) = -4.52 imply at least 268 participants under the usual design, but the largest sample size mentioned in the paper is 192. Reported vs implied N differ; could be a repeated-measures design, trials as the unit of analysis, or a typo in the df.

## All extracted test statistics

| Page | Statistic | Reported p | Recomputed p | Status |
|---:|---|---|---|---|
| 8 | t(188) = 0.15 | p = 0.88 | 0.880925 | ok |
| 8 | t(188) = 0.3 | p = 0.77 | 0.764509 | ok |
| 8 | t(188) = 7.95 | p < 0.001 | 0.0 | ok |
| 8 | chi2(3) = 3.3 | p = 0.35 | 0.347643 | ok |
| 9 | F(3, 184.035) = 15.27 | p < 0.001 | 0.0 | ok |
| 10 | F(3, 186.54) = 33.83 | p < 0.001 | 0.0 | ok |
| 10 | t(182.52) = -4.5 | p < 0.001 | 1.2e-05 | ok |
| 10 | t(181.98) = -4.05 | p < 0.001 | 7.6e-05 | ok |
| 10 | t(178.2) = -0.4 | p = 0.69 | 0.689636 | ok |
| 10 | t(190.26) = -6.59 | p < 0.001 | 0.0 | ok |
| 10 | t(186.19) = -2.14 | p = 0.03 | 0.033656 | ok |
| 10 | t(185.6) = -2.52 | p = 0.01 | 0.012579 | ok |
| 11 | t(184.97) = 6.76 | p < 0.001 | 0.0 | ok |
| 11 | t(184.42) = 6.69 | p < 0.001 | 0.0 | ok |
| 11 | t(180.45) = 0.01 | p = 0.99 | 0.992032 | ok |
| 11 | t(193.05) = 19.62 | p < 0.001 | 0.0 | ok |
| 11 | t(188.79) = 2.97 | p = 0.003 | 0.003365 | ok |
| 11 | t(188.17) = 2.95 | p = 0.004 | 0.003581 | ok |
| 12 | t(88.4) = -1.97 | p = 0.053 | 0.051969 | ok |
| 12 | t(92.83) = 2.77 | p = 0.001 | 0.00677 | flagged |
| 12 | t(98.18) = 3.62 | p < 0.001 | 0.000468 | ok |
| 12 | t(94.29) = -1.11 | p = 0.27 | 0.269822 | ok |
| 12 | F(3, 181.4) = 6.5 | p < 0.001 | 0.000335 | ok |
| 12 | F(3, 181.45) = 10.38 | p < 0.001 | 2e-06 | ok |
| 13 | t(267) = 0.65 | p = 0.516 | 0.516251 | ok |
| 13 | t(267) = -4.52 | p < 0.001 | 9e-06 | ok |
| 13 | t(100.1) = 2.01 | p = 0.047 | 0.047122 | ok |
| 13 | t(102.86) = 3.15 | p = 0.002 | 0.002138 | ok |
| 14 | t(179.7) = 0.63 | p = 0.53 | 0.529495 | ok |
| 14 | t(179.01) = 1.86 | p = 0.064 | 0.064526 | ok |
| 14 | t(174.07) = 1.23 | p = 0.22 | 0.220357 | ok |
| 14 | t(189.27) = -2.51 | p = 0.013 | 0.012911 | ok |
| 14 | t(183.97) = -3.1 | p = 0.002 | 0.002239 | ok |
| 14 | t(183.23) = -4.29 | p < 0.001 | 2.9e-05 | ok |
| 14 | t(180) = -3.95 | p < 0.001 | 0.000112 | ok |
| 14 | t(179.4) = 0.96 | p = 0.34 | 0.338347 | ok |
| 14 | t(175.16) = 2.93 | p = 0.004 | 0.003841 | ok |
| 14 | t(188.17) = -4.76 | p < 0.001 | 4e-06 | ok |
| 14 | t(183.6) = -0.87 | p = 0.39 | 0.385436 | ok |
| 14 | t(182.95) = -3.72 | p < 0.001 | 0.000265 | ok |
| 15 | t(97.37) = -1.83 | p = 0.07 | 0.070309 | ok |
| 15 | t(99.94) = -3.54 | p < 0.001 | 0.000609 | ok |
| 15 | t(87.59) = -2.92 | p = 0.004 | 0.00445 | ok |
| 15 | t(91.68) = -0.86 | p = 0.39 | 0.392032 | ok |
| 15 | t(89.09) = 2.61 | p = 0.01 | 0.010621 | ok |
| 16 | t(85.11) = 3.02 | p = 0.003 | 0.003336 | ok |
| 16 | t(91.33) = -1.43 | p = 0.16 | 0.156129 | ok |
| 16 | t(87.13) = -3.58 | p < 0.001 | 0.000565 | ok |

## Notes and limitations

This report lists places where a value reported in the paper differs from the value recomputed from other reported numbers. A difference is not evidence of misconduct. Common benign causes are rounding, typos, one-tailed tests, corrections for multiple comparisons, adjusted degrees of freedom, non-integer scales (which make GRIM and GRIMMER inapplicable) and PDF text-extraction errors. Each flag should be read in the paper before drawing any conclusion.

GRIM and GRIMMER assume every score is a whole number and that the N in the same sentence or parenthesis is the N behind that mean; both assumptions fail for averaged multi-item scales, continuous measures and subgroup means. The df vs N check only flags tests whose df imply more participants than the paper mentions anywhere. Duplicated statistics are usually legitimate repetition.
