# papercheck report: choi_2024_plosone.pdf

Generated 2026-11-08 with papercheck 0.1.0. 21 pages, 33 test statistics with p values, 68 reported means (0 with a usable N for GRIM).

## Summary

| Check | Items examined | Errors | Warnings | Info |
|---|---:|---:|---:|---:|
| p value recomputation (statcheck style) | 33 | 0 | 1 | 0 |
| GRIM (means of integer data) | 0 | 0 | 0 | 0 |
| GRIMMER (SDs of integer data) | 0 | 0 | 0 | 0 |
| Degrees of freedom vs reported N | 33 | 0 | 0 | 0 |
| Duplicated statistics | 33 | 0 | 0 | 0 |
| Unverifiable statements (ps < .05, statistics without p, p without statistic) | 17 | 0 | 0 | 17 |
| 95% CI vs point estimate | 4 | 0 | 4 | 0 |
| Regression coefficient vs SE and p | 0 | 0 | 0 | 0 |

Total flags: 22 (errors 0, warnings 5, info 17).

Severity: an error is a reported vs recomputed p value on different sides of .05 (the conclusion about significance would change). A warning is a numeric inconsistency that does not change the decision, or a GRIM failure. Info items are worth a look but have common benign explanations.

## Flagged items

### 1. [WARNING] 95% CI vs point estimate, page 9

Reported: `effect of -.1044 (95% CI:-.1718, -.0496`

Sentence: "Competence also had a significant indirect effect of -.1044 (95% CI:-.1718, -.0496)."

Reported effect = -.1044 with CI [-.1718, -.0496]. For a symmetric interval the point estimate should be at the midpoint (-.1718 + -.0496) / 2 = -0.1107, but the reported value is 0.0063 away. The interval may belong to a different estimate, be a bootstrap or otherwise asymmetric interval, or contain a typo.

### 2. [WARNING] 95% CI vs point estimate, page 12

Reported: `effect of -.3862 (95% CI:-.4915, -.2970`

Sentence: "This analysis revealed an indirect effect of -.3862 (95% CI:-.4915, -.2970) for prosociality, indicating a significant indirect effect."

Reported effect = -.3862 with CI [-.4915, -.2970]. For a symmetric interval the point estimate should be at the midpoint (-.4915 + -.2970) / 2 = -0.3942, but the reported value is 0.0081 away. The interval may belong to a different estimate, be a bootstrap or otherwise asymmetric interval, or contain a typo.

### 3. [WARNING] 95% CI vs point estimate, page 12

Reported: `effect of -.0803 (95% CI:-.1314, -.0345`

Sentence: "Competence also had a significant indirect effect of -.0803 (95% CI:-.1314, -.0345)."

Reported effect = -.0803 with CI [-.1314, -.0345]. For a symmetric interval the point estimate should be at the midpoint (-.1314 + -.0345) / 2 = -0.0829, but the reported value is 0.0026 away. The interval may belong to a different estimate, be a bootstrap or otherwise asymmetric interval, or contain a typo.

### 4. [WARNING] p value recomputation (statcheck style), page 15

Reported: `t(184.671) = 2.781, p = .036`

Sentence: "However, among targets described as being highly prosocial, while targets described as having a high desire for status were given less status (M = 5.00, 95% CI [4.78, 5.22]) than targets described as having a low desire for status (M = 5.42, 95% CI [5.22, 5.63], t(184.671) = 2.781, p = .036, d = .406), this difference was much smaller than among targets with unknown prosocial tendencies."

Reported t(184.671) = 2.781, p = .036. Recomputed p = 0.0060 (range 0.0060 to 0.0060 given rounding of the test statistic) does not match the reported p. The significance decision is unchanged.

Recomputed p = 0.005981 (interval [0.005972, 0.00599]); consistent if one-tailed: False; decision error: False.

### 5. [WARNING] 95% CI vs point estimate, page 16

Reported: `effect of -.1275 (95% CI:-.1974, -.0657`

Sentence: "Perceived competence also had a significant indirect effect of -.1275 (95% CI:-.1974, -.0657)."

Reported effect = -.1275 with CI [-.1974, -.0657]. For a symmetric interval the point estimate should be at the midpoint (-.1974 + -.0657) / 2 = -0.1316, but the reported value is 0.0040 away. The interval may belong to a different estimate, be a bootstrap or otherwise asymmetric interval, or contain a typo.

### 6. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 5

Reported: `p = .016`

Sentence: "In one-way ANOVAs, we found coworkers with the highest perceived desire for status were afforded significantly less status (M = 4.46, 95% CI = [4.20, 4.72]) than coworkers with a moderate desire for status (M = 4.92, 95% CI = [4.67, 5.17], p = .016), and coworkers with the lowest desire for status (M = 4.93, 95% CI = [4.70, 5.16], p = .007)."

