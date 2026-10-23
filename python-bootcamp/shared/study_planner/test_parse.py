"""Tests for shared/study_planner/parse.py (T-W2, Đỗ Huy)."""

from __future__ import annotations

import textwrap
from datetime import date
from pathlib import Path

import pytest

from shared.study_planner.parse import parse_csv


@pytest.fixture()
def sample_dir():
    """Return the path to the bootcamp samples/ directory."""
    return Path(__file__).resolve().parents[2] / "samples"


# ── Happy path ────────────────────────────────────────────────────────


def test_parse_sample_csv(sample_dir):
    """parse_csv returns the correct tasks from the instructor's sample."""
    tasks = parse_csv(sample_dir / "tasks.csv")
    assert len(tasks) == 2
    assert tasks[0].title == "DS exam"
    assert tasks[0].importance == 5
    assert tasks[0].effort_h == 6.0
    assert tasks[0].deadline == date(2026, 10, 30)
    assert tasks[1].title == "Assignment"


# ── Bad rows ──────────────────────────────────────────────────────────


def test_bad_importance_string(sample_dir):
    """A non-integer importance raises ValueError with the line number."""
    with pytest.raises(ValueError, match="line 3"):
        parse_csv(sample_dir / "tasks_bad.csv")


def test_importance_out_of_range(tmp_path):
    """importance outside 1–5 raises ValueError."""
    csv = tmp_path / "bad.csv"
    csv.write_text(
        textwrap.dedent("""\
            title,importance,effort_h,deadline
            ok,3,1,2026-10-30
            nope,9,1,2026-10-30
        """),
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="line 3"):
        parse_csv(csv)


def test_importance_zero(tmp_path):
    """importance = 0 is out of range."""
    csv = tmp_path / "zero.csv"
    csv.write_text(
        "title,importance,effort_h,deadline\nzero,0,1,2026-10-30\n",
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="line 2"):
        parse_csv(csv)


def test_missing_columns(tmp_path):
    """A row with fewer columns than expected raises ValueError with line number."""
    csv = tmp_path / "missing_cols.csv"
    csv.write_text(
        "title,importance,effort_h,deadline\nStudy,3\n",
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="line 2"):
        parse_csv(csv)


def test_extra_columns(tmp_path):
    """A row with extra unexpected columns raises ValueError with line number."""
    csv = tmp_path / "extra_cols.csv"
    csv.write_text(
        "title,importance,effort_h,deadline\nStudy,3,1,2026-10-30,bonus\n",
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="line 2"):
        parse_csv(csv)


def test_blank_line_preserves_physical_line_number(tmp_path):
    """A blank line before an invalid row must not throw off the physical line count."""
    csv = tmp_path / "with_blank.csv"
    csv.write_text(
        "title,importance,effort_h,deadline\n\nStudy,bad,1,2026-10-30\n",
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="line 3"):
        parse_csv(csv)


def test_multiline_field_reports_correct_line(tmp_path):
    """A multiline quoted field shifts the physical line position accurately."""
    csv = tmp_path / "multiline.csv"
    csv.write_text(
        'title,importance,effort_h,deadline\n"Study\nMore",3,1,2026-10-30\nBad,high,1,2026-10-30\n',
        encoding="utf-8",
    )
    # Header is line 1.
    # "Study\nMore" spans lines 2 and 3.
    # Bad row is on line 4.
    with pytest.raises(ValueError, match="line 4"):
        parse_csv(csv)


# ── Edge cases ────────────────────────────────────────────────────────


def test_empty_csv(tmp_path):
    """A CSV with only a header returns an empty list."""
    csv = tmp_path / "empty.csv"
    csv.write_text(
        "title,importance,effort_h,deadline\n",
        encoding="utf-8",
    )
    assert parse_csv(csv) == []


def test_zero_byte_file(tmp_path):
    """A completely empty file (0 bytes) raises ValueError for line 1."""
    csv = tmp_path / "zero_bytes.csv"
    csv.write_text("", encoding="utf-8")
    with pytest.raises(ValueError, match="line 1"):
        parse_csv(csv)


def test_bad_header(tmp_path):
    """A CSV with incorrect column names raises ValueError naming line 1."""
    csv = tmp_path / "bad_header.csv"
    csv.write_text("name,priority,hours,due\na,3,1,2026-10-30\n", encoding="utf-8")
    with pytest.raises(ValueError, match="line 1"):
        parse_csv(csv)
