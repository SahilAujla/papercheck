"""Tests for papercheck.grim (GRIM and GRIMMER)."""

import math
import statistics
from fractions import Fraction

import pytest

from papercheck.grim import (
    GrimResult,
    GrimmerResult,
    count_decimals,
    grim_test,
    grimmer_test,
)


# --------------------------------------------------------------------------- #
# count_decimals
# --------------------------------------------------------------------------- #


@pytest.mark.parametrize(
    "text, expected",
    [
        ("3.50", 2),
        ("3.5", 1),
        ("12", 0),
        ("-0.05", 2),
        (".5", 1),
        ("  2.125 ", 3),
        ("0", 0),
        ("-7", 0),
        ("100.", 0),
    ],
)
def test_count_decimals(text, expected):
    assert count_decimals(text) == expected


# --------------------------------------------------------------------------- #
# GRIM
# --------------------------------------------------------------------------- #


def test_grim_consistent_simple():
    # 70 / 20 = 3.50 exactly.
    r = grim_test(3.50, 20, 2)
    assert isinstance(r, GrimResult)
    assert r.consistent is True
    assert r.nearest_possible == []
    assert r.note == ""


def test_grim_inconsistent_with_neighbours():
    # 3.51 * 20 = 70.2; neither 70/20 = 3.50 nor 71/20 = 3.55 rounds to 3.51.
    r = grim_test(3.51, 20, 2)
    assert r.consistent is False
    assert 3.50 in r.nearest_possible
    assert 3.55 in r.nearest_possible
    assert len(r.nearest_possible) == 2
    # Nearest first: 3.50 is 0.01 away, 3.55 is 0.04 away.
    assert r.nearest_possible[0] == 3.50


def test_grim_one_decimal_consistent():
    # 12 / 5 = 2.4 exactly.
    r = grim_test(2.4, 5, 1)
    assert r.consistent is True


def test_grim_one_decimal_inconsistent():
    # 2.3 * 5 = 11.5; 11/5 = 2.2 and 12/5 = 2.4 are the achievable neighbours.
    r = grim_test(2.3, 5, 1)
    assert r.consistent is False
    assert sorted(r.nearest_possible) == [2.2, 2.4]


def test_grim_rounding_not_exact_but_consistent():
    # 148 / 28 = 5.2857..., which rounds to 5.3. With decimals=1 and n=28 > 10
    # every one-decimal value is achievable, so the module also flags the test
    # as uninformative; either way the reported mean is consistent.
    r = grim_test(5.3, 28, 1)
    assert r.consistent is True
    assert r.nearest_possible == []


def test_grim_rounding_informative_case():
    # Same idea where n*items <= 10**decimals: 37 / 7 = 5.2857... -> 5.29.
    r = grim_test(5.29, 7, 2)
    assert r.consistent is True
    assert r.note == ""
    # 5.30 is not reachable with n = 7 (37/7 = 5.2857, 38/7 = 5.4286).
    r2 = grim_test(5.30, 7, 2)
    assert r2.consistent is False
    assert r2.nearest_possible == [5.29, 5.43]


def test_grim_half_boundary_is_accepted_either_way():
    # 1 / 8 = 0.125 can be reported as 0.12 (half-even) or 0.13 (half-up).
    assert grim_test(0.12, 8, 2).consistent is True
    assert grim_test(0.13, 8, 2).consistent is True
    assert grim_test(0.14, 8, 2).consistent is False


def test_grim_n_too_large_is_uninformative():
    r = grim_test(4.5, 1000, 1)
    assert r.consistent is True
    assert r.note == "n*items too large for GRIM to be informative"
    assert r.nearest_possible == []


def test_grim_items_scale_the_granularity():
    # Two items, n = 10: granularity is 1/20, and 65/20 = 3.25.
    r = grim_test(3.25, 10, 2, items=2)
    assert r.consistent is True
    assert r.items == 2
    # With a single item 3.25 * 10 = 32.5 is not an integer sum.
    assert grim_test(3.25, 10, 2, items=1).consistent is False


