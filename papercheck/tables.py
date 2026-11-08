"""Table extraction with PyMuPDF find_tables(): means, SDs and group n from table columns or rows."""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Optional

import pymupdf

from .models import MeanSD

_SIG_MARKS = "\x03#*†‡§abcd"
_NUM_CELL = re.compile(r"^-?\d*\.?\d+$")


@dataclass
class Table:
    page: int
    rows: list[list[str]]
    bbox: tuple[float, float, float, float] = (0, 0, 0, 0)
    strategy: str = "lines"
    caption: str = ""

    @property
    def header(self) -> list[str]:
        return self.rows[0] if self.rows else []


def fix_cell(cell: Optional[str]) -> str:
    """Clean a cell: drop significance marks and footnote letters glued to numbers, collapse whitespace."""
    if cell is None:
        return ""
    s = cell.replace("\n", " ")
    for ch in _SIG_MARKS:
        s = s.replace(ch, "")
    s = re.sub(r"(?<=\d)[a-d](?=\s|$)", "", s)
    return re.sub(r"\s+", " ", s).strip()


def _cell_text(page, rect) -> str:
    """Rebuild a cell from positioned words. find_tables().extract() can reorder characters in some PDFs
    ('3.51' comes back as '351 .'); words sorted by position do not have that problem."""
    if rect is None:
        return ""
    words = page.get_text("words", clip=pymupdf.Rect(rect))
    words.sort(key=lambda w: (round(w[1], 1), w[0]))
    return " ".join(w[4] for w in words)


def load_tables(path: str) -> list[Table]:
    """All tables PyMuPDF can find. Uses the 'lines' strategy; falls back to 'text' on pages that mention a
    table with SD values but have no ruled table."""
    doc = pymupdf.open(path)
    out: list[Table] = []
    for i, page in enumerate(doc, start=1):
        text = page.get_text("text")
        found = _find(page, "lines")
        if not found and re.search(r"\bTable \d", text) and re.search(r"\bSD\b|\(SD\)", text):
            found = [t for t in _find(page, "text") if _looks_like_stats_table(t)]
        for t in found:
            t.page = i
            t.caption = _caption(text)
            out.append(t)
    doc.close()
    return out


def _find(page, strategy: str) -> list[Table]:
    try:
        tabs = page.find_tables(strategy=strategy)
    except Exception:
        return []
    res = []
    for t in tabs.tables:
        rows = [[fix_cell(_cell_text(page, rect)) for rect in row.cells] for row in t.rows]
        rows = [r for r in rows if any(c for c in r)]
        if len(rows) >= 2 and len(rows[0]) >= 2:
            res.append(Table(page=0, rows=rows, bbox=tuple(t.bbox), strategy=strategy))
    return res


def _looks_like_stats_table(t: Table) -> bool:
    head = " ".join(t.header).lower()
    return bool(re.search(r"\bm\b|mean|\bsd\b", head))


def _caption(text: str) -> str:
    m = re.search(r"Table \d+\.?[^\n]{0,160}", text)
    return m.group(0).strip() if m else ""


_COL_M = re.compile(r"^(m|mean|means|m \(sd\)|mean \(sd\)|m\(sd\))$", re.I)
_COL_SD = re.compile(r"^(sd|s\.d\.|std|std\. dev\.)$", re.I)
_COL_N = re.compile(r"^(n|\bn\b|sample size)$", re.I)
_HEAD_N = re.compile(r"\(?\b[nN]\s*=\s*(\d[\d,]*)\)?")
_MSD_CELL = re.compile(r"^(?P<mean>-?\d*\.?\d+)\s*\(\s*(?P<sd>\d*\.?\d+)\s*\)$")


def means_from_tables(tables: list[Table]) -> list[MeanSD]:
    """Pull means with SD and n out of tables.

    Handles three layouts: (1) columns headed M, SD, n with one group per row; (2) 'M (SD)' cells in a column whose
    header carries '(n = 23)'; (3) a row labelled n/N under the columns giving the group size per column."""
    out: list[MeanSD] = []
    for t in tables:
        head = [h.strip() for h in t.header]
        low = [h.lower().strip() for h in head]
        m_cols = [i for i, h in enumerate(low) if _COL_M.match(h)]
        sd_cols = [i for i, h in enumerate(low) if _COL_SD.match(h)]
        n_cols = [i for i, h in enumerate(low) if _COL_N.match(h)]
        col_n = {i: int(_HEAD_N.search(h).group(1).replace(",", "")) for i, h in enumerate(head) if _HEAD_N.search(h)}
        n_row = _n_row(t.rows)
        for r_i, row in enumerate(t.rows[1:], start=1):
            if row is t.rows[n_row] if n_row is not None else False:
                continue
            label = row[0] if row else ""
            row_n = None
            if n_cols and n_cols[0] < len(row) and _NUM_CELL.match(row[n_cols[0]] or ""):
                row_n = int(float(row[n_cols[0]]))
            # layout 1: M and SD columns paired by order
            for k, mc in enumerate(m_cols):
                if mc >= len(row) or not _NUM_CELL.match(row[mc] or ""):
                    continue
                sd_txt = None
                if k < len(sd_cols) and sd_cols[k] < len(row) and _NUM_CELL.match(row[sd_cols[k]] or ""):
                    sd_txt = row[sd_cols[k]]
                n, src = _pick_n(row_n, col_n.get(mc), n_row, t.rows, mc)
                out.append(_mk(row[mc], sd_txt, n, src, t, label, head[mc]))
            # layout 2 and 3: 'M (SD)' cells anywhere in the row
            for c_i, cell in enumerate(row):
                mm = _MSD_CELL.match(cell or "")
                if not mm or c_i in m_cols:
                    continue
                n, src = _pick_n(row_n, col_n.get(c_i), n_row, t.rows, c_i)
                out.append(_mk(mm["mean"], mm["sd"], n, src, t, label, head[c_i] if c_i < len(head) else ""))
    return out


def _n_row(rows: list[list[str]]) -> Optional[int]:
    for i, r in enumerate(rows):
        if r and re.fullmatch(r"(n|N|sample size|No\. of participants)", (r[0] or "").strip()):
            return i
    return None


def _pick_n(row_n, col_n, n_row, rows, col) -> tuple[Optional[int], str]:
    if row_n:
        return row_n, "table n column"
    if col_n:
        return col_n, "table column header"
    if n_row is not None and col < len(rows[n_row]) and _NUM_CELL.match(rows[n_row][col] or ""):
        return int(float(rows[n_row][col])), "table n row"
    return None, ""


def _mk(mean_txt: str, sd_txt: Optional[str], n, src, t: Table, label: str, col: str) -> MeanSD:
    where = f"{t.caption or 'table'}; row '{label}'; column '{col}'".strip()
    return MeanSD(mean=float(mean_txt), mean_text=mean_txt, sd=float(sd_txt) if sd_txt else None, sd_text=sd_txt,
                  n=n, n_source=src, raw=f"{mean_txt}" + (f" ({sd_txt})" if sd_txt else ""), page=t.page,
                  sentence=where, pos=0)
