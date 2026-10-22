"""
W2-4: tests for Thông's (@vbthg) W1-4 primes_up_to (sieve of Eratosthenes).
"""
from members.vbthg.w1.translate import primes_up_to


def test_small_limits():
    assert primes_up_to(2) == [2]
    assert primes_up_to(3) == [2, 3]
    assert primes_up_to(10) == [2, 3, 5, 7]


def test_below_two_has_no_primes():
    # Edge case the instructor's tests miss: 0 and negative numbers, not only 1.
    assert primes_up_to(0) == []
    assert primes_up_to(-5) == []


def test_limit_is_included_when_prime():
    assert primes_up_to(13)[-1] == 13
    assert primes_up_to(14)[-1] == 13


def test_squares_of_primes_are_removed():
    # The sieve starts at prime * prime, so 4, 9, 25 and 49 must still be crossed out.
    primes = primes_up_to(50)
    for square in (4, 9, 25, 49):
        assert square not in primes


def test_count_up_to_1000():
    primes = primes_up_to(1000)
    assert len(primes) == 168
    assert primes[-1] == 997


def test_matches_trial_division():
    def is_prime(n):
        return n >= 2 and all(n % d for d in range(2, int(n ** 0.5) + 1))

    assert primes_up_to(200) == [n for n in range(200 + 1) if is_prime(n)]
