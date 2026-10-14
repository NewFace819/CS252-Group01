"""W1-4 Translate C++ to Python."""


def gcd(a: int, b: int) -> int:
    """Return the greatest common divisor of a and b using Euclid's algorithm.

    Difference from C++:
    In C++, updating values typically requires an explicit temporary
    variable (`int temp = b; b = a % b; a = temp;`). In Python, tuple unpacking
    allows simultaneous assignment `a, b = b, a % b` without an explicit temporary variable.
    Furthermore, Python handles arbitrarily large integers without integer overflow.
    """
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def binary_search(a: list[int], key: int) -> int:
    """Find the index of key in sorted list a using binary search, or -1 if not found.

    Difference from C++:
    In C++, `lo + (hi - lo) / 2` is used to prevent potential 32-bit signed integer
    overflow when calculating the midpoint. In Python, integers have arbitrary precision
    and never overflow, making `(lo + hi) // 2` safe. Furthermore, Python lists are dynamic
    objects passed by reference without needing explicit const reference syntax.
    """
    lo = 0
    hi = len(a) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == key:
            return mid
        if a[mid] < key:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
