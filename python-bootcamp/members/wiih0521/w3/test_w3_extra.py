"""Unit tests for wiih0521 W3 modules: dates, log_stats, and cli."""

from __future__ import annotations

import subprocess
import sys
from datetime import date
from pathlib import Path

import pytest

from members.wiih0521.w3.dates import parse_due
from members.wiih0521.w3.log_stats import analyse, p95

BOOTCAMP = Path(__file__).resolve().parents[3]
REF_DATE = date(2026, 10, 6)  # Tuesday


# ── W3-1: dates.parse_due ─────────────────────────────────────────────


class TestDates:
    """Tests for parse_due."""

    def test_iso_dates(self):
        assert parse_due("2026-12-25", REF_DATE) == date(2026, 12, 25)

    def test_tomorrow(self):
        assert parse_due("tomorrow", REF_DATE) == date(2026, 10, 7)
        assert parse_due("  TOMORROW  ", REF_DATE) == date(2026, 10, 7)

    def test_in_n_days(self):
        assert parse_due("in 1 day", REF_DATE) == date(2026, 10, 7)
        assert parse_due("in 5 days", REF_DATE) == date(2026, 10, 11)

    def test_weekdays_upcoming(self):
        # REF_DATE is Tuesday
        assert parse_due("wed", REF_DATE) == date(2026, 10, 7)
        assert parse_due("Wednesday", REF_DATE) == date(2026, 10, 7)
        assert parse_due("Mon", REF_DATE) == date(2026, 10, 12)
        # Same day -> next week (+7 days)
        assert parse_due("tue", REF_DATE) == date(2026, 10, 13)
        assert parse_due("Tuesday", REF_DATE) == date(2026, 10, 13)

    def test_invalid_dates(self):
        with pytest.raises(ValueError):
            parse_due("yesterday", REF_DATE)
        with pytest.raises(ValueError):
            parse_due("invalid-date", REF_DATE)
        with pytest.raises(ValueError):
            parse_due("", REF_DATE)


# ── W3-2: log_stats ───────────────────────────────────────────────────


class TestLogStats:
    """Tests for log_stats analyse and p95."""

    def test_empty_log(self):
        res = analyse([])
        assert res == {"counts": {}, "p95": {}, "slowest": None}

    def test_single_measurement(self):
        res = analyse([("api", 150)])
        assert res["counts"] == {"api": 1}
        assert res["p95"] == {"api": 150}
        assert res["slowest"] == "api"

    def test_p95_nearest_rank(self):
        # 100 values 1..100
        lats = list(range(1, 101))
        # ceil(0.95 * 100) = 95 -> 95th element is 95
        assert p95(lats) == 95

    def test_multiple_routes(self):
        data = [
            ("search", 50),
            ("search", 70),
            ("search", 60),
            ("home", 20),
            ("home", 30),
        ]
        res = analyse(data)
        assert res["counts"] == {"search": 3, "home": 2}
        assert res["slowest"] == "search"
        assert res["p95"]["home"] == 30
        assert res["p95"]["search"] == 70


# ── W3-3: cli ─────────────────────────────────────────────────────────


class TestCLI:
    """Tests for study planner CLI."""

    def test_cli_execution_with_sample(self):
        sample = BOOTCAMP / "samples" / "tasks.csv"
        res = subprocess.run(
            [
                sys.executable,
                "-m",
                "members.wiih0521.w3.cli",
                str(sample),
                "--hours",
                "2",
                "--today",
                "2026-10-26",
            ],
            capture_output=True,
            text=True,
            cwd=BOOTCAMP,
        )
        assert res.returncode == 0
        assert "Tonight (2.0 h):" in res.stdout
        assert "Assignment" in res.stdout
        assert "DS exam" in res.stdout

    def test_cli_missing_file_fails(self):
        res = subprocess.run(
            [
                sys.executable,
                "-m",
                "members.wiih0521.w3.cli",
                "nonexistent.csv",
                "--hours",
                "3",
            ],
            capture_output=True,
            text=True,
            cwd=BOOTCAMP,
        )
        assert res.returncode == 1
        assert "Error" in res.stderr
