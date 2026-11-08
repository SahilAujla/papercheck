# Example paper sources

Three open-access PLOS ONE papers used as papercheck examples. All three are empirical,
multi-study psychology experiments that report APA-style inferential statistics in the
running text, with means and standard deviations in parentheses. PDFs live in `data/`
(gitignored) and were downloaded from the PLOS "printable" endpoint:
`https://journals.plos.org/plosone/article/file?id=<DOI>&type=printable`.

Verification command (counts are: APA test-statistic openers matching `[tFr](\d`, then `SD =` occurrences):

```
.venv/bin/python -c "import pymupdf,re,sys; t=''.join(p.get_text() for p in pymupdf.open(sys.argv[1])); print(len(re.findall(r'[tFr]\s*\(\s*\d', t)), len(re.findall(r'SD\s*=', t)))" data/<file>.pdf
```

## 1. yan_2018_plosone.pdf

- Citation: Yan, J., Zhang, N.-N., and Xu, D.-X. (2018). Mindset switching increases the use of 'want-based' over 'should-based' behaviors. PLOS ONE, 13(4), e0196269.
- DOI URL: https://doi.org/10.1371/journal.pone.0196269 (checked 2026-11-08)
- Licence: CC BY 4.0 (Creative Commons Attribution License, stated in the article's copyright line)
- Verification counts: 29 test statistics, 64 `SD =` occurrences
- Notes: four experiments, per-study N between 87 and 139, 7-point Likert-type measures, F and t tests with means and SDs in text. Good GRIM target.

## 2. bernstein_2018_plosone.pdf

- Citation: Bernstein, M. J., Chen, Z., Poon, K.-T., Benfield, J. A., and Ng, H. K. S. (2018). Ostracized but why? Effects of attributions and empathy on connecting with the socially excluded. PLOS ONE, 13(8), e0201183.
- DOI URL: https://doi.org/10.1371/journal.pone.0201183 (checked 2026-11-08)
- Licence: CC BY 4.0 (Creative Commons Attribution License, stated in the article's copyright line)
- Verification counts: 19 test statistics, 35 `SD =` occurrences
- Notes: four studies, N of 128 and 146 reported, rating-scale measures of attributions, empathy and desire to affiliate; t tests, ANOVAs and a path analysis (chi-square, RMSEA, CFI).

## 3. moyal_2020_plosone.pdf

- Citation: Moyal, A., and Ritov, I. (2020). The effect of contest participation and contest outcome on subsequent prosocial behavior. PLOS ONE, 15(11), e0240712.
- DOI URL: https://doi.org/10.1371/journal.pone.0240712 (checked 2026-11-08)
- Licence: CC BY 4.0 (Creative Commons Attribution License, stated in the article's copyright line)
- Verification counts: 27 test statistics, 40 `SD =` occurrences
- Notes: several experiments on prosocial giving after contests; conditions of roughly 116 to 123 participants, with pooled analyses up to N = 357 (t and F tests, means and SDs in text). Larger total N than the other two, so GRIM on pooled means is less informative, but per-condition means remain checkable.

## Rejected candidates (for the record)

- Hayran, Anik and Gurhan-Canli (2020), 10.1371/journal.pone.0232318: strong counts (32, 46) but released under CC0, not CC BY, so excluded by the licence requirement.
- Xie et al. (2020), 10.1371/journal.pone.0236748: counts 14, 21, just under the preferred 15.
- Davies et al. (2018), 10.1371/journal.pone.0207343: counts 22, 1, almost no SDs in text.
- Gao et al. (2019), 10.1371/journal.pone.0225757: counts 15, 15, but several studies with N above 200.
- Christy et al. (2016), Rudzinska-Wojciechowska (2017), Blake et al. (2020), Park and Shin (2017), Denne et al. (2021), Erlandsson et al. (2020), Ostermaier and Uhl (2017), Huang et al. (2020), Weigand and Jacobsen (2021): first count below 15.

## Summary of the three runs (papercheck 0.1.0, 2026-11-08)

Every flag below is a difference between a value reported in the paper and a value recomputed from other reported
numbers. None of them is evidence of misconduct; the benign explanations listed in each report apply.

| Paper | Test statistics | Means (with usable N) | Errors | Warnings | Info |
|---|---:|---:|---:|---:|---:|
| Yan, Zhang and Xu 2018 | 30 | 59 (11) | 0 | 1 | 4 |
| Bernstein et al. 2018 | 16 | 35 (0) | 0 | 0 | 0 |
| Moyal and Ritov 2020 | 26 | 22 (11) | 0 | 0 | 0 |

- Yan 2018, page 18: reported χ2(1, N = 89) = 5.00, p = 0.042; recomputed p = 0.025 for an uncorrected chi-square with
  1 df. The significance decision does not change. A continuity-corrected test or Fisher's exact test on the same 2 x 2
  table would give a different p, so the discrepancy may simply be a difference in which statistic and which p were
  reported together. The remaining 29 p values in the paper match recomputation.
- Yan 2018, page 18: four GRIM info flags on subgroup means (for example M = 5.68) that were tested against the study
  N of 89 because no subgroup n was available in the text. With the correct subgroup n they may well be possible.
  Treat these as a coverage note, not a finding.
- Bernstein 2018: all 16 p values match. An earlier version of the extractor flagged the df of t(233) and t(223)
  against a largest reported N of 146; the paper gives its Study 4 sample as "Two-hundred and thirty-five", which is
  now parsed, and the flags were withdrawn.
- Moyal 2020: all 26 p values match; 11 means with SDs pass GRIM and GRIMMER with the stated group or study Ns.

## Ten additional papers (added 2026-11-08)

Selected with the PLOS search API (journal PLOS ONE, subject Psychology, research articles, 2015 to 2024, body containing `SD =` and a second study or experiment),
downloaded from the printable endpoint, kept when the PDF was over 100 KB and the first verification count was at least 15, and the article page
linked the CC BY 4.0 licence. Reports for these ten are in this directory and were produced by the same papercheck 0.1.0 run.

## 4. michelkrohler_2023_plosone.pdf

- Citation: Michel-Kröhler, A., Wessa, M., and Berti, S. (2023). Experimental induction of state rumination: A study evaluating the efficacy of goal-cueing task in different experimental settings. PLOS ONE, 18(11), e0288450.
- DOI URL: https://doi.org/10.1371/journal.pone.0288450 (checked 2026-11-08)
- Licence: CC BY 4.0 (article page links creativecommons.org/licenses/by/4.0/; no CC0 or public-domain statement)
- Verification counts: 110 test statistics, 19 `SD =` occurrences; 34 pages, 930 KB

## 5. gill_2023_plosone.pdf

- Citation: Gill, M. J., and Zungu, S. P. (2023). What do other people think he deserves? Social influence on utilization of mitigating information regarding a violent offender's unfortunate life history. PLOS ONE, 18(11), e0291729.
- DOI URL: https://doi.org/10.1371/journal.pone.0291729 (checked 2026-11-08)
- Licence: CC BY 4.0 (article page links creativecommons.org/licenses/by/4.0/; no CC0 or public-domain statement)
- Verification counts: 47 test statistics, 9 `SD =` occurrences; 22 pages, 1092 KB

## 6. makanju_2024_plosone.pdf

- Citation: Makanju, D., Livingstone, A. G., Sweetman, J., Okafor, C. O., and Attoh, F. (2024). How appraisals of an in-group's collective history shape collective identity and action: Evidence in relation to African identity. PLOS ONE, 19(9), e0308727.
- DOI URL: https://doi.org/10.1371/journal.pone.0308727 (checked 2026-11-08)
- Licence: CC BY 4.0 (article page links creativecommons.org/licenses/by/4.0/; no CC0 or public-domain statement)
- Verification counts: 39 test statistics, 31 `SD =` occurrences; 34 pages, 1335 KB

## 7. choi_2024_plosone.pdf

- Citation: Choi, A. L., and Anderson, C. (2024). Be careful what you wish for: Individuals perceived to desire status are afforded less status. PLOS ONE, 19(6), e0304727.
- DOI URL: https://doi.org/10.1371/journal.pone.0304727 (checked 2026-11-08)
- Licence: CC BY 4.0 (article page links creativecommons.org/licenses/by/4.0/; no CC0 or public-domain statement)
- Verification counts: 36 test statistics, 6 `SD =` occurrences; 21 pages, 1287 KB

## 8. buchanan_2023_plosone.pdf

- Citation: Buchanan, K., and Sandstrom, G. M. (2023). Buffering the effects of bad news: Exposure to others' kindness alleviates the aversive effects of viewing others' acts of immorality. PLOS ONE, 18(5), e0284438.
- DOI URL: https://doi.org/10.1371/journal.pone.0284438 (checked 2026-11-08)
- Licence: CC BY 4.0 (article page links creativecommons.org/licenses/by/4.0/; no CC0 or public-domain statement)
- Verification counts: 29 test statistics, 10 `SD =` occurrences; 26 pages, 1043 KB

## 9. maj_2024_plosone.pdf

- Citation: Maj, A., Matynia, M., Michalak, N., Bis, A., and Andersson, G. (2024). New in Town: An internet-based self-efficacy intervention for internal migrants: A randomized controlled trial. PLOS ONE, 19(3), e0299638.
- DOI URL: https://doi.org/10.1371/journal.pone.0299638 (checked 2026-11-08)
- Licence: CC BY 4.0 (article page links creativecommons.org/licenses/by/4.0/; no CC0 or public-domain statement)
- Verification counts: 26 test statistics, 16 `SD =` occurrences; 19 pages, 797 KB

## 10. takahashi_2023_plosone.pdf

- Citation: Takahashi, Y., Himichi, T., Masuchi, A., Nakanishi, D., and Ohtsubo, Y. (2023). Is reading fiction associated with a higher mind-reading ability? Two conceptual replication studies in Japan. PLOS ONE, 18(6), e0287542.
- DOI URL: https://doi.org/10.1371/journal.pone.0287542 (checked 2026-11-08)
- Licence: CC BY 4.0 (article page links creativecommons.org/licenses/by/4.0/; no CC0 or public-domain statement)
- Verification counts: 26 test statistics, 4 `SD =` occurrences; 16 pages, 937 KB

## 11. urschler_2024_plosone.pdf

- Citation: Urschler, D. F., Fischer, P., and Kessler, T. (2024). Standing-up against moral violations: The predicting role of attribution, kinship, and severity. PLOS ONE, 19(8), e0307740.
- DOI URL: https://doi.org/10.1371/journal.pone.0307740 (checked 2026-11-08)
- Licence: CC BY 4.0 (article page links creativecommons.org/licenses/by/4.0/; no CC0 or public-domain statement)
- Verification counts: 25 test statistics, 18 `SD =` occurrences; 17 pages, 1030 KB

## 12. drake_2023_plosone.pdf

- Citation: Drake, A. C., and Sears, C. R. (2023). Do humour styles moderate the association between hopelessness and suicide ideation? A comparison of student and community samples. PLOS ONE, 18(12), e0295995.
- DOI URL: https://doi.org/10.1371/journal.pone.0295995 (checked 2026-11-08)
- Licence: CC BY 4.0 (article page links creativecommons.org/licenses/by/4.0/; no CC0 or public-domain statement)
- Verification counts: 23 test statistics, 2 `SD =` occurrences; 24 pages, 1019 KB

## 13. takayama_2023_plosone.pdf

- Citation: Takayama, A., and Sekiya, H. (2023). Effects of various sitting and standing postures on arousal and valence. PLOS ONE, 18(6), e0286720.
- DOI URL: https://doi.org/10.1371/journal.pone.0286720 (checked 2026-11-08)
- Licence: CC BY 4.0 (article page links creativecommons.org/licenses/by/4.0/; no CC0 or public-domain statement)
- Verification counts: 21 test statistics, 4 `SD =` occurrences; 22 pages, 2414 KB
