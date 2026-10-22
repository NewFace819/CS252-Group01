"""Verify the actual package command required by W2-5."""

from pathlib import Path
import subprocess
import sys


def test_module_command_prints_sample_tasks():
    bootcamp = Path(__file__).resolve().parents[3]
    result = subprocess.run(
        [sys.executable, "-m", "members.vbthg.w2"],
        cwd=bootcamp, capture_output=True, text=True, timeout=10, check=True,
    )
    assert result.stderr == ""
    assert result.stdout.splitlines() == [
        "DS exam: importance=5, effort=6 h, deadline=2026-10-30",
        "Assignment: importance=4, effort=1.5 h, deadline=2026-10-27",
    ]
