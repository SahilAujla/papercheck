"""Data classes shared by the extractor, the checks and the report."""
from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any, Optional


@dataclass
class Stat:
    """One inferential test statistic reported together with a p value."""

    kind: str                     # 't', 'F', 'chi2', 'r', 'z'
    value: float
    value_decimals: int
    df1: Optional[float] = None   # t/r/chi2 df, or F numerator df
    df2: Optional[float] = None   # F denominator df
    n: Optional[int] = None       # N reported inside chi2(df, N = ...)
    value_comparator: str = "="   # '=', '<', '>'
    p_reported: Optional[float] = None
    p_comparator: Optional[str] = None  # '=', '<', '>', 'ns'
    p_decimals: int = 2
    raw: str = ""
    page: int = 0
    sentence: str = ""
    pos: int = 0                  # character offset in the normalized page text

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    def label(self) -> str:
        if self.kind == "F":
            return f"F({_fmt(self.df1)}, {_fmt(self.df2)}) {self.value_comparator} {self.value}"
        if self.kind == "z":
            return f"z {self.value_comparator} {self.value}"
        name = {"chi2": "chi2", "t": "t", "r": "r"}[self.kind]
        if self.kind == "chi2" and self.n:
            return f"{name}({_fmt(self.df1)}, N = {self.n}) {self.value_comparator} {self.value}"
        return f"{name}({_fmt(self.df1)}) {self.value_comparator} {self.value}"


@dataclass
class MeanSD:
    """A reported mean, optionally with SD and N, as written in the text."""

    mean: float
    mean_text: str
    sd: Optional[float] = None
    sd_text: Optional[str] = None
    n: Optional[int] = None
    n_source: str = ""            # 'same parenthesis', 'same sentence', ''
    raw: str = ""
    page: int = 0
    sentence: str = ""
    pos: int = 0

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class Flag:
    """One finding. Severity is 'error' (decision error), 'warning' or 'info'."""

    check: str                    # 'p_recompute', 'grim', 'grimmer', 'df_vs_n', 'duplicate'
    severity: str
    page: int
    sentence: str
    raw: str
    explanation: str
    details: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _fmt(x: Optional[float]) -> str:
    if x is None:
        return "?"
    return str(int(x)) if float(x).is_integer() else str(x)
