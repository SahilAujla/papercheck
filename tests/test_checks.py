import pytest

from papercheck.checks import check_df_vs_n, check_duplicates, check_grim, check_p_values, compute_p, run_all
from papercheck.extract import extract_means, extract_sample_sizes, extract_stats
from papercheck.models import MeanSD, Stat
from papercheck.pdf import load_text


def _stat(**kw):
    base = dict(kind="t", value=2.14, value_decimals=2, df1=38.0, p_reported=0.039, p_comparator="=", p_decimals=3,
                raw="t(38) = 2.14, p = .039", page=1, sentence="x")
    base.update(kw)
    return Stat(**base)


def test_compute_p_values():
    assert compute_p("t", 2.14, 38, None) == pytest.approx(0.0388, abs=1e-3)
    assert compute_p("F", 4.21, 2, 87) == pytest.approx(0.0179, abs=1e-3)
    assert compute_p("chi2", 5.0, 1, None) == pytest.approx(0.0253, abs=1e-3)
    assert compute_p("r", 0.32, 58, None) == pytest.approx(0.0127, abs=1e-3)
    assert compute_p("z", 1.96, None, None) == pytest.approx(0.05, abs=1e-3)
    assert compute_p("t", 2.0, 0, None) is None


def test_consistent_p_not_flagged():
    assert check_p_values(_stat()) is None
    assert check_p_values(_stat(p_comparator="<", p_reported=0.05)) is None
    assert check_p_values(_stat(value=1.0, p_comparator="ns", p_reported=None)) is None
    # rounding of the statistic is respected: t(38)=2.02 gives p in [.048, .052], reported .05 overlaps
    assert check_p_values(_stat(value=2.02, p_reported=0.05, p_decimals=2)) is None


def test_inconsistent_p_is_warning_without_decision_change():
    f = check_p_values(_stat(kind="chi2", value=5.0, df1=1.0, p_reported=0.042, p_decimals=3,
                             raw="chi2(1, N = 89) = 5.00, p = 0.042"))
    assert f is not None and f.severity == "warning" and f.details["decision_error"] is False
    assert f.details["p_recomputed"] == pytest.approx(0.0253, abs=1e-3)


def test_decision_error_is_error():
    # t(38) = 1.50 gives p = .14, reported as p = .03
    f = check_p_values(_stat(value=1.50, p_reported=0.03, p_decimals=2))
    assert f is not None and f.severity == "error" and f.details["decision_error"] is True
    # and the reverse: reported ns but recomputed p is tiny
    f2 = check_p_values(_stat(value=4.0, p_comparator="ns", p_reported=None))
    assert f2 is not None and f2.severity == "error"


def test_one_tailed_consistent_is_info():
    # t(38) = 1.80 two-tailed p = .080, one-tailed .040; reported p = .04
    f = check_p_values(_stat(value=1.80, p_reported=0.04, p_decimals=2))
    assert f is not None and f.details["consistent_if_one_tailed"] is True
    assert f.severity in ("info", "error")  # decision error wins when both apply


def test_p_equals_zero_treated_as_less_than():
    assert check_p_values(_stat(value=9.0, p_reported=0.0, p_decimals=3)) is None


def test_grim_flags_impossible_mean():
    m = MeanSD(mean=3.51, mean_text="3.51", n=20, n_source="same sentence", raw="M = 3.51", page=2, sentence="s")
    flags = check_grim(m)
    assert len(flags) == 1 and flags[0].check == "grim" and flags[0].severity == "warning"
    assert 3.5 in flags[0].details["nearest_possible"]
    weak = MeanSD(mean=3.51, mean_text="3.51", n=20, n_source="nearest preceding N on the page", raw="", page=2,
                  sentence="s")
    assert check_grim(weak)[0].severity == "info"
    ok = MeanSD(mean=3.50, mean_text="3.50", n=20, n_source="same sentence", raw="", page=2, sentence="s")
    assert check_grim(ok) == []
    assert check_grim(MeanSD(mean=3.51, mean_text="3.51", n=None, raw="", page=1, sentence="")) == []


