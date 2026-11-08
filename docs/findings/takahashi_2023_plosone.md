# takahashi_2023_plosone, items 8 and 9 (pages 9 and 10)

## Source

- Citation: Takahashi, Y., Himichi, T., Masuchi, A., Nakanishi, D., and Ohtsubo, Y. (2023). Is reading fiction associated with a higher mind-reading ability? Two conceptual replication studies in Japan. PLOS ONE, 18(6), e0287542.
- DOI URL: https://doi.org/10.1371/journal.pone.0287542
- Licence: CC BY 4.0 (article page links creativecommons.org/licenses/by/4.0/; no CC0 or public-domain statement)
- PDF: /Users/sahil/code/papercheck/data/takahashi_2023_plosone.pdf

## What the paper states about corrections and tails

A full-text search of the PDF for Bonferroni, Holm, FDR, false discovery, Greenhouse, one-tailed, one-sided, two-tailed, two-sided and multiple comparison found a single hit, on page 3: the power analysis assumed "significance level = .05 [two-sided]". No multiple-comparison correction and no one-tailed test is stated anywhere in the paper, including on pages 9 and 10.

## Commands run

```
cd /Users/sahil/code/papercheck
.venv/bin/python -c "import pymupdf; d=pymupdf.open('data/takahashi_2023_plosone.pdf'); t=d[8].get_text(); i=t.find('5.12'); print(t[i-900:i+500]); t=d[9].get_text(); i=t.find('286'); print(t[i-1200:i+500])"
.venv/bin/python -c "
from scipy import stats; import numpy as np
p=stats.f.sf(5.12,2,296); print(p, stats.f.sf(5.115,2,296), stats.f.sf(5.125,2,296), .004/p)
F=.036*296/(2*(1-.036)); print(F, stats.f.sf(F,2,296), 10.24/(10.24+296), stats.f.isf(.004,2,296))
for r in (.145,.15,.155):
  df=286; t=r*np.sqrt(df/(1-r*r)); p2=2*stats.t.sf(t,df); print(r,t,p2,p2/2)
for n in range(100,400):
  df=n-2; t=.15*np.sqrt(df/(1-.15**2)); p2=2*stats.t.sf(t,df)
  if abs(p2-.037)<.0008: print('two-tailed match',n,df,p2)
  if abs(p2/2-.037)<.0008: print('one-tailed match',n,df,p2/2)
tc=stats.t.isf(.037/2,286); print(tc/np.sqrt(286+tc*tc))"
```

---

## Item 8: F(2, 296) = 5.12, p = .004 (page 9)

### Reported sentence (verbatim)

"This 3 (condition) × 2 (gender) ANOVA with ΔRMET as the dependent variable again revealed a nonsignificant effect of condition, F(2, 296) = 1.47, p = .232, ηp2 = .010. Although the effect of gender was not significant, F(1, 296) = 0.001, p = .977, ηp2 < .001, we found an unexpected condition × gender interaction effect, F(2, 296) = 5.12, p = .004, ηp2 = .036."

### Reported vs recomputed

| Quantity | Reported | Recomputed | Note |
|---|---|---|---|
| p, F(2, 296) = 5.12 | .004 | .0065 | F rounding interval [5.115, 5.125) gives p in [.0065, .0065]; prints as .006 or .007, never .004 |
| p, one-tailed | .004 | not applicable | an F test with 2 numerator df has no one-tailed form |
| p, corrected | .004 | not applicable | .004 / .0065 = 0.61; a correction can only make p larger, so no Bonferroni, Holm or FDR factor produces .004 |
| eta-p2 from F = 5.12, df (2, 296) | .036 | .0334 | prints as .033, not .036 |
| F implied by eta-p2 = .036 | 5.12 | 5.53 | eta-p2 = F * df1 / (F * df1 + df2) |
| p at F = 5.53, df (2, 296) | .004 | .0044 | prints as .004 |
| F implied by p = .004 | 5.12 | 5.63 | |

Rounding: F to two decimals, p to three decimals, eta-p2 to three decimals. The reported p and eta-p2 are mutually consistent with F of about 5.5 (eta-p2 = .036 gives F = 5.53, p = .0044). The printed F = 5.12 is the one value that disagrees with the other two.