def test_grim_negative_mean():
    # -7 / 4 = -1.75 is achievable; -1.76 is not.
    assert grim_test(-1.75, 4, 2).consistent is True
    r = grim_test(-1.76, 4, 2)
    assert r.consistent is False
    assert -1.75 in r.nearest_possible


def test_grim_zero_decimals():
    # Integers are always achievable when n*items <= 1 ... n=1 only.
    assert grim_test(3, 1, 0).consistent is True
    # n = 2 > 10**0 is uninformative.
    assert grim_test(3, 2, 0).note != ""


def test_grim_bad_inputs_return_consistent_with_note():
    for kwargs in (
        dict(mean=3.5, n=0, decimals=2),
        dict(mean=3.5, n=-4, decimals=2),
        dict(mean=3.5, n=10, decimals=-1),
        dict(mean=3.5, n=10, decimals=2, items=0),
    ):
        r = grim_test(**kwargs)
        assert r.consistent is True
        assert r.note != ""
        assert r.nearest_possible == []


# --------------------------------------------------------------------------- #
# GRIMMER
# --------------------------------------------------------------------------- #


def _ss_interval(mean_sum: int, n: int, sd: str, decimals_sd: int):
    """Independent computation of the sum-of-squares interval implied by an SD.

    var = (SS - S**2/N) / (N - 1)  =>  SS = var * (N - 1) + S**2 / N,
    with var ranging over [(sd - h)**2, (sd + h)**2], h = 0.5 * 10**-decimals.
    """
    sd_f = Fraction(sd)
    h = Fraction(1, 2 * 10**decimals_sd)
    base = Fraction(mean_sum * mean_sum, n)
    lo = (sd_f - h) ** 2 * (n - 1) + base
    hi = (sd_f + h) ** 2 * (n - 1) + base
    return lo, hi


def _integers_in(lo: Fraction, hi: Fraction):
    return list(range(math.ceil(lo), math.floor(hi) + 1))


def test_grimmer_real_sample_1_to_5():
    data = [1, 2, 3, 4, 5]
    mean = round(statistics.mean(data), 2)  # 3.00
    sd = round(statistics.stdev(data), 2)  # sqrt(2.5) = 1.5811 -> 1.58
    assert mean == 3.0 and sd == 1.58
    r = grimmer_test(mean, sd, len(data), 2, 2)
    assert isinstance(r, GrimmerResult)
    assert r.grim_consistent is True
    assert r.consistent is True
    assert r.note == ""


def test_grimmer_real_sample_skewed():
    data = [1, 1, 1, 5, 5]
    mean = round(statistics.mean(data), 2)  # 2.60
    sd = round(statistics.stdev(data), 2)  # sqrt(4.8) = 2.1909 -> 2.19
    assert mean == 2.6 and sd == 2.19
    r = grimmer_test(mean, sd, len(data), 2, 2)
    assert r.grim_consistent is True
    assert r.consistent is True


def test_grimmer_fabricated_sd_1_00_is_consistent():
    # n=5, mean 3.00 -> S = 15, S**2/N = 45. SD in [0.995, 1.005] gives
    # var in [0.990025, 1.010025] and SS in [48.9601, 49.0401], which
    # contains the integer 49 (same parity as S = 15), so GRIMMER passes.
    lo, hi = _ss_interval(15, 5, "1.00", 2)
    ints = [s for s in _integers_in(lo, hi) if (s - 15) % 2 == 0]
    assert ints == [49]
    r = grimmer_test(3.00, 1.00, 5, 2, 2)
    assert r.grim_consistent is True
    assert r.consistent is True


