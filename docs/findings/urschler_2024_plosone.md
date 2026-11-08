# urschler_2024_plosone: hand verification of triage items 12 and 14

## Source

- Citation: Urschler, D. F., Fischer, P., and Kessler, T. (2024). Standing-up against moral violations: The predicting role of attribution, kinship, and severity. PLOS ONE, 19(8), e0307740.
- DOI URL: https://doi.org/10.1371/journal.pone.0307740 (checked 2026-11-08)
- Licence: CC BY 4.0 (article page links creativecommons.org/licenses/by/4.0/; no CC0 or public-domain statement)
- PDF: /Users/sahil/code/papercheck/data/urschler_2024_plosone.pdf
- Verified by hand on 2026-11-08 against the PDF text extracted with pymupdf.

## Reported sentences

Item 12, page 7 (Study 1, Results):

> "Neither the Severity by Kinship interaction, F(1, 278) = 2.65, p = .073, nor the Severity by Responsibility interaction, F(1, 278) = 2.10, p = .150, was significant (see Fig 1)."

Item 14, page 9 (Study 2, Results):

> "Neither the Severity by Kinship interaction, F(1, 334) = 0.85, p = .427, nor the Responsibility by Kinship interaction, F(1, 334) = 1.01, p = .316, was significant."

Both sentences sit in the paragraph that follows the simple-effect analyses of the Responsibility by Severity interaction and precede the three-way interaction test. In both studies the surrounding tests (for example F(1, 278) = 2.10, p = .150 and F(1, 334) = 1.01, p = .316) recompute correctly, so the discrepancy is specific to the Severity by Kinship cell in each study.

## Commands run

Page text (page index is page number minus one):

```
/Users/sahil/code/papercheck/.venv/bin/python -c "import pymupdf; print(pymupdf.open('/Users/sahil/code/papercheck/data/urschler_2024_plosone.pdf')[6].get_text())"
/Users/sahil/code/papercheck/.venv/bin/python -c "import pymupdf; print(pymupdf.open('/Users/sahil/code/papercheck/data/urschler_2024_plosone.pdf')[8].get_text())"
```

Recomputation (scipy 1.x, F distribution survival function; the one-tailed value is p/2, which is the directional t test with t = sqrt(F) for a 1-df numerator; the rounding interval uses F plus or minus 0.005):

```
/Users/sahil/code/papercheck/.venv/bin/python -c "
from scipy import stats
for F,df1,df2 in ((2.65,1,278),(0.85,1,334)):
    p=stats.f.sf(F,df1,df2)
    print(F,df1,df2,'two-tailed',round(p,4),'one-tailed',round(p/2,4),
          'Bonf k=2',round(min(1,2*p),4),'Bonf k=3',round(min(1,3*p),4),
          'interval',round(stats.f.sf(F+0.005,df1,df2),4),round(stats.f.sf(F-0.005,df1,df2),4))
print('F for p=.073 at (1,278):',stats.f.isf(0.073,1,278))
print('F for p=.427 at (1,334):',stats.f.isf(0.427,1,334))
"
```

Search of the whole PDF for a stated correction or directional test:

```
/Users/sahil/code/papercheck/.venv/bin/python -c "
import pymupdf,re
d=pymupdf.open('/Users/sahil/code/papercheck/data/urschler_2024_plosone.pdf')
for i,pg in enumerate(d):
    for m in re.finditer(r'(?i)(one[- ]tailed|two[- ]tailed|bonferroni|holm|fdr|false discovery|greenhouse|geisser|corrected|adjust\w*|directional)',pg.get_text()):
        print(i+1,m.group(0))
"
```

Result: the only hit is the word "corrected" on page 11, which belongs to a different study and does not refer to a p value adjustment for these ANOVA terms. No one-tailed test, Bonferroni, Holm, FDR or Greenhouse-Geisser correction is stated on pages 7 or 9 or in the Methods sections.

## Comparison table

| Item | Page | Reported | Recomputed two-tailed | Recomputed one-tailed (p/2) | Rounding interval of F (p) | Bonferroni k=2 / k=3 | F that would give the reported p |
|---|---|---|---|---|---|---|---|
| 12 | 7 | F(1, 278) = 2.65, p = .073 | .1047 | .0523 | .1044 to .1050 | .209 / .314 | 3.24 |
| 14 | 9 | F(1, 334) = 0.85, p = .427 | .3572 | .1786 | .3558 to .3586 | .714 / 1.000 | 0.63 |

Rounding notes: both F values are printed to two decimals and both p values to three decimals. The reported p lies outside the rounding interval of F in both cases (item 12 by about .031, item 14 by about .070), so rounding of the printed statistic cannot account for either gap. Neither a one-tailed reading nor a Bonferroni multiplication (k = 2 or 3, the number of two-way interaction terms tested) lands on the reported value for either item. Greenhouse-Geisser does not apply: these are between-subjects factors with df1 = 1, and the printed df are integers.

## Plausible benign explanations

1. A transcription slip when copying from software output. For item 12, p = .073 corresponds to F about 3.24 at these df; for item 14, p = .427 corresponds to F about 0.63. Either the F or the p in each cell may have been copied from a neighbouring row of an ANOVA table (for example a different interaction term, or the same term from a model with or without a covariate).
2. The F and p may come from two different model specifications (for example Type II vs Type III sums of squares, or a model fitted before and after a data exclusion), with only one of the two numbers updated in the text.
3. For item 12, the reported p = .073 is close to, but not equal to, the one-tailed value (.052). A directional test is not stated anywhere in the paper, and .052 is not .073, so this is not a one-tailed reporting match; it is noted only because the gap is in that direction.
4. The denominator df (278 and 334) match the other tests on the same pages and are consistent with the reported sample sizes, so a wrong df is not the likely source.

## What would settle it

- The trial-level data (willingness-to-intervene scores with the Severity, Responsibility and Kinship codes) for Studies 1 and 2, which would allow the ANOVA to be refitted and the Severity by Kinship term read directly.
- The analysis script or the software output (SPSS, R or JASP ANOVA table) from which the sentences were typed, which would show whether the F or the p is the transcribed value.
- The PLOS ONE data availability statement for this article should point to the deposited data; checking that deposit is the next step and was not done here because of time.

## Classification

Both items are a numerical reported vs recomputed discrepancy: the p value printed next to the F statistic and df does not equal the p value those numbers imply, and the gap is not explained by rounding of the printed statistic, by a one-tailed test, or by any multiple-comparison or sphericity correction stated in the paper. In both cases the reported and recomputed p values are above .05, so the significance conclusion drawn in the text (the interaction is not significant) does not change. This note describes a mismatch between printed numbers only; no inference about the authors' conduct is made or implied, and the most likely cause is an ordinary transcription error between software output and manuscript.
