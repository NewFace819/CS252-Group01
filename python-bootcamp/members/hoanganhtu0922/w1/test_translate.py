"""Unit tests for W1-4 translate.py (gcd variant)."""

import sys
from pathlib import Path

# Ensure python-bootcamp directory is on sys.path
bootcamp_dir = Path(__file__).resolve().parents[3]
if str(bootcamp_dir) not in sys.path:
    sys.path.insert(0, str(bootcamp_dir))

from members.hoanganhtu0922.w1.translate import gcd  # noqa: E402


def test_gcd_positive():
    assert gcd(48, 18) == 6
    assert gcd(101, 103) == 1
    assert gcd(54, 24) == 6


def test_gcd_with_zero():
    assert gcd(0, 5) == 5
    assert gcd(7, 0) == 7
    assert gcd(0, 0) == 0


def test_gcd_negative():
    assert gcd(-48, 18) == 6
    assert gcd(48, -18) == 6
    assert gcd(-48, -18) == 6
