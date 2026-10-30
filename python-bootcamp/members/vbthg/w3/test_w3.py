"""Boundary and command-level checks for the individual Week 3 exercises."""

import subprocess
import sys
from datetime import date
from pathlib import Path

import pytest

from members.vbthg.w2.models import Task
from members.vbthg.w3.cli import format_plan
from members.vbthg.w3.dates import parse_due
from members.vbthg.w3.log_stats import analyse

BOOTCAMP = Path(__file__).resolve().parents[3]


@pytest.mark.parametrize("text,today,expected", [
    ("2024-02-29", date(2026, 10, 6), date(2024, 2, 29)),
    ("tomorrow", date(2026, 12, 31), date(2027, 1, 1)),
    ("in 0 days", date(2026, 10, 6), date(2026, 10, 6)),
    ("in 3 days", date(2026, 10, 30), date(2026, 11, 2)),
    ("Tue", date(2026, 10, 6), date(2026, 10, 13)),
    ("Mon", date(2026, 10, 11), date(2026, 10, 12)),
    (" FRI ", date(2026, 10, 6), date(2026, 10, 9)),
])
def test_deadline_boundaries(text: str, today: date, expected: date) -> None:
    """Resolve calendar transitions and strictly-next weekdays."""
    assert parse_due(text, today) == expected


@pytest.mark.parametrize("text", [
    "", "2026-02-29", "20261030", "2026-1-02", "in -1 days", "someday",
])
def test_unknown_deadline(text: str) -> None:
    """Reject ambiguous formats and impossible dates."""
    with pytest.raises(ValueError):
        parse_due(text, date(2026, 10, 6))


def test_deadline_overflow_is_value_error() -> None:
    """Keep the documented exception even at the end of the date range."""
    with pytest.raises(ValueError):
        parse_due("tomorrow", date.max)


def test_p95_uses_nearest_rank_not_maximum() -> None:
    """A 20-observation route has p95 at the nineteenth observation."""
    pairs = [("fee", value) for value in range(20, 0, -1)]
    pairs.append(("rag", 18))
    assert analyse(iter(pairs)) == {
        "counts": {"fee": 20, "rag": 1},
        "p95": {"fee": 19, "rag": 18},
        "slowest": "fee",
    }


def test_empty_log_and_equal_p95() -> None:
    """Empty logs have no slowest route; ties have a stable route name."""
    assert analyse([]) == {"counts": {}, "p95": {}, "slowest": None}
    assert analyse([("z", 10), ("a", 10)])["slowest"] == "a"


@pytest.mark.parametrize("latency", [-1, float("nan"), float("inf")])
def test_invalid_latency(latency: float) -> None:
    """Invalid measurements must not silently distort route statistics."""
    with pytest.raises(ValueError, match="latency_ms"):
        analyse([("fee", latency)])


def test_plan_sorts_without_mutating_and_allocates_partial_task() -> None:
    """The urgent task comes first even when the CSV lists it last."""
    tasks = [
        Task("DS exam", 5, 6, date(2026, 10, 30)),
        Task("Assignment", 4, 1.5, date(2026, 10, 27)),
    ]
    plan = format_plan(tasks, 2, date(2026, 10, 26))
    assert plan.splitlines() == [
        "Tonight (2.0 h):",
        "  1. Assignment ...... 1.5 h",
        "  2. DS exam ...... 0.5 h",
    ]
    assert [task.title for task in tasks] == ["DS exam", "Assignment"]
    assert [task.effort_h for task in tasks] == [6, 1.5]


@pytest.mark.parametrize("hours", [-1, float("nan"), float("inf")])
def test_invalid_budget(hours: float) -> None:
    """Reject nonfinite or negative budgets before allocation."""
    with pytest.raises(ValueError, match="hours"):
        format_plan([], hours, date(2026, 10, 26))


def test_no_work_and_surplus_budget() -> None:
    """Zero budgets and zero effort yield no blocks; surplus is not counted."""
    today = date(2026, 10, 26)
    tasks = [Task("No effort", 5, 0, today), Task("Study", 2, 0.5, today)]
    assert format_plan(tasks, 0, today) == "Nothing planned."
    assert format_plan([], 2, today) == "Nothing planned."
    assert format_plan(tasks, 3, today).splitlines() == [
        "Tonight (0.5 h):", "  1. Study ...... 0.5 h",
    ]


def run_cli(*arguments: str) -> subprocess.CompletedProcess[str]:
    """Exercise the real module entry point from the bootcamp directory."""
    return subprocess.run(
        [sys.executable, "-m", "members.vbthg.w3.cli", *arguments],
        cwd=BOOTCAMP, capture_output=True, text=True, timeout=10,
    )


def test_cli_sample_is_reproducible() -> None:
    """A fixed reference date produces the expected two-hour plan."""
    result = run_cli("samples/tasks.csv", "--hours", "2", "--today", "2026-10-26")
    assert result.returncode == 0
    assert result.stderr == ""
    assert "Tonight (2.0 h):" in result.stdout
    assert result.stdout.index("Assignment") < result.stdout.index("DS exam")
    assert "0.5 h" in result.stdout


@pytest.mark.parametrize("filename", ["missing.csv", "samples/tasks_bad.csv"])
def test_cli_file_error_has_no_traceback(filename: str) -> None:
    """Missing and invalid CSVs exit with code 1 and an actionable error."""
    result = run_cli(filename, "--hours", "2")
    assert result.returncode == 1
    assert result.stdout == ""
    assert "Cannot create plan:" in result.stderr
    assert "Traceback" not in result.stderr


def test_cli_rejects_invalid_date_argument() -> None:
    """Bad --today values are reported by argparse with exit code 2."""
    result = run_cli("samples/tasks.csv", "--hours", "2", "--today", "2026-02-30")
    assert result.returncode == 2
    assert "--today" in result.stderr


def test_cli_header_only_csv(tmp_path: Path) -> None:
    """A valid CSV with no tasks is a successful empty plan."""
    sample = tmp_path / "empty.csv"
    sample.write_text("title,importance,effort_h,deadline\n", encoding="utf-8")
    result = run_cli(str(sample), "--hours", "2")
    assert result.returncode == 0
    assert result.stdout.strip() == "Nothing planned."
