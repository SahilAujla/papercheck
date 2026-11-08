import json
from pathlib import Path

import pymupdf

from papercheck.checks import check_grim
from papercheck.cli import analyze
from papercheck.tables import Table, fix_cell, load_tables, means_from_tables

FIXTURE = Path(__file__).parent / "fixtures" / "yan_2018_p9_table.json"


def make_ruled_table_pdf(path: Path, rows, caption="Table 1. Descriptive statistics by condition."):
    doc = pymupdf.open()
    page = doc.new_page()
    page.insert_text((72, 60), caption, fontsize=10)
    xs = [72 + 90 * i for i in range(len(rows[0]) + 1)]
    y0 = 80
    for i, r in enumerate(rows):
        y = y0 + i * 20
        page.draw_line((xs[0], y), (xs[-1], y))
        for j, c in enumerate(r):
            page.insert_text((xs[j] + 4, y + 14), c, fontsize=10)
    page.draw_line((xs[0], y0 + len(rows) * 20), (xs[-1], y0 + len(rows) * 20))
    for x in xs:
        page.draw_line((x, y0), (x, y0 + len(rows) * 20))
    doc.save(str(path))


def test_fix_cell_strips_marks():
    assert fix_cell("0.84\x03\x03") == "0.84"
    assert fix_cell("-1.04#") == "-1.04"
    assert fix_cell("3.51a") == "3.51"
    assert fix_cell(None) == ""


def test_yan_coefficient_table_yields_no_means():
    data = json.loads(FIXTURE.read_text())
    t = Table(page=data["page"], rows=data["rows"], caption=data["caption"])
    assert "SE" in " ".join(t.rows[1])  # it is a coefficient table
    assert means_from_tables([t]) == []  # no M/SD/n layout, so nothing is fed to GRIM


def test_m_sd_n_columns(tmp_path):
    pdf = tmp_path / "t.pdf"
    make_ruled_table_pdf(pdf, [["Condition", "M", "SD", "n"], ["Control", "3.51", "1.02", "20"],
                              ["Treatment", "4.20", "0.95", "25"]])
    tables = load_tables(str(pdf))
    assert len(tables) == 1 and tables[0].rows[1] == ["Control", "3.51", "1.02", "20"]  # cells read correctly
    means = means_from_tables(tables)
    assert [(m.mean_text, m.sd_text, m.n, m.n_source) for m in means] == [
        ("3.51", "1.02", 20, "table n column"), ("4.20", "0.95", 25, "table n column")]
    assert means[0].page == 1 and "Table 1" in means[0].sentence and "Control" in means[0].sentence
    flags = check_grim(means[0])
    assert flags and flags[0].check == "grim" and flags[0].severity == "warning"  # 3.51 impossible for n = 20
    assert not [f for f in check_grim(means[1]) if f.check == "grim"]  # 4.20 * 25 = 105, possible


def test_m_sd_cells_with_n_in_column_header(tmp_path):
    pdf = tmp_path / "t.pdf"
    make_ruled_table_pdf(pdf, [["Measure", "Control (n = 20)", "Treatment (n = 25)"],
                              ["Mood", "3.51 (1.02)", "4.20 (0.95)"], ["Effort", "2.45 (0.80)", "2.52 (0.90)"]])
    means = means_from_tables(load_tables(str(pdf)))
    got = {(m.mean_text, m.n, m.n_source) for m in means}
    assert got == {("3.51", 20, "table column header"), ("4.20", 25, "table column header"),
                   ("2.45", 20, "table column header"), ("2.52", 25, "table column header")}


def test_n_row_layout(tmp_path):
    pdf = tmp_path / "t.pdf"
    make_ruled_table_pdf(pdf, [["", "Group A", "Group B"], ["M (SD)", "3.51 (1.02)", "4.20 (0.95)"],
                              ["n", "20", "25"]])
    means = means_from_tables(load_tables(str(pdf)))
    assert {(m.mean_text, m.n, m.n_source) for m in means} == {("3.51", 20, "table n row"), ("4.20", 25, "table n row")}


def test_analyze_includes_table_means(tmp_path):
    pdf = tmp_path / "paper.pdf"
    make_ruled_table_pdf(pdf, [["Condition", "M", "SD", "n"], ["Control", "3.51", "1.02", "20"]])
    payload = analyze(str(pdf))
    assert payload["summary"]["means_with_n"] == 1
    assert any(f["check"] == "grim" and f["severity"] == "warning" for f in payload["flags"])
