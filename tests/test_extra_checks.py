from papercheck.extra_checks import check_ci_symmetry, check_regression, check_unverifiable
from papercheck.pdf import load_text


def kinds(flags):
    return [f.details.get("kind") for f in flags]


# ---------------------------------------------------------------- unverifiable

def test_blanket_ps_flagged():
    flags = check_unverifiable(load_text("All effects were reliable, ps < .05, and robust."))
    assert len(flags) == 1
    assert flags[0].check == "unverifiable" and flags[0].severity == "info"
    assert flags[0].details["kind"] == "blanket_p"
    assert "blanket" in flags[0].explanation


def test_blanket_all_ps_and_p_values():
    text = "Results held, all ps < .001. Other contrasts did not, p values > .10."
    flags = check_unverifiable(load_text(text))
    assert kinds(flags) == ["blanket_p", "blanket_p"]
    assert [f.details["p"] for f in flags] == [0.001, 0.10]


def test_bare_t_flagged_with_implied_p():
    flags = check_unverifiable(load_text("The groups differed, t(38) = 2.14."))
    assert len(flags) == 1
    f = flags[0]
    assert f.details["kind"] == "stat_without_p" and f.details["stat"] == "t"
    assert abs(f.details["p_implied"] - 0.0388) < 0.001
    assert "0.038" in f.explanation


def test_bare_F_r_and_chi2():
    text = ("The ANOVA was reliable, F(2, 87) = 4.21. The correlation was r(58) = .32. "
            "The association held, χ2(1) = 5.3. The chi-square(2) = 7.1 also held.")
    flags = check_unverifiable(load_text(text))
    assert [f.details["stat"] for f in flags] == ["F", "r", "chi2", "chi2"]
    assert all(f.details["p_implied"] is not None for f in flags)


def test_bare_z_only_after_separator():
    flags = check_unverifiable(load_text("The sampling rate was 44 Hz = 2.1 units. The effect held (z = 2.10)."))
    assert len(flags) == 1
    assert flags[0].details["stat"] == "z"


def test_stat_with_p_in_sentence_not_flagged():
    flags = check_unverifiable(load_text("The groups differed, t(38) = 2.14, p = .04."))
    assert flags == []


def test_known_spans_skip():
    pages = load_text("The groups differed, t(38) = 2.14.")
    m_start = pages[0].text.index("t(38)")
    flags = check_unverifiable(pages, {1: [(m_start, m_start + 12)]})
    assert flags == []
    assert len(check_unverifiable(pages, {2: [(m_start, m_start + 12)]})) == 1


def test_lone_p_flagged_and_p_with_stat_not():
    text = "The difference was significant, p = .03. Scores rose, b = 0.42, SE = 0.11, p = .001."
    flags = check_unverifiable(load_text(text))
    assert kinds(flags) == ["p_without_stat"]
    assert flags[0].raw == "p = .03"


def test_unverifiable_cap_40():
    text = " ".join(f"Test {i} was reliable, t(3{i % 9}) = 2.{i:02d}." for i in range(45))
    flags = check_unverifiable(load_text(text))
    assert len(flags) == 41
    assert flags[-1].details == {"kind": "omitted", "omitted": 5}


# ---------------------------------------------------------------- ci_symmetry

def test_ci_symmetric_not_flagged():
    text = ("The effect was medium, d = 0.45, 95% CI [0.12, 0.78]. The slope was b = 1.2, SE = 0.4, 95% CI = [0.42, 1.98]. "
            "The mean was M = 3.4, 95% CI (3.1, 3.7), and r = .32, 95% CI [.07, .54].")
    assert check_ci_symmetry(load_text(text)) == []


def test_ci_asymmetric_flagged():
    flags = check_ci_symmetry(load_text("The effect was large, d = 0.65, 95% CI [0.12, 0.78]."))
    assert len(flags) == 1
    f = flags[0]
    assert f.check == "ci_symmetry" and f.severity == "warning"
    assert f.details["estimate"] == "d" and abs(f.details["midpoint"] - 0.45) < 1e-9
    assert "0.45" in f.explanation and "0.65" in f.explanation


def test_ci_other_syntaxes():
    text = ("The gain was 2.9, 95% CI: 2.1 to 3.7. The difference of 2.1 (95% CI 1.5, 2.7) was reliable. "
            "Hedges' g = 0.90, CI95 [0.20, 0.60].")
    flags = check_ci_symmetry(load_text(text))
    assert len(flags) == 1
    assert flags[0].details["estimate"] == "Hedges' g"


