"""T-W3 (Thông): exercise the real planner command across all four modules."""

from pathlib import Path
import re
import subprocess
import sys

BOOTCAMP = Path(__file__).resolve().parents[2]


def run_planner(csv: Path, hours: str, today: str) -> subprocess.CompletedProcess[str]:
    """Start a fresh interpreter with the documented module command."""
    return subprocess.run(
        [sys.executable, "-m", "shared.study_planner", str(csv),
         "--hours", hours, "--today", today],
        cwd=BOOTCAMP, capture_output=True, text=True, timeout=10,
    )


def plan_lines(result: subprocess.CompletedProcess[str]) -> list[str]:
    """Require a clean CLI exit and ignore only the cosmetic dot padding."""
    assert result.returncode == 0, result.stderr
    assert result.stderr == ""
    return [re.sub(r"\.{2,}", "...", line).strip() for line in result.stdout.splitlines()]


def test_sample_csv_partial_session() -> None:
    """Parse -> prioritise -> allocate -> render must reorder and split tasks."""
    sample = BOOTCAMP / "samples" / "tasks.csv"
    original = sample.read_bytes()
    assert plan_lines(run_planner(sample, "2", "2026-10-26")) == [
        "Tonight (2.0 h):",
        "1. Assignment ... 1.5 h",
        "2. DS exam ... 0.5 h",
    ]
    assert sample.read_bytes() == original


def test_reference_date_changes_priority(tmp_path: Path) -> None:
    """The supplied --today must reach prioritise, not the machine's clock."""
    sample = tmp_path / "tasks.csv"
    sample.write_text(
        "title,importance,effort_h,deadline\n"
        "Later exam,5,2,2026-10-30\n"
        "Earlier task,2,1,2026-10-27\n",
        encoding="utf-8",
    )
    assert plan_lines(run_planner(sample, "1", "2026-10-26")) == [
        "Tonight (1.0 h):", "1. Earlier task ... 1.0 h",
    ]
    assert plan_lines(run_planner(sample, "1", "2026-10-30")) == [
        "Tonight (1.0 h):", "1. Later exam ... 1.0 h",
    ]


def test_surplus_budget_reports_allocated_total(tmp_path: Path) -> None:
    """The CLI reports actual work, preserving quoted CSV titles end to end."""
    sample = tmp_path / "quoted tasks.csv"
    sample.write_text(
        'title,importance,effort_h,deadline\n"Read, revise",3,1.5,2026-10-30\n',
        encoding="utf-8",
    )
    assert plan_lines(run_planner(sample, "4", "2026-10-26")) == [
        "Tonight (1.5 h):", "1. Read, revise ... 1.5 h",
    ]
