"""PDF text loading and normalization (PyMuPDF)."""
from __future__ import annotations

import re
from dataclasses import dataclass

import pymupdf


@dataclass
class Page:
    number: int   # 1-based
    text: str     # normalized text


_LIGATURES = {
    "ﬀ": "ff", "ﬁ": "fi", "ﬂ": "fl", "ﬃ": "ffi", "ﬄ": "ffl",
    "−": "-", "–": "-", "—": "-", "‐": "-", "‑": "-",
    " ": " ", " ": " ", " ": " ", " ": " ", " ": " ", " ": " ",
    " ": " ", " ": " ", " ": " ", " ": " ", "​": "",
    "’": "'", "‘": "'", "“": '"', "”": '"',
    "＜": "<", "＞": ">", "＝": "=", "≤": "<=", "≥": ">=",
    "Χ": "χ", "ᵪ": "χ", "𝜒": "χ", " ": " ",
    "²": "2", "₂": "2",
}


def normalize(text: str) -> str:
    """Make PDF text regex friendly without changing character meaning."""
    for src, dst in _LIGATURES.items():
        text = text.replace(src, dst)
    # de-hyphenate words broken across lines: "signifi-\ncant" -> "significant"
    text = re.sub(r"(?<=[a-z])-\n(?=[a-z])", "", text)
    # join lines inside paragraphs, keep blank lines as paragraph breaks
    text = re.sub(r"(?<!\n)\n(?!\n)", " ", text)
    text = re.sub(r"[ \t]+", " ", text)
    # digits split from a decimal point by a space, e.g. "p = . 05" or "2. 14"
    text = re.sub(r"(?<=[=<>])\s*\.\s+(?=\d)", " .", text)
    text = re.sub(r"(?<=\d)\s\.(?=\d)", ".", text)
    return text


def load_pdf(path: str) -> list[Page]:
    doc = pymupdf.open(path)
    pages = []
    for i, page in enumerate(doc, start=1):
        pages.append(Page(number=i, text=normalize(page.get_text("text"))))
    doc.close()
    return pages


def load_text(text: str) -> list[Page]:
    """Treat a plain string as a one-page document (used in tests)."""
    return [Page(number=1, text=normalize(text))]


_SENT_BOUNDARY = re.compile(r"(?<=[a-z\)\]0-9%])\.\s+(?=[A-Z\(])|\n\n")


def sentence_at(text: str, pos: int, max_len: int = 400) -> str:
    """Return the sentence containing character offset pos."""
    start = 0
    for m in _SENT_BOUNDARY.finditer(text, 0, pos):
        start = m.end()
    end_m = _SENT_BOUNDARY.search(text, pos)
    end = end_m.start() + 1 if end_m else len(text)
    sent = text[start:end].strip()
    if len(sent) > max_len:
        # centre the window on the match
        rel = pos - start
        lo = max(0, rel - max_len // 2)
        sent = ("..." if lo > 0 else "") + sent[lo:lo + max_len].strip() + "..."
    return re.sub(r"\s+", " ", sent)