def test_grimmer_flag_when_mean_passes_but_sd_impossible():
    m = MeanSD(mean=3.0, mean_text="3.00", sd=1.10, sd_text="1.10", n=5, n_source="same sentence", raw="",
               page=1, sentence="s")
    flags = check_grim(m)
    assert [f.check for f in flags] == ["grimmer"]
    good = MeanSD(mean=3.0, mean_text="3.00", sd=1.58, sd_text="1.58", n=5, n_source="same sentence", raw="",
                  page=1, sentence="s")
    assert check_grim(good) == []


def test_df_vs_n_flags_only_when_df_exceeds_every_reported_n():
    sizes = [{"n": 120, "page": 1, "raw": "N = 120", "kind": "N ="}]
    small = _stat(df1=38.0)
    big = _stat(df1=233.0, raw="t(233) = 16.64, p < .001")
    flags = check_df_vs_n([small, big], sizes)
    assert len(flags) == 1 and flags[0].raw.startswith("t(233)") and flags[0].severity == "warning"
    welch = _stat(df1=233.7)
    assert check_df_vs_n([welch], sizes) == []
    chi = _stat(kind="chi2", df1=1.0, n=89, value=5.0)
    assert check_df_vs_n([chi], sizes)[0].severity == "info"


def test_duplicates():
    a = _stat(page=1, sentence="abstract")
    b = _stat(page=5, sentence="results")
    c = _stat(value=3.0)
    flags = check_duplicates([a, b, c])
    assert len(flags) == 1 and flags[0].details["count"] == 2 and flags[0].details["pages"] == [1, 5]


def test_run_all_end_to_end_on_text():
    txt = ("We recruited 40 students (N = 40). Scores were higher in group A (M = 3.51, SD = 1.02, n = 20), "
           "t(38) = 1.50, p = .03. Also t(38) = 1.50, p = .03 was found again. Another test, t(80) = 2.5, p = .014.")
    pages = load_text(txt)
    flags = run_all(extract_stats(pages), extract_means(pages), extract_sample_sizes(pages))
    checks = sorted(f.check for f in flags)
    assert checks == ["df_vs_n", "duplicate", "grim", "p_recompute", "p_recompute"]
    assert flags[0].severity == "error"  # sorted errors first


def test_value_comparator_bounds_recomputed_p():
    # urschler_2024 p9: "t(334) < 0.01, p = .999" means the statistic is below 0.01, so p is at least .992
    st = _stat(df1=334.0, value=0.01, value_comparator="<", p_reported=0.999, p_decimals=3,
               raw="t(334) < 0.01, p = .999")
    assert check_p_values(st) is None
    st2 = _stat(df1=40.0, value=10.0, value_comparator=">", p_reported=0.001, p_comparator="<", p_decimals=3)
    assert check_p_values(st2) is None


def test_df_vs_n_downgraded_for_repeated_measures_wording():
    sizes = [{"n": 29, "page": 1, "raw": "N = 29", "kind": "N ="}]
    # takayama_2023 p6: 29 participants x 3 days, F(2, 56)
    st = _stat(kind="F", df1=2.0, df2=56.0, value=1.84, p_reported=0.17, p_decimals=2,
               sentence="A repeated measures ANOVA across the three days showed no effect, F(2, 56) = 1.84, p = .17.",
               raw="F(2, 56) = 1.84, p = .17")
    flags = check_df_vs_n([st], sizes)
    assert len(flags) == 1 and flags[0].severity == "info"
    plain = _stat(kind="F", df1=2.0, df2=56.0, value=1.84, sentence="Groups differed, F(2, 56) = 1.84, p = .17.")
    assert check_df_vs_n([plain], sizes)[0].severity == "warning"
