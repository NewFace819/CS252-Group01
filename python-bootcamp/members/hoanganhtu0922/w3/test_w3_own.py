"""Own edge-case tests for W3-1, W3-2 and W3-3."""

import subprocess
import sys
from collections import Counter
from datetime import date
from pathlib import Path

import pytest

from members.hoanganhtu0922.w3.cli import main
from members.hoanganhtu0922.w3.dates import parse_due
from members.hoanganhtu0922.w3.log_stats import analyse

BOOTCAMP = Path(__file__).resolve().parents[3]
SAMPLE = BOOTCAMP / "samples" / "tasks.csv"
TODAY = date(2026, 10, 6)  # a Tuesday


# --- W3-1 ---------------------------------------------------------------
@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("2026-10-30", date(2026, 10, 30)),
        ("tomorrow", date(2026, 10, 7)),
        ("in 3 days", date(2026, 10, 9)),
        ("in 1 day", date(2026, 10, 7)),
        ("in 0 days", TODAY),
        ("Fri", date(2026, 10, 9)),
        ("friday", date(2026, 10, 9)),
        ("Tue", date(2026, 10, 13)),
        ("Mon", date(2026, 10, 12)),
        ("  TOMORROW ", date(2026, 10, 7)),
    ],
)
def test_parse_due_ok(text: str, expected: date) -> None:
    assert parse_due(text, TODAY) == expected


@pytest.mark.parametrize("text", ["", "someday", "frog", "2026-13-45", "in x days", "in 3 weeks"])
def test_parse_due_bad(text: str) -> None:
    with pytest.raises(ValueError):
        parse_due(text, TODAY)


# --- W3-2 ---------------------------------------------------------------
def test_analyse_empty() -> None:
    assert analyse([]) == {"counts": Counter(), "p95": {}, "slowest": None}


def test_analyse_single_value() -> None:
    res = analyse([("a", 42)])
    assert res["counts"] == {"a": 1}
    assert res["p95"] == {"a": 42}
    assert res["slowest"] == "a"


def test_analyse_p95_nearest_rank() -> None:
    pairs = [("r", i) for i in range(1, 101)]  # 1..100 -> rank 95 -> 95
    assert analyse(pairs)["p95"]["r"] == 95


def test_analyse_unsorted_input() -> None:
    pairs = [("r", 500), ("r", 100), ("r", 300)]
    assert analyse(pairs)["p95"]["r"] == 500


# --- W3-3 ---------------------------------------------------------------
def test_cli_output(capsys: pytest.CaptureFixture[str]) -> None:
    code = main([str(SAMPLE), "--hours", "2", "--today", "2026-10-26"])
    out = capsys.readouterr().out
    assert code == 0
    assert out.startswith("Tonight (2.0 h):")
    assert out.index("Assignment") < out.index("DS exam")


def test_cli_missing_file(capsys: pytest.CaptureFixture[str]) -> None:
    code = main(["nope.csv", "--hours", "2"])
    assert code == 1
    assert "file not found" in capsys.readouterr().err


def test_cli_zero_hours(capsys: pytest.CaptureFixture[str]) -> None:
    assert main([str(SAMPLE), "--hours", "0", "--today", "2026-10-26"]) == 0
    assert "Nothing planned." in capsys.readouterr().out


def test_cli_bad_csv(capsys: pytest.CaptureFixture[str]) -> None:
    bad = BOOTCAMP / "samples" / "tasks_bad.csv"
    assert main([str(bad), "--hours", "2"]) == 1
    assert "error" in capsys.readouterr().err


def test_cli_bad_today_exits_2() -> None:
    proc = subprocess.run(
        [sys.executable, "-m", "members.hoanganhtu0922.w3.cli", str(SAMPLE),
         "--hours", "2", "--today", "not-a-date"],
        capture_output=True, text=True, cwd=BOOTCAMP,
    )
    assert proc.returncode == 2
