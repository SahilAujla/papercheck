# papercheck report: bernstein_2018_plosone.pdf

Generated 2026-11-08 with papercheck 0.1.0. 21 pages, 16 test statistics with p values, 35 reported means (0 with a usable N for GRIM).

## Summary

| Check | Items examined | Errors | Warnings | Info |
|---|---:|---:|---:|---:|
| p value recomputation (statcheck style) | 16 | 0 | 0 | 0 |
| GRIM (means of integer data) | 0 | 0 | 0 | 0 |
| GRIMMER (SDs of integer data) | 0 | 0 | 0 | 0 |
| Degrees of freedom vs reported N | 16 | 0 | 0 | 0 |
| Duplicated statistics | 16 | 0 | 0 | 0 |
| Unverifiable statements (ps < .05, statistics without p, p without statistic) | 11 | 0 | 0 | 11 |
| 95% CI vs point estimate | 0 | 0 | 0 | 0 |
| Regression coefficient vs SE and p | 0 | 0 | 0 | 0 |

Total flags: 11 (errors 0, warnings 0, info 11).

Severity: an error is a reported vs recomputed p value on different sides of .05 (the conclusion about significance would change). A warning is a numeric inconsistency that does not change the decision, or a GRIM failure. Info items are worth a look but have common benign explanations.

## Flagged items

### 1. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 7

Reported: `ps>.081`

Sentence: "In not one case did Target Sex or Participant Sex exert a main effect nor any interaction, at any level, with our dependent variables (all Fs<3.06, ps>.081."

'ps>.081' is a blanket p statement covering several tests at once. It cannot be checked against a specific test statistic.

### 2. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 11

Reported: `p < .001`

Sentence: "Our results mostly supported our hypothesis; Fischer's LSD post hoc tests revealed that Exclusion Internal (M = 3.57, SD = 2.25) was the least desirable as an affiliation partner as compared to both Exclusion Control (M = 5.51, SD = 2.13; p < .001) and Exclusion External (M = 4.78, SD = 1.74; p = .004)."

'p < .001' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 3. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 11

Reported: `p = .004`

Sentence: "Our results mostly supported our hypothesis; Fischer's LSD post hoc tests revealed that Exclusion Internal (M = 3.57, SD = 2.25) was the least desirable as an affiliation partner as compared to both Exclusion Control (M = 5.51, SD = 2.13; p < .001) and Exclusion External (M = 4.78, SD = 1.74; p = .004)."

'p = .004' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 4. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 11

Reported: `p>.08`

Sentence: "The latter two conditions, however, did not differ from each other (p>.08)."

'p>.08' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 5. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 12

Reported: `p = .011`

Sentence: "Fischer's LSD post-hoc tests revealed that, consistent with our hypothesis, Exclusion Internal (M = 3.59, SD = 2.32) resulted in the least empathy as compared to both Exclusion Control (M = 5.59, SD = 2.01; p = .011) and Exclusion External (M = 6.28, SD = 1.95; p < .001)."

'p = .011' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 6. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 12

Reported: `p < .001`

Sentence: "Fischer's LSD post-hoc tests revealed that, consistent with our hypothesis, Exclusion Internal (M = 3.59, SD = 2.32) resulted in the least empathy as compared to both Exclusion Control (M = 5.59, SD = 2.01; p = .011) and Exclusion External (M = 6.28, SD = 1.95; p < .001)."

'p < .001' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 7. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 12

Reported: `p = .11`

Sentence: "However, while Exclusion External had descriptively greater empathy than did Exclusion Control, it did not reach conventional levels of significance (p = .11)."

'p = .11' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 8. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 14

Reported: `p = .069`

Sentence: "Model fit was good for this model on all three indices: Chi-square (χ2[1] = 3.32, p = .069), RMSEA (.10, 90% pclose = .150), and CFI (.987)."

'p = .069' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 9. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 17

Reported: `p < .001`

Sentence: "...factors (and included a direct effect from Exclusion to External Attributions) to see if this model was better; in fact, it was a far worse model than our hypothesized one [Chi-square (χ2[1] = 82.36, p < .001), RMSEA (.590, 90%, p-close < .001), and CFI (.548)]...."

'p < .001' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 10. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 17

Reported: `p < .001`

Sentence: "If we run the same path analysis without the direct effect of Exclusion on External Attributions, but with Empathy as the first step which then predicts External Attributions, we again get a model with very poor fit, [Chi-square (χ2[1] = 105.83, p < .001), RMSEA (.471, 90%, p-close < .001), and CFI (.423)]."

'p < .001' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 11. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 17

Reported: `p < .001`

Sentence: "We conducted a final model in which we again reversed Empathy and External Attributions (relative to our hypothesized model), but now, we included a direct effect of Empathy on Desire to Affiliate and removed the direct effect of Exclusion on Attributions, but this was also a poor model [Chi-square (χ2[1] = 23.46, p < .001), RMSEA (.310, 90%, pclose < .001), and CFI (.875)]."

'p < .001' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

## All extracted test statistics

| Page | Statistic | Reported p | Recomputed p | Status |
|---:|---|---|---|---|
| 5 | t(117) = 13.2 | p < 0.001 | 0.0 | ok |
| 5 | t(117) = 6.38 | p < 0.001 | 0.0 | ok |
| 5 | t(117) = 2.22 | p = 0.028 | 0.028346 | ok |
| 7 | t(119) = 12.28 | p < 0.001 | 0.0 | ok |
| 7 | t(119) = 4.46 | p < 0.001 | 1.9e-05 | ok |
| 7 | t(119) = 4.47 | p < 0.001 | 1.8e-05 | ok |
| 9 | t(135) = 14.83 | p < 0.001 | 0.0 | ok |
| 9 | t(135) = 2.61 | p = 0.01 | 0.010076 | ok |
| 9 | t(135) = 3.82 | p < 0.001 | 0.000203 | ok |
| 11 | F(2, 143) = 46.01 | p < 0.001 | 0.0 | ok |
| 11 | F(2, 143) = 11.13 | p < 0.001 | 3.2e-05 | ok |
| 12 | F(2, 143) = 22.05 | p < 0.001 | 0.0 | ok |
| 13 | t(233) = 16.64 | p < 0.001 | 0.0 | ok |
| 13 | t(233) = 6.48 | p < 0.001 | 0.0 | ok |
| 13 | t(223) = 3.08 | p = 0.002 | 0.00233 | ok |
| 14 | t(223) = 6.27 | p < 0.001 | 0.0 | ok |

## Notes and limitations

This report lists places where a value reported in the paper differs from the value recomputed from other reported numbers. A difference is not evidence of misconduct. Common benign causes are rounding, typos, one-tailed tests, corrections for multiple comparisons, adjusted degrees of freedom, non-integer scales (which make GRIM and GRIMMER inapplicable) and PDF text-extraction errors. Each flag should be read in the paper before drawing any conclusion.

GRIM and GRIMMER assume every score is a whole number and that the N in the same sentence or parenthesis is the N behind that mean; both assumptions fail for averaged multi-item scales, continuous measures and subgroup means. The df vs N check only flags tests whose df imply more participants than the paper mentions anywhere. Duplicated statistics are usually legitimate repetition.