def test_grimmer_fabricated_sd_1_10_is_inconsistent():
    # n=5, mean 3.00 -> S = 15, S**2/N = 45. SD in [1.095, 1.105] gives
    # var in [1.199025, 1.221025] and SS in [49.7961, 49.8841], which
    # contains no integer at all, so GRIMMER must fail.
    lo, hi = _ss_interval(15, 5, "1.10", 2)
    assert float(lo) == pytest.approx(49.7961)
    assert float(hi) == pytest.approx(49.8841)
    assert _integers_in(lo, hi) == []
    # 3.00 with n=5 has exactly one matching sum (S = 15), so no other sum
    # can rescue it.
    assert [s for s in range(10, 21) if round(s / 5, 2) == 3.00] == [15]
    r = grimmer_test(3.00, 1.10, 5, 2, 2)
    assert r.grim_consistent is True
    assert r.consistent is False


def test_grimmer_parity_refinement():
    # n=5, mean 3.00, S = 15 (odd). An SD that lands exactly on SS = 50 (even)
    # is impossible for integer data because sum(x**2) == sum(x) (mod 2).
    # SS = 50 -> var = (50 - 45) / 4 = 1.25 -> sd = 1.118034. Reported to
    # four decimals (1.1180), the SS interval is [49.9996, 50.0004]: only 50.
    sd_exact = math.sqrt(1.25)
    sd_text = f"{sd_exact:.4f}"
    assert sd_text == "1.1180"
    lo, hi = _ss_interval(15, 5, sd_text, 4)
    assert _integers_in(lo, hi) == [50]
    r = grimmer_test(3.00, float(sd_text), 5, 2, 4)
    assert r.grim_consistent is True
    assert r.consistent is False
    # SS = 51 (odd) is fine: var = 1.5, sd = 1.224745 -> 1.2247.
    sd_ok = f"{math.sqrt(1.5):.4f}"
    lo, hi = _ss_interval(15, 5, sd_ok, 4)
    assert _integers_in(lo, hi) == [51]
    assert grimmer_test(3.00, float(sd_ok), 5, 2, 4).consistent is True


def test_grimmer_grim_failure_propagates():
    # 3.51 is GRIM-inconsistent for n=20, so GRIMMER cannot pass either.
    r = grimmer_test(3.51, 1.00, 20, 2, 2)
    assert r.grim_consistent is False
    assert r.consistent is False
    assert r.note != ""


def test_grimmer_items_not_implemented():
    r = grimmer_test(3.25, 1.00, 10, 2, 2, items=2)
    assert r.grim_consistent is True
    assert r.consistent is True
    assert r.note == "GRIMMER only implemented for items=1"


def test_grimmer_n_too_large_is_uninformative():
    r = grimmer_test(4.5, 1.2, 1000, 1, 1)
    assert r.grim_consistent is True
    assert r.consistent is True
    assert "too large" in r.note


def test_grimmer_guards():
    for kwargs in (
        dict(mean=3.0, sd=-0.5, n=5, decimals_mean=2, decimals_sd=2),
        dict(mean=3.0, sd=1.0, n=1, decimals_mean=2, decimals_sd=2),
        dict(mean=3.0, sd=1.0, n=0, decimals_mean=2, decimals_sd=2),
        dict(mean=3.0, sd=1.0, n=5, decimals_mean=-1, decimals_sd=2),
        dict(mean=3.0, sd=1.0, n=5, decimals_mean=2, decimals_sd=-1),
    ):
        r = grimmer_test(**kwargs)
        assert r.consistent is True, kwargs
        assert r.note != "", kwargs


def test_grimmer_zero_sd_requires_identical_values():
    # mean 3.00, n=5, sd 0.00: all values equal 3 -> SS = 45 exactly. Fine.
    assert grimmer_test(3.00, 0.00, 5, 2, 2).consistent is True
    # mean 3.20, n=5 (S = 16), sd 0.00: SS would have to be 16**2/5 = 51.2,
    # which is not an integer, so identical values cannot produce this mean.
    lo, hi = _ss_interval(16, 5, "0.00", 2)
    assert _integers_in(lo, hi) == []
    assert grimmer_test(3.20, 0.00, 5, 2, 2).consistent is False
