from papercheck.extract import extract_means, extract_sample_sizes, extract_stats
from papercheck.pdf import load_text, normalize, sentence_at

TXT = """Participants were 120 undergraduates (N = 120). The effect was significant, t(38) = 2.14, p = .039, d = 0.69.
Anxiety differed by group, F(2, 87) = 4.21, MSE = 2.10, p < .05, ηp2 = .09. The correlation was r(58) = .32, p = .012.
Gender was unrelated, χ2(1, N = 120) = 0.53, p = .47. Also t(40) = −1.05, ns. Finally, z = 2.58, p < .01.
Also t(22) = 2.5, 95% CI [0.1, 0.9], p = .02 and F(1, 50) = 3.9, p = 0.054, and t(10)=1.0,p=.34; chi-square(2) = 7.1, p < .05.
The mean score (M = 3.42, SD = 1.10, n = 23) exceeded the control (M = 2.9, SD = 1.3)."""


def _by_kind(stats):
    out = {}
    for s in stats:
        out.setdefault(s.kind, []).append(s)
    return out


def test_extracts_all_kinds():
    stats = extract_stats(load_text(TXT))
    kinds = _by_kind(stats)
    assert len(kinds["t"]) == 4
    assert len(kinds["F"]) == 2
    assert len(kinds["chi2"]) == 2
    assert len(kinds["r"]) == 1
    assert len(kinds["z"]) == 1


def test_t_fields_and_p_formats():
    stats = _by_kind(extract_stats(load_text(TXT)))
    t1 = stats["t"][0]
    assert (t1.df1, t1.value, t1.p_comparator, t1.p_reported, t1.p_decimals) == (38, 2.14, "=", 0.039, 3)
    ns = [s for s in stats["t"] if s.p_comparator == "ns"][0]
    assert ns.value == -1.05 and ns.p_reported is None  # unicode minus normalized, 'ns' handled
    ci = [s for s in stats["t"] if s.df1 == 22][0]
    assert ci.p_reported == 0.02  # CI clause between the statistic and p is skipped
    compact = [s for s in stats["t"] if s.df1 == 10][0]
    assert compact.p_reported == 0.34


def test_f_with_extra_clause_and_p_less_than():
    f = _by_kind(extract_stats(load_text(TXT)))["F"][0]
    assert (f.df1, f.df2, f.value, f.p_comparator, f.p_reported) == (2, 87, 4.21, "<", 0.05)
    f2 = _by_kind(extract_stats(load_text(TXT)))["F"][1]
    assert f2.p_reported == 0.054 and f2.p_decimals == 3  # "0.054" and ".054" both accepted


def test_chi_square_variants():
    chis = _by_kind(extract_stats(load_text(TXT)))["chi2"]
    assert chis[0].n == 120 and chis[0].df1 == 1 and chis[0].p_reported == 0.47
    assert chis[1].df1 == 2 and chis[1].value == 7.1  # "chi-square(2)" spelled out


def test_means_with_n_sources():
    means = extract_means(load_text(TXT))
    assert len(means) == 2
    assert (means[0].mean, means[0].sd, means[0].n, means[0].n_source) == (3.42, 1.10, 23, "same parenthesis")
    assert means[1].mean_text == "2.9" and means[1].n == 23 and means[1].n_source == "same sentence"


def test_sample_sizes():
    ns = {d["n"] for d in extract_sample_sizes(load_text(TXT))}
    assert {120, 23} <= ns


def test_normalize_dehyphenates_and_joins_lines():
    assert normalize("signifi-\ncant effect\nhere") == "significant effect here"
    assert normalize("p = . 05") == "p = .05"


def test_sentence_at_picks_containing_sentence():
    text = normalize("First sentence here. The effect was t(38) = 2.14, p = .039. Third one.")
    pos = text.index("t(38)")
    assert sentence_at(text, pos) == "The effect was t(38) = 2.14, p = .039."


def test_no_false_z_from_words():
    stats = extract_stats(load_text("The Hz = 2.5, p = .03 setting was used."))
    assert stats == []


def test_spelled_out_sample_sizes_and_word_numbers():
    from papercheck.extract import words_to_int
    assert words_to_int("Two-hundred and thirty-five") == 235
    assert words_to_int("One-hundred and nineteen") == 119
    assert words_to_int("forty") == 40
    assert words_to_int("two thousand") == 2000
    assert words_to_int("the") is None
    txt = "Two-hundred and thirty-five (126 Female; MAge = 32.1) participated. Forty students took part."
    found = extract_sample_sizes(load_text(txt))
    assert {d["n"] for d in found if d["kind"] == "spelled out"} >= {235, 40}
    assert 40 in {d["n"] for d in found}


def test_means_without_comma_and_paren_sd():
    txt = ("Participants (N = 357) did the task. The treatment group (M = 10.51 SD = 2.66) did not differ. "
           "Their mean age was 33.18 (SD = 9.88).")
    means = extract_means(load_text(txt))
    assert [(m.mean, m.sd) for m in means] == [(10.51, 2.66), (33.18, 9.88)]
    assert all(m.n == 357 for m in means)


def test_sample_size_regex_rejects_number_tails_and_study_labels():
    txt = ("Study 2 revealed that people chose faster. The value was 0.016 with participants responding. "
           "A total of 584 participants took part; Experiment 3 students were excluded.")
    found = {d["n"] for d in extract_sample_sizes(load_text(txt)) if d["kind"] == "count noun"}
    assert found == {584}


def test_table_like_cells_do_not_borrow_a_preceding_n():
    # michelkrohler_2023 p6: several group n in one table block; the cell must not be tested against the wrong one
    txt = ("Table 1. Descriptives, M (SD). n = 20 (f = 14, m = 6) n = 19 (f = 13, m = 6) n = 20 (f = 14, m = 6). "
           "RSQ-B .77 9.70 (2.99) [8.30, 11.10] 9.42 (3.02) [7.96, 10.88] 9.60 (2.64).")
    means = extract_means(load_text(txt))
    cells = [m for m in means if m.mean_text == "9.42"]
    assert cells and cells[0].n is None