'p = .016' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 7. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 5

Reported: `p = .007`

Sentence: "In one-way ANOVAs, we found coworkers with the highest perceived desire for status were afforded significantly less status (M = 4.46, 95% CI = [4.20, 4.72]) than coworkers with a moderate desire for status (M = 4.92, 95% CI = [4.67, 5.17], p = .016), and coworkers with the lowest desire for status (M = 4.93, 95% CI = [4.70, 5.16], p = .007)."

'p = .007' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 8. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 5

Reported: `p = .999`

Sentence: "There were no significant differences between coworkers in the lowest third and the coworkers in the middle third, p = .999."

'p = .999' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 9. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 8

Reported: `p < .001`

Sentence: "Participants rated targets described as high in the desire for status (M = 4.29, 95% CI [4.15, 4.42]) as less prosocial than targets described as high in the desire for achievement (M = 5.22, 95% CI [5.09, 5.35], p < .001), and control targets (M = 5.63, 95% CI [5.50, 5.76], p < .001)."

'p < .001' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 10. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 8

Reported: `p < .001`

Sentence: "Participants rated targets described as high in the desire for status (M = 4.29, 95% CI [4.15, 4.42]) as less prosocial than targets described as high in the desire for achievement (M = 5.22, 95% CI [5.09, 5.35], p < .001), and control targets (M = 5.63, 95% CI [5.50, 5.76], p < .001)."

'p < .001' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 11. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 9

Reported: `p < .001`

Sentence: "Participants rated targets described as high in the desire for status (M = 5.87, 95% CI [5.81, 5.92]) as less competent than targets described as high in the desire for achievement (M = 6.28, 95% CI [6.23, 6.33], p < .001), and control targets (M = 6.19, 95% CI [6.14, 6.24], p < .001)."

'p < .001' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 12. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 9

Reported: `p < .001`

Sentence: "Participants rated targets described as high in the desire for status (M = 5.87, 95% CI [5.81, 5.92]) as less competent than targets described as high in the desire for achievement (M = 6.28, 95% CI [6.23, 6.33], p < .001), and control targets (M = 6.19, 95% CI [6.14, 6.24], p < .001)."

'p < .001' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 13. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 12

Reported: `p < .001`

Sentence: "Targets described as desiring status for selfish reasons (M = 3.61, 95% CI [3.41, 3.80]) were seen as being significantly less prosocial than targets described as desiring status for prosocial reasons (M = 4.38, 95% CI [4.19, 4.58], p < .001), or the control targets (M = 5.13, 95% CI [4.94, 5.33], p < .001)."

'p < .001' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 14. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 12

Reported: `p < .001`

Sentence: "Targets described as desiring status for selfish reasons (M = 3.61, 95% CI [3.41, 3.80]) were seen as being significantly less prosocial than targets described as desiring status for prosocial reasons (M = 4.38, 95% CI [4.19, 4.58], p < .001), or the control targets (M = 5.13, 95% CI [4.94, 5.33], p < .001)."

'p < .001' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 15. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 12

Reported: `p < .001`

Sentence: "The difference between the targets desiring status for prosocial reasons and the control targets was also significant, p < .001."

'p < .001' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 16. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 12

Reported: `p < .001`

Sentence: "Targets described as desiring status for selfish reasons (M = 5.36, 95% CI [5.16, 5.56]) were seen as being significantly less competent when compared to targets in the control condition (M = 5.89, 95% CI [5.69, 6.10], p < .001)."

'p < .001' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 17. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 12

Reported: `p = .074`

Sentence: "However, targets described as desiring status for selfish reasons and targets described as desiring status for prosocial reasons (M = 5.62, 95% CI [5.42, 5.82]) were not significantly different in their competence ratings, p = .074."

'p = .074' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 18. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 12

Reported: `p = .063`

Sentence: "The competence ratings for the targets desiring status for prosocial reasons and the control condition did not significantly differ either, p = .063."

'p = .063' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 19. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 16

Reported: `p < .001`

Sentence: "Replicating the negative effect of desire for status on prosociality perceptions, targets described as having a strong desire for status (M = 4.23, 95% CI [4.10, 4.36]) were seen as significantly less prosocial than targets described as having a weak desire for status (M = 5.34, 95% CI [5.21, 5.47], p < .001)."

'p < .001' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 20. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 16

Reported: `p < .001`

Sentence: "As expected and serving as a manipulation check, targets described as being highly prosocial (M = 5.07, 95% CI [4.94, 5.20]) were seen as being significantly more prosocial than targets who were not (M = 4.50, 95% CI [4.37, 4.63], p < .001)."

