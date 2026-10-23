"""W2-4: Cross-member tests for hoanganhtu0922's W1-4 gcd (Euclid algorithm).

Reviewed by Đỗ Huy (@wiih0521).
Covers basic cases, coprimes, multiples, zeros, negative numbers,
arbitrarily large integers, and consecutive Fibonacci numbers.
"""

from members.hoanganhtu0922.w1.translate import gcd


def test_basic_gcd():
    """Greatest common divisor of typical composite integers."""
    assert gcd(48, 18) == 6
    assert gcd(54, 24) == 6
    assert gcd(100, 75) == 25


def test_coprime_numbers():
    """Coprime integers should yield a gcd of 1."""
    assert gcd(17, 19) == 1
    assert gcd(13, 27) == 1
    assert gcd(8, 9) == 1


def test_divisible_pair():
    """When a divides b or vice-versa, gcd is the smaller absolute value."""
    assert gcd(12, 36) == 12
    assert gcd(100, 25) == 25
    assert gcd(7, 49) == 7


def test_same_numbers():
    """gcd(a, a) == |a|."""
    assert gcd(42, 42) == 42
    assert gcd(1, 1) == 1


def test_with_one():
    """gcd with 1 is always 1."""
    assert gcd(1, 100) == 1
    assert gcd(50, 1) == 1


def test_with_zero():
    """Edge cases: gcd(a, 0) == |a|, gcd(0, b) == |b|, and gcd(0, 0) == 0."""
    assert gcd(0, 5) == 5
    assert gcd(7, 0) == 7
    assert gcd(0, 0) == 0


def test_negative_numbers():
    """Edge case not in standard instructor tests: negative inputs."""
    assert gcd(-48, 18) == 6
    assert gcd(48, -18) == 6
    assert gcd(-48, -18) == 6
    assert gcd(-7, 0) == 7


def test_large_integers():
    """Python arbitrary-precision integers test."""
    p1 = 10**50
    p2 = 10**30
    assert gcd(p1, p2) == 10**30


def test_consecutive_fibonacci():
    """Consecutive Fibonacci numbers are always coprime."""
    assert gcd(55, 89) == 1
    assert gcd(89, 144) == 1
