# michelkrohler_2023_plosone, item 7: F(1,201) = 2.70, p = .11 (page 25)

## Source

- Citation: Michel-Kröhler, A., Wessa, M., and Berti, S. (2023). Experimental induction of state rumination: A study evaluating the efficacy of goal-cueing task in different experimental settings. PLOS ONE, 18(11), e0288450.
- DOI URL: https://doi.org/10.1371/journal.pone.0288450
- Licence: CC BY 4.0 (article page links creativecommons.org/licenses/by/4.0/; no CC0 or public-domain statement)
- PDF: /Users/sahil/code/papercheck/data/michelkrohler_2023_plosone.pdf, page 25

## Reported sentence (page 25, verbatim)

"Finally, results of the 4 x 2 ANOVA for calmness indicated a significant effect for condition, F(3,201) = 3.04, p = .03, ηp2 = .04, and for the time x condition interaction, F(3,201) = 6.77, p < .001, ηp2 = .09, but not for time, F(1,201) = 2.70, p = .11, ηp2 = .01."

The statistic is the main effect of time (2 levels: before vs after the goal-cueing task) in a 4 (condition) x 2 (time) mixed ANOVA on calmness.

## Commands run

```
cd /Users/sahil/code/papercheck
.venv/bin/python -c "import pymupdf; t=pymupdf.open('data/michelkrohler_2023_plosone.pdf')[24].get_text(); i=t.find('2.70'); print(t[i-700:i+200])"
.venv/bin/python -c "
from scipy import stats
p=stats.f.sf(2.70,1,201); print(p, stats.f.sf(2.695,1,201), stats.f.sf(2.705,1,201), p/2, 2*p)
print(stats.f.isf(.11,1,201), 2.7/203.7)"
# search for stated corrections or tails anywhere in the PDF
.venv/bin/python -c "import pymupdf,re; d=pymupdf.open('data/michelkrohler_2023_plosone.pdf')
for i,pg in enumerate(d):
  t=pg.get_text()
  for m in re.finditer(r'(?i)(bonferroni|holm|false discovery|FDR|greenhouse|one-tailed|one-sided|two-tailed|two-sided|multiple comparison)',t): print(i+1, t[m.start()-80:m.end()+80])"
```

## Reported vs recomputed

| Quantity | Reported | Recomputed | Note |
|---|---|---|---|
| p, two-tailed F(1,201) = 2.70 | .11 | .1019 | F rounding interval [2.695, 2.705) gives p in [.1016, .1022]; every value in it prints as .10 |
| p, one-tailed equivalent (t = sqrt(F), one-sided) | .11 | .0510 | does not match |
| p, Bonferroni k = 2 (two time levels) | .11 | .204 | does not match |
| p, Greenhouse-Geisser | .11 | not applicable | time has 2 levels, so df = 1 and epsilon = 1; no correction possible |
| F that would give p = .11 at (1, 201) | 2.70 | 2.58 | |
| eta-p2 from F = 2.70, df (1, 201) | .01 | .0133 | consistent with the printed F |

Rounding: F is printed to two decimals, p to two decimals. The printed p is .01 above the top of the rounding interval of F, so rounding of F alone does not account for it.

## What the paper states about corrections and tails

- Page 10: Greenhouse-Geisser correction is applied when Mauchly's test indicates a sphericity violation. It cannot apply here (df = 1).
- Pages 22 and 24 to 25: Bonferroni-adjusted p values (printed as "pbonf") are used for simple main effects and pairwise comparisons only. The omnibus effects in the same sentence (condition, time x condition) are printed as plain "p", and a k = 2 adjustment gives .20, not .11.
- No one-tailed or one-sided test is stated anywhere in the PDF.

## Plausible benign explanations

- A transcription slip in p (.10 typed as .11), or in F (2.58 typed as 2.70); eta-p2 = .01 is consistent with either F, so it does not discriminate.
- The F and the p were copied from different model runs (for example with and without a covariate, or from the GG-corrected and uncorrected output tables in JASP or SPSS, which print the same p when df = 1 but could differ if the rows were misaligned).
- A rounding chain: the software printed p = .102, which was later rounded up by hand.

## What would settle it

The trial-level calmness ratings (4 conditions x 2 time points, N = 205) or the analysis output file. One ANOVA on the deposited data would show whether F = 2.70 and p = .10, or F = 2.58 and p = .11, is the correct pair.

## Classification

This is a numerical reported vs recomputed discrepancy: reported p = .11, recomputed p = .102 (which prints as .10). No stated correction or one-tailed test in the paper explains it. The significance conclusion does not change: the time main effect is nonsignificant at alpha = .05 under either value, and the authors describe it as nonsignificant. No inference about the authors' conduct is made or implied; a one-digit difference of this size is consistent with an ordinary transcription or rounding slip.
