# papercheck report: drake_2023_plosone.pdf

Generated 2026-11-08 with papercheck 0.1.0. 24 pages, 27 test statistics with p values, 6 reported means (2 with a usable N for GRIM).

## Summary

| Check | Items examined | Errors | Warnings | Info |
|---|---:|---:|---:|---:|
| p value recomputation (statcheck style) | 27 | 0 | 0 | 0 |
| GRIM (means of integer data) | 2 | 0 | 0 | 0 |
| GRIMMER (SDs of integer data) | 0 | 0 | 0 | 0 |
| Degrees of freedom vs reported N | 27 | 0 | 0 | 0 |
| Duplicated statistics | 27 | 0 | 0 | 0 |
| Unverifiable statements (ps < .05, statistics without p, p without statistic) | 4 | 0 | 0 | 4 |
| 95% CI vs point estimate | 0 | 0 | 0 | 0 |
| Regression coefficient vs SE and p | 0 | 0 | 0 | 0 |

Total flags: 4 (errors 0, warnings 0, info 4).

Severity: an error is a reported vs recomputed p value on different sides of .05 (the conclusion about significance would change). A warning is a numeric inconsistency that does not change the decision, or a GRIM failure. Info items are worth a look but have common benign explanations.

## Flagged items

### 1. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 9

Reported: `p < .001`

Sentence: "Suicide ideation -.43** -.01.23** .37** .37** - Mean 37.99 36.72 28.65 32.18 7.04 1.99 Standard Deviation 9.15 8.01 7.44 9.90 5.32 2.70 Hopelessness = BHS total, Suicide ideation = HDSQ-SS total. **p < .001. https://doi.org/10.1371/journal.pone.0295995.t003 PLOS ONE Humour styles as a moderator between hopelessness and suicide ideation PLOS ONE | https://doi.org/10.1371/journal.pone.0295995 Decemb..."

'p < .001' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 2. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 10

Reported: `p < .01`

Sentence: "Suicide ideation .00 -.19.12.39** .54** - Mean 44.48 33.65 25.64 30.15 5.64 1.18 Standard Deviation 6.96 8.13 6.42 9.91 4.61 1.97 Hopelessness = BHS total, Suicide ideation = HDSQ-SS total. *p < .01. **p < .001. https://doi.org/10.1371/journal.pone.0295995.t004 PLOS ONE Humour styles as a moderator between hopelessness and suicide ideation PLOS ONE | https://doi.org/10.1371/journal.pone.0295995 De..."

'p < .01' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 3. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 10

Reported: `p < .001`

Sentence: "...icide ideation .00 -.19.12.39** .54** - Mean 44.48 33.65 25.64 30.15 5.64 1.18 Standard Deviation 6.96 8.13 6.42 9.91 4.61 1.97 Hopelessness = BHS total, Suicide ideation = HDSQ-SS total. *p < .01. **p < .001. https://doi.org/10.1371/journal.pone.0295995.t004 PLOS ONE Humour styles as a moderator between hopelessness and suicide ideation PLOS ONE | https://doi.org/10.1371/journal.pone.0295995 Dece..."

'p < .001' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 4. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 18

Reported: `p = .050`

Sentence: "We noted that although this moderation effect was not statistically significant (p = .050) in the community sample (despite the larger sample size), the trend in the data was identical, which could indicate that these associations are present but weaker."

'p = .050' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

## All extracted test statistics

| Page | Statistic | Reported p | Recomputed p | Status |
|---:|---|---|---|---|
| 7 | t(514.32) = 33.64 | p < 0.001 | 0.0 | ok |
| 7 | chi2(1) = 64.98 | p < 0.001 | 0.0 | ok |
| 8 | chi2(1) = 56.25 | p < 0.001 | 0.0 | ok |
| 8 | chi2(2) = 305.42 | p < 0.001 | 0.0 | ok |
| 8 | chi2(5) = 300.74 | p < 0.001 | 0.0 | ok |
| 10 | F(2, 421) = 68.6 | p < 0.001 | 0.0 | ok |
| 11 | F(1, 420) = 0.97 | p = 0.326 | 0.325247 | ok |
| 11 | F(2, 165) = 35.33 | p < 0.001 | 0.0 | ok |
| 11 | F(1, 164) = 2.93 | p = 0.089 | 0.088838 | ok |
| 11 | F(2, 421) = 37.38 | p < 0.001 | 0.0 | ok |
| 12 | F(1, 420) = 10.51 | p = 0.001 | 0.001282 | ok |
| 12 | t(420) = 4.23 | p < 0.001 | 2.9e-05 | ok |
| 12 | t(420) = 2.89 | p = 0.004 | 0.004052 | ok |
| 12 | t(420) = 0.06 | p = 0.954 | 0.952184 | ok |
| 12 | F(2, 165) = 33.7 | p < 0.001 | 0.0 | ok |
| 13 | F(1, 164) = 1.89 | p = 0.171 | 0.171077 | ok |
| 14 | F(2, 421) = 43.56 | p < 0.001 | 0.0 | ok |
| 14 | F(1, 420) = 4.11 | p = 0.043 | 0.043261 | ok |
| 14 | F(2, 165) = 33.82 | p < 0.001 | 0.0 | ok |
| 14 | F(1, 164) = 1.0 | p = 0.319 | 0.318784 | ok |
| 15 | F(2, 421) = 59.32 | p < 0.001 | 0.0 | ok |
| 15 | F(1, 420) = 3.88 | p = 0.05 | 0.049521 | ok |
| 15 | F(2, 165) = 38.21 | p < 0.001 | 0.0 | ok |
| 15 | F(1, 164) = 12.76 | p < 0.001 | 0.000465 | ok |
| 15 | t(164) = 0.71 | p = 0.481 | 0.478712 | ok |
| 16 | t(164) = 4.92 | p < 0.001 | 2e-06 | ok |
| 16 | t(164) = 7.33 | p < 0.001 | 0.0 | ok |

## Notes and limitations

This report lists places where a value reported in the paper differs from the value recomputed from other reported numbers. A difference is not evidence of misconduct. Common benign causes are rounding, typos, one-tailed tests, corrections for multiple comparisons, adjusted degrees of freedom, non-integer scales (which make GRIM and GRIMMER inapplicable) and PDF text-extraction errors. Each flag should be read in the paper before drawing any conclusion.

GRIM and GRIMMER assume every score is a whole number and that the N in the same sentence or parenthesis is the N behind that mean; both assumptions fail for averaged multi-item scales, continuous measures and subgroup means. The df vs N check only flags tests whose df imply more participants than the paper mentions anywhere. Duplicated statistics are usually legitimate repetition.
