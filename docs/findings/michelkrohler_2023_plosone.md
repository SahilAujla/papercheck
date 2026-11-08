# michelkrohler_2023_plosone, page 14 (Table 4), two F-test p values: reported vs recomputed

## Citation and licence

Michel-Kröhler, A., Wessa, M., and Berti, S. (2023). Experimental induction of state rumination: A study evaluating the efficacy of goal-cueing task in different experimental settings. PLOS ONE, 18(11), e0288450. https://doi.org/10.1371/journal.pone.0288450. Licence: CC BY 4.0 (article page links creativecommons.org/licenses/by/4.0/; no CC0 or public-domain statement). Local copy: `data/michelkrohler_2023_plosone.pdf` (34 pages).

## The reported cells

Both items are table cells in Table 4 on page 14 of the PDF (PDF index 13). Table 4 lists, for each experiment and dependent variable, the condition effect, the time effect and the interaction effect of the mixed ANOVAs, each as an F-statistic with p and a separate partial eta-squared column.

Item 4 in `examples/SUMMARY.md` (Exp. 1a, Mood, Valence, Interaction effect column):

> F(1,162) = 2.37, p = .12 | .01

Item 5 in `examples/SUMMARY.md` (Exp. 1c, State Rumination, Ruminative self-focus, Condition effect column):

> F(2,56) = 3.55, p = .03 | .11

In both cases the value after the p is the partial eta-squared column, not part of the p value. The extraction in SUMMARY.md read the cells correctly.

## Commands run

```
/Users/sahil/code/papercheck/.venv/bin/python -c "import pymupdf; print(pymupdf.open('/Users/sahil/code/papercheck/data/michelkrohler_2023_plosone.pdf')[13].get_text())"
/Users/sahil/code/papercheck/.venv/bin/python -c "from scipy import stats; print(stats.f.sf(2.37,1,162), stats.f.sf(3.55,2,56))"
/Users/sahil/code/papercheck/.venv/bin/python -c "from scipy import stats; print(stats.f.sf(2.375,1,162), stats.f.sf(2.365,1,162), stats.f.sf(3.555,2,56), stats.f.sf(3.545,2,56))"
```

A whole-PDF search for "Bonferroni", "Holm", "FDR", "false discovery", "one-tailed", "one tailed", "directional", "Greenhouse", "corrected" and "adjusted" found:

- Greenhouse-Geisser: the Methods state that a Greenhouse-Geisser correction was applied to ANOVAs when Mauchly's test indicated a sphericity violation. This cannot explain either cell. Item 4 is an interaction with a two-level within-subject factor (df1 = 1), where epsilon is 1 and the correction changes nothing. Item 5 is a between-subjects condition effect (3 groups, df1 = 2), to which sphericity corrections do not apply. In any case the printed df are integers, so no correction was applied to these cells.
- Bonferroni: the Methods say Bonferroni-adjusted p values were reported for simple main effect analyses that followed significant interactions. The two cells here are omnibus ANOVA effects, not simple main effects, and a Bonferroni adjustment would make p larger, not smaller, so it cannot move .126 to .12 or .035 to .03.
- No one-tailed or directional test is stated.

## Comparison

F tests are one-sided by construction (the upper tail of the F distribution), so "one-tailed" and "two-tailed" are the same quantity; the one-tailed column is given only because the task template asks for it.

| Item | Reported | Recomputed (upper tail of F) | Interval for F rounded to 2 dp | Corrected |
|---|---|---|---|---|
| 4: Exp. 1a Valence interaction | F(1,162) = 2.37, p = .12 | p = 0.1256 | 0.1252 to 0.1260 | not applicable (see above) |
| 5: Exp. 1c Ruminative self-focus condition | F(2,56) = 3.55, p = .03 | p = 0.0354 | 0.0352 to 0.0355 | not applicable (see above) |

Rounding: F is printed to two decimals and p to two decimals. For item 4 every F that rounds to 2.37 gives p in [0.1252, 0.1260], all of which round to .13; the printed .12 is what truncating 0.1256 to two decimals gives. For item 5 every F that rounds to 3.55 gives p in [0.0352, 0.0355], all of which round to .04; the printed .03 is what truncating 0.0354 gives. Both printed values are off by exactly one unit in the last place in the direction of truncation.

## Plausible benign explanations

1. Truncation instead of rounding when transferring p values from software output (which typically shows three decimals, .126 and .035) into a two-decimal table. The same pattern appears in SUMMARY.md item 6 on page 15 of this paper (p = .975 printed as .97), which supports a systematic truncation habit rather than two independent errors.
2. The F statistics were themselves rounded from values slightly below the printed ones in a way that, combined with rounding of p, happened to land one unit low. The intervals above show this is not possible for either cell: no F that rounds to 2.37 or 3.55 yields a p that rounds to .12 or .03.
3. The table p values were computed from slightly different df (for example with a few more participants after a different exclusion rule) than the printed df. Item 5 would need df2 of roughly 70 or more at F = 3.55 to reach p = .03; item 4 would need an F of about 2.45 at df (1,162) to reach p = .12.

## What would settle it

The trial-level data behind Table 4 (per-participant valence scores at both time points in Exp. 1a, and ruminative self-focus scores by condition in Exp. 1c), or the ANOVA output tables from the analysis software, which would show the p values to three or more decimals and confirm whether .126 and .035 were truncated.

## Conclusion

Both items are numerical reported vs recomputed discrepancies of one unit in the second decimal: F(1,162) = 2.37 gives p = 0.126, printed as .12, and F(2,56) = 3.55 gives p = 0.035, printed as .03. Neither the stated Greenhouse-Geisser correction nor the stated Bonferroni adjustment applies to these cells, and no one-tailed test is stated. The significance conclusion does not change for either: item 4 is non-significant under both the reported and recomputed value, and item 5 is significant at the .05 level under both (.03 and .035). No inference about the authors' conduct is made or implied; the pattern is consistent with truncating three-decimal software output to two decimals.
