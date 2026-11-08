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