'p < .001' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 21. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 16

Reported: `p < .001`

Sentence: "Similarly, targets described as having a strong desire for status (M = 5.48, 95% CI [5.36, 5.60]) were seen as significantly less competent than targets described as having a weak desire for status (M = 5.85, 95% CI [5.72, 5.97], p < .001)."

'p < .001' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

### 22. [INFO] Unverifiable statements (ps < .05, statistics without p, p without statistic), page 16

Reported: `p < .001`

Sentence: "Targets described as being highly prosocial (M = 5.87, 95% CI [5.75, 6.00]) were seen as being significantly more competent than targets who were not (M = 5.45, 95% CI [5.33, 5.57], p < .001)."

'p < .001' is a p value without a test statistic in the same sentence, so it cannot be recomputed.

## All extracted test statistics

| Page | Statistic | Reported p | Recomputed p | Status |
|---:|---|---|---|---|
| 4 | t(131.49) = -2.602 | p = 0.01 | 0.010331 | ok |
| 4 | t(121.89) = -7.629 | p < 0.001 | 0.0 | ok |
| 4 | t(122.3) = -1.772 | p = 0.079 | 0.078885 | ok |
| 4 | t(133.04) = -3.021 | p = 0.003 | 0.003022 | ok |
| 5 | t(419.65) = -3.918 | p < 0.001 | 0.000104 | ok |
| 5 | t(99.77) = -3.235 | p = 0.002 | 0.00165 | ok |
| 6 | t(192.24) = -4.194 | p < 0.001 | 4.2e-05 | ok |
| 6 | t(207.29) = -10.92 | p < 0.001 | 0.0 | ok |
| 6 | t(240.43) = -3.497 | p < 0.001 | 0.00056 | ok |
| 6 | t(945.66) = 3.074 | p = 0.002 | 0.002173 | ok |
| 6 | t(966) = -6.327 | p < 0.001 | 0.0 | ok |
| 6 | t(958) = -2.26 | p = 0.024 | 0.024045 | ok |
| 6 | t(196.26) = -4.316 | p < 0.001 | 2.5e-05 | ok |
| 6 | t(530.6) = -1.78 | p = 0.076 | 0.075648 | ok |
| 6 | t(136.06) = -5.99 | p < 0.001 | 0.0 | ok |
| 8 | F(2, 600) = 71.6 | p < 0.001 | 0.0 | ok |
| 8 | t(341.723) = 9.527 | p < 0.001 | 0.0 | ok |
| 8 | t(319.664) = 9.538 | p < 0.001 | 0.0 | ok |
| 8 | F(2, 600) = 0.475 | p = 0.622 | 0.622119 | ok |
| 8 | F(2, 600) = 2.095 | p = 0.124 | 0.12397 | ok |
| 8 | F(2, 600) = 2.27 | p = 0.104 | 0.104199 | ok |
| 8 | F(2, 600) = 106.868 | p < 0.001 | 0.0 | ok |
| 8 | F(2, 600) = 16.993 | p < 0.001 | 0.0 | ok |
| 11 | F(2, 294) = 26.745 | p < 0.001 | 0.0 | ok |
| 12 | F(2, 294) = 57.463 | p < 0.001 | 0.0 | ok |
| 12 | F(2, 294) = 6.583 | p = 0.002 | 0.001597 | ok |
| 14 | t(367.565) = 6.514 | p < 0.001 | 0.0 | ok |
| 15 | t(378.927) = 4.701 | p < 0.001 | 4e-06 | ok |
| 15 | F(1, 383) = 8.668 | p = 0.003 | 0.003436 | ok |
| 15 | t(185.835) = 6.588 | p < 0.001 | 0.0 | ok |
| 15 | t(184.671) = 2.781 | p = 0.036 | 0.005981 | flagged |
| 15 | F(1, 383) = 8.526 | p = 0.004 | 0.003708 | ok |
| 15 | F(1, 383) = 5.412 | p = 0.021 | 0.02052 | ok |

## Notes and limitations

This report lists places where a value reported in the paper differs from the value recomputed from other reported numbers. A difference is not evidence of misconduct. Common benign causes are rounding, typos, one-tailed tests, corrections for multiple comparisons, adjusted degrees of freedom, non-integer scales (which make GRIM and GRIMMER inapplicable) and PDF text-extraction errors. Each flag should be read in the paper before drawing any conclusion.

GRIM and GRIMMER assume every score is a whole number and that the N in the same sentence or parenthesis is the N behind that mean; both assumptions fail for averaged multi-item scales, continuous measures and subgroup means. The df vs N check only flags tests whose df imply more participants than the paper mentions anywhere. Duplicated statistics are usually legitimate repetition.
