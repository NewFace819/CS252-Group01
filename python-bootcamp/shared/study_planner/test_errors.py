"""T-W3 (THA Anh): error handling of the study planner CLI."""

import subprocess
import sys
from datetime import date
from pathlib import Path

import pytest

from shared.contract import Task
from shared.study_planner.errors import InfeasiblePlan, check_feasible

BOOTCAMP = Path(__file__).resolve().parents[2]
SAMPLE = BOOTCAMP / "samples" / "tasks.csv"
HEADER = "title,importance,effort_h,deadline\n"


def run(*args: str) -> subprocess.CompletedProcess[str]:
    """Run `python -m shared.study_planner` in a fresh interpreter."""
    return subprocess.run(
        [sys.executable, "-m", "shared.study_planner", *args],
        cwd=BOOTCAMP, capture_output=True, text=True, timeout=10,
    )


def test_missing_file() -> None:
    res = run("does_not_exist.csv", "--hours", "2")
    assert res.returncode == 1
    assert "file not found" in res.stderr
    assert "Traceback" not in res.stderr


def test_directory_instead_of_file(tmp_path: Path) -> None:
    res = run(str(tmp_path), "--hours", "2")
    assert res.returncode == 1
    assert "Traceback" not in res.stderr


@pytest.mark.parametrize("content", ["", "  \n\n"])
def test_empty_file(tmp_path: Path, content: str) -> None:
    f = tmp_path / "empty.csv"
    f.write_text(content, encoding="utf-8")
    res = run(str(f), "--hours", "2")
    assert res.returncode == 1
    assert "empty" in res.stderr


def test_header_only_file(tmp_path: Path) -> None:
    f = tmp_path / "header.csv"
    f.write_text(HEADER, encoding="utf-8")
    res = run(str(f), "--hours", "2")
    assert res.returncode == 1
    assert "no tasks" in res.stderr


def test_bad_row_names_the_line(tmp_path: Path) -> None:
    f = tmp_path / "bad.csv"
    f.write_text(HEADER + "A,9,1,2026-10-30\n", encoding="utf-8")
    res = run(str(f), "--hours", "2")
    assert res.returncode == 1
    assert "line 2" in res.stderr


def test_strict_infeasible_plan() -> None:
    res = run(str(SAMPLE), "--hours", "2", "--today", "2026-10-26", "--strict")
    assert res.returncode == 1
    assert "7.5 h" in res.stderr and "5.5 h short" in res.stderr
    assert res.stdout == ""


def test_strict_feasible_plan_succeeds() -> None:
    res = run(str(SAMPLE), "--hours", "8", "--today", "2026-10-26", "--strict")
    assert res.returncode == 0
    assert "Tonight (7.5 h):" in res.stdout


def test_default_is_partial_plan_not_error() -> None:
    res = run(str(SAMPLE), "--hours", "2", "--today", "2026-10-26")
    assert res.returncode == 0 and res.stderr == ""


def test_check_feasible_unit() -> None:
    tasks = [Task("a", 3, 2.0, date(2026, 10, 30))]
    check_feasible(tasks, 2.0)
    with pytest.raises(InfeasiblePlan) as info:
        check_feasible(tasks, 1.0)
    assert info.value.needed_h == 2.0 and info.value.available_h == 1.0
    assert "1.0 h short" in str(info.value)
