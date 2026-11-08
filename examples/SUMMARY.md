# papercheck evidence base: 13 PLOS ONE papers

papercheck 0.1.0, run 2026-11-08. Every flag is a difference between a value reported in the paper and a value
recomputed from other reported numbers. A difference is not evidence of misconduct; papers are referred to by file
slug. "Means (with usable N)" is the number of M (SD) pairs extracted and, in parentheses, how many had a sample size
the GRIM and GRIMMER checks could use.

| Paper | Pages | Test statistics | Means (usable N) | Errors | Warnings | Info |
|---|---:|---:|---:|---:|---:|---:|
| bernstein_2018 | 21 | 16 | 35 (0) | 0 | 0 | 11 |
| buchanan_2023 | 26 | 35 | 0 (0) | 0 | 1 | 3 |
| choi_2024 | 21 | 33 | 68 (0) | 0 | 1 | 21 |
| drake_2023 | 24 | 27 | 6 (2) | 0 | 0 | 4 |
| gill_2023 | 22 | 48 | 9 (0) | 0 | 3 | 10 |
| maj_2024 | 19 | 23 | 168 (7) | 0 | 0 | 6 |
| makanju_2024 | 34 | 28 | 31 (7) | 0 | 1 | 19 |
| michelkrohler_2023 | 34 | 86 | 458 (7) | 0 | 6 | 24 |
| moyal_2020 | 16 | 26 | 22 (11) | 0 | 0 | 1 |
| takahashi_2023 | 16 | 23 | 35 (0) | 0 | 4 | 4 |
| takayama_2023 | 22 | 18 | 52 (0) | 0 | 9 | 27 |
| urschler_2024 | 17 | 25 | 18 (0) | 0 | 6 | 2 |
| yan_2018 | 24 | 30 | 59 (11) | 0 | 1 | 41 |
| Total (13 papers) | 296 | 418 | 961 (45) | 0 | 32 | 173 |

Counts regenerated at 04:05 EST after the phase 2 fixes (value comparator bounds, table-cell n, df vs N design wording, sample-size regex) and after the unverifiable, CI symmetry and regression checks were added. Warnings by check: ci_symmetry 1 (four bootstrap mediation intervals downgraded to info at 04:08), df_vs_n 14, grim 1, p_recompute 16. Info by check: df_vs_n 8, duplicate 2, grim 9, grimmer 1, unverifiable 149. The triage below was written against the pre-fix reports; the flags it names as extraction mistakes (urschler t(334) < 0.01; michelkrohler 9.42 (3.02)) and the 22 df vs N warnings are the ones the fixes removed or downgraded.


Warnings by check: p_recompute 17, df_vs_n 22, grim 1. Info by check: grim 9, grimmer 1, duplicate 2.

## Triage of every error-level flag

There are no flags with severity "error" in any of the 13 JSON reports. Every p value, GRIM and GRIMMER discrepancy was
graded warning or info because none changes a significance decision and none is impossible under the stated N.

## Triage of the p_recompute warnings (sample of 15 out of 17)

Seventeen p_recompute warnings were produced in total, so a sample of 15 was triaged. The two left out are
michelkrohler_2023_plosone page 14, F(2,56) = 1.92, p = .15 (recomputed .156) and urschler_2024_plosone page 7,
F(1, 278) = 2.10, p = .150 (recomputed .148); both are rounding near-misses of the same kind as items 4 and 10 below.
Each item was read on the PDF page with pymupdf. "True inconsistency" means the numbers as printed do not agree,
not that anything is wrong with the study.

