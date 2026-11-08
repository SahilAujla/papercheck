# gill_2023_plosone, page 12, compassion t-test: reported vs recomputed

## Citation and licence

Gill, M. J., and Zungu, S. P. (2023). What do other people think he deserves? Social influence on utilization of mitigating information regarding a violent offender's unfortunate life history. PLOS ONE, 18(11), e0291729. https://doi.org/10.1371/journal.pone.0291729. Licence: CC BY 4.0 (article page links creativecommons.org/licenses/by/4.0/; no CC0 or public-domain statement). Local copy: `data/gill_2023_plosone.pdf` (22 pages).

## The reported sentence

Page 12 of the PDF (PDF index 11), Results, paragraph describing the path model with juries as the unit of analysis (Fig 3):

> As already noted, moral outrage was lower in the narrative-affirm history condition than in narrative-neutral, t(88.40) = -1.97, p = .053. And, compassion was higher in narrative-affirm history than in narrative-neutral, t(92.83) = 2.77, p = .001. Furthermore, moral outrage was positively related to malicious punishment intentions, t(98.18) = 3.62, p < .001, whereas compassion was not related to malicious punishment intentions, t(94.29) = -1.11, p = .27.

Item 2 in `examples/SUMMARY.md`. The fractional df (92.83) indicates a Welch or Satterthwaite-type approximation; the df is used as printed.

## Commands run

```
/Users/sahil/code/papercheck/.venv/bin/python -c "import pymupdf; print(pymupdf.open('/Users/sahil/code/papercheck/data/gill_2023_plosone.pdf')[11].get_text())"
/Users/sahil/code/papercheck/.venv/bin/python -c "from scipy import stats; p2=2*stats.t.sf(2.77,92.83); print(p2, p2/2)"
/Users/sahil/code/papercheck/.venv/bin/python -c "from scipy import stats; print(2*stats.t.sf(2.775,92.83), 2*stats.t.sf(2.765,92.83))"
```

A whole-PDF search for "Bonferroni", "Holm", "FDR", "false discovery", "one-tailed", "one tailed", "directional", "Greenhouse", "corrected" and "adjusted" found no statement of a multiple-comparison correction or a one-tailed test anywhere in the paper. The only hit for "corrected" is in the literature review (jurors' errors being corrected by other jurors) and is unrelated.

## Comparison

| Quantity | Value |
|---|---|
| Reported | t(92.83) = 2.77, p = .001 |
| Recomputed two-tailed | p = 0.0068 |
| Recomputed one-tailed | p = 0.0034 |
| Two-tailed interval for t in [2.765, 2.775) | 0.0067 to 0.0069 |
| Corrected (Bonferroni etc.) | not applicable; no correction is stated, and any correction would make p larger, not smaller |

Rounding: the t is printed to two decimals and the p to three. Every value of t that rounds to 2.77 gives a two-tailed p between 0.0067 and 0.0069, which prints as .007 (or .01 at two decimals). The printed .001 is outside that interval by a factor of about seven. The one-tailed reading (0.0034) does not reach .001 either. Reaching p = .001 at df = 92.83 would need t of about 3.4.

## Plausible benign explanations

1. A typographical slip: ".001" for ".007" (one digit), or a carried-over "p < .001" from the neighbouring moral-outrage path (t(98.18) = 3.62, p < .001) in the same sentence sequence.
2. The t and p come from different model runs or different software output (for example an earlier model specification whose t was larger), with only one of them updated during revision.
3. The p belongs to a different parameterisation of the same effect in the multilevel model (for example a Wald test on a different scale), while the t and df were taken from the printed path coefficient output.

None of these can be distinguished from the PDF alone.

## What would settle it

The jury-level data (compassion score per jury in the narrative-affirm history and narrative-neutral conditions) or the model output (the lme4, SPSS or Mplus listing for the Fig 3 path model). Re-running the compassion contrast would show whether t = 2.77 with p about .007 is the correct pair, or whether the t is the typo.

## Conclusion

This is a numerical reported vs recomputed discrepancy: the printed p (.001) does not follow from the printed t (2.77) and df (92.83), which give a two-tailed p of 0.0068 and a one-tailed p of 0.0034, and no stated correction or one-tailed test in the paper maps one onto the other. The significance conclusion does not change: the effect is below the conventional .05 threshold under either the reported or the recomputed value, so the paper's claim that compassion was higher in the narrative-affirm history condition stands as written. No inference about the authors' conduct is made or implied; the most likely cause is a typing or transcription error in one digit.