def test_ci_ratio_geometric_midpoint():
    ok = check_ci_symmetry(load_text("Smokers had higher odds, OR = 1.79, 95% CI [1.10, 2.90]."))
    assert ok == []
    bad = check_ci_symmetry(load_text("Smokers had higher odds, OR = 2.60, 95% CI [1.10, 2.90]."))
    assert len(bad) == 1 and bad[0].details["ratio_scale"] is True
    assert "geometric" in bad[0].explanation
    # non-positive bound: skipped rather than flagged
    assert check_ci_symmetry(load_text("HR = 0.8, 95% CI [-0.2, 1.3].")) == []


def test_ci_reversed_is_info():
    flags = check_ci_symmetry(load_text("The effect was d = 0.45, 95% CI [0.78, 0.12]."))
    assert len(flags) == 1
    assert flags[0].severity == "info" and flags[0].details["kind"] == "reversed"


def test_ci_without_point_estimate_skipped():
    assert check_ci_symmetry(load_text("The interval was wide, 95% CI [0.12, 0.78], as expected.")) == []


# ---------------------------------------------------------------- regression

def test_regression_consistent_not_flagged():
    text = ("Income predicted scores, b = 0.42, SE = 0.11, p < .001. Age did not, B = -0.20 (SE = 0.08), p = .01. "
            "The standardized effect was β = .25, SE = .10, p < .05.")
    assert check_regression(load_text(text)) == []


def test_regression_inconsistent_warning():
    flags = check_regression(load_text("Income predicted scores, b = 0.42, SE = 0.11, p = .03."))
    assert len(flags) == 1
    f = flags[0]
    assert f.check == "regression" and f.severity == "warning"
    assert f.details["decision_error"] is False
    assert "robust or clustered" in f.explanation


def test_regression_decision_error():
    flags = check_regression(load_text("Income predicted scores, b = 0.42, SE = 0.30, p = .001."))
    assert len(flags) == 1
    assert flags[0].severity == "error" and flags[0].details["decision_error"] is True
    assert "different sides of .05" in flags[0].explanation


def test_regression_paren_se_requires_mention():
    bare = "Income predicted scores, b = 0.42 (0.11), p = .03."
    assert check_regression(load_text(bare)) == []
    mentioned = "Standard errors in parentheses: income predicted scores, b = 0.42 (0.11), p = .03."
    flags = check_regression(load_text(mentioned))
    assert len(flags) == 1 and flags[0].details["se"] == 0.11


def test_regression_t_given_uses_t_distribution_and_checks_ratio():
    ok = check_regression(load_text("Income predicted scores, b = 0.42, SE = 0.11, t(120) = 3.82, p < .001."))
    assert ok == []
    flags = check_regression(load_text("Income predicted scores, b = 0.42, SE = 0.11, t = 2.10, p < .001."))
    assert kinds(flags) == ["t_vs_b_over_se"]
    assert "does not match b / SE" in flags[0].explanation


def test_regression_small_df_changes_p():
    # b/SE = 2.1: normal p = .036, t(5) p = .09, so with t(5) in the sentence p = .09 is consistent
    assert check_regression(load_text("The slope, b = 0.21, SE = 0.10, t(5) = 2.10, p = .09, was positive.")) == []
    flags = check_regression(load_text("The slope, b = 0.21, SE = 0.10, z = 2.10, p = .09, was positive."))
    assert [f.details["kind"] for f in flags] == ["p_vs_b_over_se"]


def test_ci_symmetry_bootstrap_interval_is_info():
    from papercheck.extra_checks import check_ci_symmetry
    from papercheck.pdf import load_text
    # choi_2024 p9: a bootstrapped indirect effect has an asymmetric interval by construction
    txt = ("The bootstrap analysis showed a significant indirect effect of -.1044 (95% CI: -.1718, -.0496) "
           "on the outcome.")
    flags = check_ci_symmetry(load_text(txt))
    assert len(flags) == 1 and flags[0].severity == "info" and flags[0].details.get("asymmetric_by_design") is True
    plain = check_ci_symmetry(load_text("The effect was d = 0.45, 95% CI [0.30, 0.50]."))
    assert len(plain) == 1 and plain[0].severity == "warning"
