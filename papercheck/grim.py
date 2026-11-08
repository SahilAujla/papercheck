"""GRIM and GRIMMER consistency tests for reported means and standard deviations.

GRIM (Granularity-Related Inconsistency of Means; Brown & Heathers 2017):
when each of ``n`` participants answers ``items`` integer-valued items, the
mean must equal ``k / (n * items)`` for some integer ``k``. A reported mean
that no such fraction rounds to is impossible.

GRIMMER (Anaya 2016; Allard 2018 refinement): given a GRIM-consistent mean,
the sum of squares of integer data is itself an integer, so the reported SD
(after accounting for its rounding interval) must correspond to an integer
sum of squares. For integer data the sum of squares also has the same parity
as the sum (x**2 == x mod 2), which is applied as a trivial refinement.

Stdlib only. All arithmetic is done with ``fractions.Fraction`` so rounding
boundaries are exact.
"""

from __future__ import annotations

import math
import re
from dataclasses import dataclass, field
from fractions import Fraction

__all__ = [
    "GrimResult",
    "GrimmerResult",
    "count_decimals",
    "grim_test",
    "grimmer_test",
]

_NOTE_TOO_LARGE = "n*items too large for GRIM to be informative"
_NOTE_ITEMS = "GRIMMER only implemented for items=1"
_FLOAT_NOISE = Fraction(1, 10**9)


@dataclass
class GrimResult:
    mean: float
    n: int
    decimals: int
    items: int
    consistent: bool
    nearest_possible: list[float] = field(default_factory=list)
    note: str = ""


@dataclass
class GrimmerResult:
    mean: float
    sd: float
    n: int
    decimals_mean: int
    decimals_sd: int
    items: int
    grim_consistent: bool
    consistent: bool
    note: str = ""


# --------------------------------------------------------------------------- #
# helpers
# --------------------------------------------------------------------------- #

_DECIMALS_RE = re.compile(r"\.(\d*)")


def count_decimals(text: str) -> int:
    """Number of digits after the decimal point in a number written as text.

    "3.50" -> 2, "3.5" -> 1, "12" -> 0, "-0.05" -> 2, ".5" -> 1.
    Scientific notation such as "1.5e-3" counts the mantissa digits only.
    """
    s = str(text).strip()
    m = _DECIMALS_RE.search(s)
    if m is None:
        return 0
    return len(m.group(1))


def _frac(x) -> Fraction:
    """Exact Fraction from an int, float, str, Decimal or Fraction.

    Floats go through ``repr`` so 3.51 becomes 351/100, not the binary value.
    """
    if isinstance(x, Fraction):
        return x
    if isinstance(x, bool):
        return Fraction(int(x))
    if isinstance(x, int):
        return Fraction(x)
    if isinstance(x, float):
        if math.isnan(x) or math.isinf(x):
            raise ValueError(f"cannot test non-finite value {x!r}")
        return Fraction(repr(x))
    return Fraction(str(x).strip())


def _round_half_up(x: Fraction, decimals: int) -> Fraction:
    """Round half away from zero to ``decimals`` places, exactly."""
    shift = Fraction(10) ** decimals
    scaled = abs(x) * shift
    rounded = math.floor(scaled + Fraction(1, 2))
    result = Fraction(rounded) / shift
    return -result if x < 0 else result


def _round_half_even(x: Fraction, decimals: int) -> Fraction:
    """Round half to even (banker's rounding) to ``decimals`` places, exactly."""
    shift = Fraction(10) ** decimals
    return Fraction(round(x * shift)) / shift


def _tolerance(decimals: int) -> Fraction:
    """Half a unit in the last reported place, plus a little float slack."""
    return Fraction(1, 2) / (Fraction(10) ** decimals) + _FLOAT_NOISE


def _matches_reported(candidate: Fraction, reported: Fraction, decimals: int) -> bool:
    """Would ``candidate`` plausibly have been reported as ``reported``?

    Lenient about convention: half-up, half-even, or anything within half a
    unit of the last place (which also covers truncation at the boundary).
    """
    if _round_half_up(candidate, decimals) == reported:
        return True
    if _round_half_even(candidate, decimals) == reported:
        return True
    return abs(candidate - reported) <= _tolerance(decimals)


def _matching_sums(reported: Fraction, total_n: int, decimals: int) -> list[int]:
    """All integer sums S with S / total_n consistent with the reported mean."""
    tol = _tolerance(decimals)
    lo = math.ceil((reported - tol) * total_n)
    hi = math.floor((reported + tol) * total_n)
    # Widen by one on each side so the explicit rounding checks get a look too.
    return [
        s
        for s in range(lo - 1, hi + 2)
        if _matches_reported(Fraction(s, total_n), reported, decimals)
    ]


# --------------------------------------------------------------------------- #
# GRIM
# --------------------------------------------------------------------------- #