1. choi_2024_plosone, page 15. Reported "t(184.671) = 2.781, p = .036" (sentence: "...targets described as having a
   low desire for status (M = 5.42, 95% CI [5.22, 5.63], t(184.671) = 2.781, p = .036, d = .406)..."). Recomputed
   p = .0060. Likely benign cause: a corrected p. The recomputed value times 6 is .036, which is what a Bonferroni
   adjustment over the six pairwise comparisons of a 2 x 3 design would give, although the page does not name the
   correction. The Welch df is already used in the recomputation.
2. gill_2023_plosone, page 12. Reported "t(92.83) = 2.77, p = .001" (sentence: "compassion was higher in
   narrative-affirm history than in narrative-neutral, t(92.83) = 2.77, p = .001."). Recomputed p = .0068. True
   inconsistency: no one-tailed reading (.0034) or correction maps .0068 onto .001. Reads like a typo for .007; the
   decision is unchanged.
3. makanju_2024_plosone, page 24. Reported "F(3, 240) = 0.08, p = .974" (sentence: "...a null interaction effect of
   the subjective importance of African history and historical representations, lambda = 1.00, F(3, 240) = 0.08,
   p = .974, eta-p2 = .001."). Recomputed p = .971 (interval .968 to .973 for the rounding of F). Likely benign
   cause: this is an approximate F from Wilks' lambda printed to two decimals; with F this small the printed p sits
   just outside the rounding interval.
4. michelkrohler_2023_plosone, page 14 (Table 4). Reported "F(1,162) = 2.37, p = .12" (table cell; the next cell,
   ".01", is the eta-p2 column). Recomputed p = .126. True inconsistency, trivial: .126 rounds to .13, so .12 looks
   like truncation rather than rounding. Decision unchanged. The extraction itself was correct.
5. michelkrohler_2023_plosone, page 14 (Table 4). Reported "F(2,56) = 3.55, p = .03" (table cell for ruminative
   self-focus, Exp. 1c). Recomputed p = .0354. True inconsistency, trivial: same truncation pattern (.0354 rounds to
   .04). Decision unchanged.
6. michelkrohler_2023_plosone, page 15. Reported "F(2,36) = 0.02, p = .97" (sentence: "participants in the three
   conditions did not significantly differ in their level of trait rumination, F(2,36) = 0.02, p = .97, eta-p2 <
   .01."). Recomputed p = .980 (interval .975 to .985). Likely benign cause: F printed to two decimals when the true
   F is near zero; .97 is what truncating .975 gives.
7. michelkrohler_2023_plosone, page 25. Reported "F(1,201) = 2.70, p = .11" (sentence: "...but not for time,
   F(1,201) = 2.70, p = .11, eta-p2 = .01."). Recomputed p = .102. True inconsistency, small (.102 would print as
   .10). Decision unchanged.
8. takahashi_2023_plosone, page 9. Reported "F(2, 296) = 5.12, p = .004" (sentence: "we found an unexpected
   condition x gender interaction effect, F(2, 296) = 5.12, p = .004, eta-p2 = .036."). Recomputed p = .0065. True
   inconsistency, small. Decision unchanged.
9. takahashi_2023_plosone, page 10. Reported "r(286) = .15, p = .037" (sentence: "once the literary fiction
   condition was removed, the correlation between fiction reading time and FS became significant, r(286) = .15,
   p = .037."). Recomputed p = .011. True inconsistency as printed: r = .15 gives p = .037 only for about n = 194,
   so either the df or the p for this subsample does not match the other. The other correlations on the page use
   r(378). Decision unchanged.
10. urschler_2024_plosone, page 7. Reported "t(278) = 1.02, p = .312" (sentence: "responsibility did not
    significantly affect people's willingness to intervene ... t(278) = 1.02, p = .312."). Recomputed p = .309
    (interval .306 to .311). Likely benign cause: rounding of t (the printed p is .001 outside the interval) or a
    Welch test printed with the pooled df.
11. urschler_2024_plosone, page 7. Reported "t(278) = -0.91, p = .358" (sentence: "...responsible: M = 6.41,
    SD = 0.72, t(278) = -0.91, p = .358)."). Recomputed p = .364 (interval .361 to .366). Likely benign cause: the two
    SDs (1.25 and 0.72) are very unequal, so a Welch test with the pooled df printed is plausible; otherwise rounding.
12. urschler_2024_plosone, page 7. Reported "F(1, 278) = 2.65, p = .073" (sentence: "Neither the Severity by
    Kinship interaction, F(1, 278) = 2.65, p = .073, nor ... was significant"). Recomputed p = .105. True
    inconsistency, small; a one-tailed reading (.052) does not match either. Decision unchanged.
13. urschler_2024_plosone, page 9. Reported "t(334) < 0.01, p = .999" (sentence: "...responsible: M = 6.02,
    SD = 1.12, t(334) < 0.01, p = .999)."). Recomputed p = .992 at t = 0.01. Extraction mistake: the "<" comparator
    on the test statistic was treated as "=". With t < 0.01 the p is greater than .992, so .999 is consistent and no
    flag should be raised.
14. urschler_2024_plosone, page 9. Reported "F(1, 334) = 0.85, p = .427" (sentence: "Neither the Severity by
    Kinship interaction, F(1, 334) = 0.85, p = .427, nor the Responsibility by Kinship interaction, F(1, 334) = 1.01,
    p = .316, was significant."). Recomputed p = .357. True inconsistency, small. Decision unchanged.
15. yan_2018_plosone, page 18. Reported "chi2(1, N = 89) = 5.00, p = 0.042" (sentence: "The effect of mindset
    switching was significant, chi2(1, N = 89) = 5.00, p = 0.042."). Recomputed p = .025. Likely benign cause: a
    continuity-corrected or Fisher's exact p reported next to the uncorrected chi-square.

Counts: true inconsistency 8 (items 2, 4, 5, 7, 8, 9, 12, 14), likely benign cause 6 (items 1, 3, 6, 10, 11, 15),
extraction mistake 1 (item 13). Five of the eight true inconsistencies (4, 5, 7, 8, 14) differ from the recomputed
value by .01 or less at the printed precision, and none changes a significance decision.

Not triaged item by item: the 22 df_vs_n warnings and the one grim warning. The df_vs_n warnings that were read
(takayama pages 6, 10, 14, 17; makanju pages 9 to 11; urschler page 14; takahashi pages 10 and 11) are all cases
where the df legitimately exceeds the largest extracted N: repeated-measures F with df2 = (k - 1)(n - 1), one-sample
t on pooled observations (87 = 29 participants x 3 days), Wilks' lambda approximate F, or analyses pooling two
studies (290 + 346 = 636, hence t(634)). They are check-logic false positives rather than extraction mistakes.

## Estimated false-positive rate

Over the 15 triaged p_recompute flags: extraction mistakes 1 of 15 (6.7 percent); benign causes 6 of 15 (40 percent);
numbers that really do not agree as printed 8 of 15 (53 percent). Including the one grim warning (an extraction
mistake, bug 2 below) gives 2 extraction mistakes out of 16 triaged flags (12.5 percent). If the 22 df_vs_n warnings
are counted as false positives of the check logic, 24 of the 40 warnings in the evidence base (60 percent) would be
removed by the fixes listed below, leaving 16 warnings of which 8 are small reported-versus-recomputed disagreements.

## Extraction bugs found

1. Comparator on the test statistic is dropped. urschler_2024_plosone, page 9: "t(334) < 0.01, p = .999". The
   statistic was recomputed as if t = 0.01 (p = .992) and the reported .999 was flagged. Correct parse:
   value_comparator "<", recomputed p is a lower bound (p > .992), and a reported p above that bound is consistent.
   The same applies to table cells like "F(1,162) < 1" in michelkrohler page 14, which are currently (correctly)
   skipped but should stay skipped once "<" is handled.
2. Wrong n attached to a table mean for GRIM. michelkrohler_2023_plosone, page 6, Table (Exp. 1c row): the text
   runs "n = 20 (f = 14, m = 6) n = 19 (f = 13, m = 6) n = 20 (f = 14, m = 6) ... RSQ-B .77 9.70 (2.99) [8.30, 11.10]
   9.42 (3.02) [7.96, 10.88] 9.60 (2.64) [8.36, 10.83]". The mean 9.42 (3.02) is the second column (n = 19;
   9.42 x 19 = 178.98, which passes GRIM) but it was tested with n = 20 (188.4, flagged as a warning). Correct
   parse: either map table columns to the n of the same column or do not attach an n to means inside a table block
   (the four michelkrohler grim info flags on pages 6 and 14 have the same table origin and should be rechecked).
3. df_vs_n raises on designs where df2 is not bounded by N - 1. takayama_2023_plosone, page 6: "F (2, 56) = 1.84"
   and "t (86) = 5.99" with 29 participants measured on 3 days (13 flags in that paper alone); makanju_2024_plosone,
   page 9: "F(6, 1156) = 22.09" introduced by "Using Wilks' lambda" with N = 584; urschler_2024_plosone, page 14:
   "t(634) = 1.08" pooling two studies of 290 and 346; takahashi_2023_plosone, page 10: "F(3, 400) = 1.02" after
   "the new data were combined with the original Study 2 data". Correct behaviour: suppress or downgrade to info when
   the sentence mentions repeated measures, within-subject, days or sessions, Wilks' lambda or MANOVA, or combining
   studies, or when df2 is an integer multiple of (N - 1) for some extracted N.
4. Sample-size extractor captures numbers that are not participant counts. makanju_2024_plosone, page 23:
   "016 with participants" parsed as n = 16 (the digits are the tail of a longer number); urschler_2024_plosone,
   page 11: "2 revealed that people" parsed as n = 2 (it is "Study 2 revealed..."); gill_2023_plosone, page 7:
   "twelve", "three", "two" parsed as sample sizes from a sentence about group sizes. Correct parse: require the
   number to be followed directly by a participant noun (participants, students, adults, women, men, undergraduates)
   or to appear as "N =" / "n =", and ignore a number that is preceded by a digit, a decimal point or the word
   "Study".
5. Unit-of-analysis mismatch in df_vs_n. gill_2023_plosone, page 13: "t(267) = .65" is flagged against the largest
   extracted N of 192 because the paper reports "jury (N = 192) as the unit of analysis" while this t test uses
   individual participants. Not fixable by regex alone; the flag text should say which N it compared against (it
   does) and the check should prefer the largest N anywhere in the paper over the nearest one.
6. Sentence boundaries inside hyphenated line breaks. makanju_2024_plosone, page 24: the flagged sentence starts
   "up ANOVA main effects of..." because "follow-\nup" was split at the hyphen. Cosmetic, but the sentence shown in
   the report should join "follow-up".

Working as intended and worth a regression test: michelkrohler_2023_plosone, page 14, the table text
"F(1,162) = 2.37, p = .12\n.01" was parsed as p = .12 with the eta-p2 cell ".01" left alone; and
buchanan_2023_plosone produced 0 means from 10 "SD =" occurrences because all of them are table notes reading
"SD = Standard Deviation", which is the correct outcome.