### Plausible benign explanations

- A single-digit transcription slip in F (for example 5.52 or 5.53 typed as 5.12). This is the simplest account, because both the printed p and the printed eta-p2 point to F near 5.5.
- The F was taken from a different model (for example Type I vs Type III sums of squares, or a model with a covariate) than the p and eta-p2.

### What would settle it

The participant-level ΔRMET, condition and gender data for Study 2 (N = 302 in the three conditions), or the ANOVA output. One run of the 3 x 2 ANOVA gives F, p and eta-p2 together.

### Classification

This is a numerical reported vs recomputed discrepancy: reported p = .004, recomputed p = .0065 from the printed F and df. No stated correction or one-tailed test in the paper explains it, and the F test has no one-tailed version. The significance conclusion does not change: the interaction is significant at alpha = .05 and at alpha = .01 under either value, and the authors treat it as significant. No inference about the authors' conduct is made or implied; the internal agreement between p and eta-p2 points to a transcription slip in the F value.

---

## Item 9: r(286) = .15, p = .037 (page 10)

### Reported sentence (verbatim)

"Even FS was not significantly correlated with fiction reading time, r(378) = .09, p = .094. We suspect that this attenuated correlation may be due to the experimental manipulation. [...] Although this is mere speculation, it should be noted that once the literary fiction condition was removed, the correlation between fiction reading time and FS became significant, r(286) = .15, p = .037."

Context: the full Study 2 sample gives r(378), that is N = 380 (three conditions of about 100 plus an additional 100 no-task participants). Removing the literary fiction condition (about 94 participants) leaves about 288, so df = 286 is consistent with the described subsample. The analysis is a Pearson correlation of log10 fiction reading time with the IRI Fantasy (FS) subscale.

### Reported vs recomputed

| Quantity | Reported | Recomputed | Note |
|---|---|---|---|
| p, two-tailed, r = .15, df = 286 | .037 | .0108 | t = 2.566 |
| p, two-tailed, r rounding interval [.145, .155) | .037 | .0084 to .0138 | the reported p is outside the whole interval |
| p, one-tailed | .037 | .0054 | does not match |
| p times k (Bonferroni) | .037 | k = 3.43 | not an integer; k = 3 gives .032, k = 4 gives .043 |
| n at which r = .15 gives p = .037 two-tailed | n = 288 | n = 193 to 195 (df 191 to 193) | |
| n at which r = .15 gives p = .037 one-tailed | n = 288 | n = 142 to 144 | |
| r that gives p = .037 at df = 286 | .15 | .123 | prints as .12 |
| check: r for p = .011 at df = 286 | | .150 | the recomputed p is self-consistent |

Rounding: r to two decimals, p to three decimals. No rounding of r at df = 286 reaches p = .037.

### Plausible benign explanations

- A transcription slip in r (.12 typed as .15) or in p (.011 typed as .037). Either alone resolves the inconsistency.
- The p came from a different procedure than the Pearson r printed beside it, for example a Spearman correlation, a partial correlation controlling for condition, or a bootstrap or permutation p, while the r is the Pearson value.
- The df and the r/p pair came from different subsamples (the SUMMARY.md triage noted that n of about 194 would reconcile r = .15 with p = .037; the paper does not describe a subsample of that size, and df = 286 matches the stated removal of one condition from N = 380, so the df is the value most consistent with the text).
- The reported p is adjusted for some number of tests not stated in the paper; no integer k reproduces .037 exactly, so this is the least likely of the benign accounts.

### What would settle it

The Study 2 participant-level data (condition, log10 fiction reading time, IRI subscale scores) or the analysis script. Recomputing the correlation on the no-task, nonfiction and calculation participants would show which of r, df or p is misprinted.

### Classification

This is a numerical reported vs recomputed discrepancy: reported p = .037, recomputed two-tailed p = .011 (one-tailed .005) from the printed r and df. The paper states two-sided testing and no correction, so neither explains the difference. The significance conclusion does not change: the correlation is significant at alpha = .05 under either value, and the authors describe it as significant (though as "mere speculation" in context). No inference about the authors' conduct is made or implied; a mismatch of this kind among three printed numbers is consistent with a single transcription slip.