def grim_test(mean: float, n: int, decimals: int, items: int = 1) -> GrimResult:
    """Standard GRIM test.

    ``consistent`` is True when some integer sum divided by ``n * items``
    rounds to ``mean`` at ``decimals`` places. When inconsistent,
    ``nearest_possible`` lists up to two achievable means (rounded to
    ``decimals``) that bracket the reported one, nearest first.

    Degenerate inputs (``n <= 0``, ``items <= 0``, ``decimals < 0``) and
    uninformative cases (``n * items > 10 ** decimals``, where every value at
    that precision is achievable) return ``consistent=True`` with a note.
    """
    try:
        n = int(n)
        items = int(items)
        decimals = int(decimals)
    except (TypeError, ValueError):
        return GrimResult(mean, n, decimals, items, True, [], "invalid n/items/decimals")

    if n <= 0:
        return GrimResult(mean, n, decimals, items, True, [], "n must be positive")
    if items <= 0:
        return GrimResult(mean, n, decimals, items, True, [], "items must be positive")
    if decimals < 0:
        return GrimResult(mean, n, decimals, items, True, [], "decimals must be >= 0")

    total_n = n * items
    if total_n > 10**decimals:
        return GrimResult(mean, n, decimals, items, True, [], _NOTE_TOO_LARGE)

    try:
        reported = _frac(mean)
    except (ValueError, ZeroDivisionError):
        return GrimResult(mean, n, decimals, items, True, [], "mean is not a finite number")

    if _matching_sums(reported, total_n, decimals):
        return GrimResult(float(mean), n, decimals, items, True, [], "")

    # Inconsistent: report the achievable means on either side of the target.
    scaled = reported * total_n
    k_lo = math.floor(scaled)
    k_hi = k_lo + 1
    candidates: dict[float, Fraction] = {}
    for k in (k_lo, k_hi):
        exact = Fraction(k, total_n)
        rounded = float(_round_half_up(exact, decimals))
        # Keep the candidate nearest to the reported mean for each rounded value.
        dist = abs(exact - reported)
        if rounded not in candidates or dist < candidates[rounded]:
            candidates[rounded] = dist
    nearest = sorted(candidates, key=lambda v: (candidates[v], v))[:2]

    return GrimResult(float(mean), n, decimals, items, False, nearest, "")


# --------------------------------------------------------------------------- #
# GRIMMER
# --------------------------------------------------------------------------- #


def _sum_of_squares_matches(
    total: int, total_n: int, sd: Fraction, decimals_sd: int
) -> bool:
    """Is there an integer sum of squares consistent with sum ``total`` and ``sd``?

    With N = total_n and sample variance var = (SS - S**2 / N) / (N - 1):
        SS = var * (N - 1) + S**2 / N.
    The reported SD stands for any value in [sd - h, sd + h] with
    h = 0.5 * 10**-decimals_sd, so var (and hence SS) ranges over an interval.
    An integer SS in that interval with the same parity as S is a match.
    """
    half_unit = Fraction(1, 2) / (Fraction(10) ** decimals_sd)
    sd_lo = max(sd - half_unit, Fraction(0))
    sd_hi = sd + half_unit
    var_lo = sd_lo * sd_lo
    var_hi = sd_hi * sd_hi

    base = Fraction(total * total, total_n)  # S**2 / N
    ss_lo = var_lo * (total_n - 1) + base - _FLOAT_NOISE
    ss_hi = var_hi * (total_n - 1) + base + _FLOAT_NOISE

    first = math.ceil(ss_lo)
    last = math.floor(ss_hi)
    if first > last:
        return False
    # Parity refinement: for integer data sum(x**2) == sum(x) (mod 2).
    for ss in range(first, last + 1):
        if ss >= base and (ss - total) % 2 == 0:
            return True
    return False


def grimmer_test(
    mean: float,
    sd: float,
    n: int,
    decimals_mean: int,
    decimals_sd: int,
    items: int = 1,
) -> GrimmerResult:
    """GRIMMER test for a reported mean and (sample) standard deviation.

    ``grim_consistent`` is the GRIM result for the mean. ``consistent`` is the
    GRIMMER result: it is False when GRIM fails, or when GRIM passes but no
    integer sum of squares (with the right parity) reproduces the reported SD
    within its rounding interval for any sum matching the mean.

    Only ``items == 1`` is implemented; other values return ``consistent=True``
    with a note. Degenerate inputs (``sd < 0``, ``n < 2``, negative decimals)
    and uninformative cases (``n * items > 10 ** decimals_mean``) also return
    ``consistent=True`` with a note.
    """
    grim = grim_test(mean, n, decimals_mean, items)

    def result(grim_ok: bool, ok: bool, note: str) -> GrimmerResult:
        return GrimmerResult(
            mean=mean,
            sd=sd,
            n=n,
            decimals_mean=decimals_mean,
            decimals_sd=decimals_sd,
            items=items,
            grim_consistent=grim_ok,
            consistent=ok,
            note=note,
        )

    if grim.note:
        # Degenerate or uninformative GRIM input; nothing more can be said.
        return result(True, True, grim.note)

    try:
        n_int = int(n)
        items_int = int(items)
        decimals_sd = int(decimals_sd)
        decimals_mean = int(decimals_mean)
    except (TypeError, ValueError):
        return result(True, True, "invalid n/items/decimals")

    if n_int < 2:
        return result(grim.consistent, True, "n must be at least 2 for an SD")
    if decimals_sd < 0:
        return result(grim.consistent, True, "decimals_sd must be >= 0")

    try:
        sd_frac = _frac(sd)
    except (ValueError, ZeroDivisionError):
        return result(grim.consistent, True, "sd is not a finite number")
    if sd_frac < 0:
        return result(grim.consistent, True, "sd must be non-negative")

    if items_int != 1:
        return result(grim.consistent, True, _NOTE_ITEMS)

    if not grim.consistent:
        return result(False, False, "GRIM inconsistent, so GRIMMER cannot pass")

    reported = _frac(mean)
    total_n = n_int  # items == 1
    sums = _matching_sums(reported, total_n, decimals_mean)
    for total in sums:
        if _sum_of_squares_matches(total, total_n, sd_frac, decimals_sd):
            return result(True, True, "")

    return result(True, False, "")
