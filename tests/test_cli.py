import json
from pathlib import Path

from papercheck.cli import main


def test_cli_writes_markdown_and_json(tmp_path: Path):
    paper = tmp_path / "paper.txt"
    paper.write_text("Participants (N = 40). The effect, t(38) = 1.50, p = .03, was clear (M = 3.51, SD = 1.0, n = 20).")
    out = tmp_path / "reports"
    assert main([str(paper), "--out", str(out), "--quiet"]) == 0
    md = (out / "paper.md").read_text()
    data = json.loads((out / "paper.json").read_text())
    assert "# papercheck report: paper.txt" in md
    assert "| p value recomputation (statcheck style) | 1 | 1 |" in md
    assert data["summary"]["flags_by_severity"]["error"] == 1
    assert data["flags"][0]["page"] == 1 and "t(38) = 1.50, p = .03" in data["flags"][0]["raw"]
    assert "misconduct" in data["disclaimer"]  # the disclaimer says a flag is not evidence of misconduct


def test_cli_reports_bad_path(tmp_path: Path, capsys):
    rc = main([str(tmp_path / "missing.pdf"), "--out", str(tmp_path / "r"), "--quiet"])
    assert rc == 1
    assert "failed" in capsys.readouterr().err
