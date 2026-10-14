"""Member 4: the sieve of Eratosthenes in Python.

Unlike a C++ vector<bool>, Python uses a list of booleans here. A comprehension
collects the surviving indices instead of pushing them into a result vector.
"""

from math import isqrt


def primes_up_to(n: int) -> list[int]:
    """Return all primes <= n by marking multiples from each prime's square."""
    if n < 2:
        return []

    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for prime in range(2, isqrt(n) + 1):
        if is_prime[prime]:
            for multiple in range(prime * prime, n + 1, prime):
                is_prime[multiple] = False
    return [number for number in range(2, n + 1) if is_prime[number]]
