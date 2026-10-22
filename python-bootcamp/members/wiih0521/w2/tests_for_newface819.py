"""W2-4: Tests for newface819's W1-4 binary_search (reviewed by wiih0521).

At least five pytest tests covering Hải's (@NewFace819) binary_search.
Includes edge cases the instructor's tests do not cover:
- Target smaller than all elements
- Target larger than all elements
- Target between elements
- List with duplicate values
- Single-element present and absent
- Negative numbers
"""

from members.newface819.w1.translate import binary_search


def test_found_first_element():
    """Target is the very first element."""
    assert binary_search([10, 20, 30, 40, 50], 10) == 0


def test_found_last_element():
    """Target is the very last element."""
    assert binary_search([10, 20, 30, 40, 50], 50) == 4


def test_found_middle_element():
    """Target is in the middle of odd-length and even-length lists."""
    assert binary_search([1, 3, 5, 7, 9], 5) == 2
    assert binary_search([2, 4, 6, 8], 6) == 2


def test_empty_list():
    """Empty list returns -1."""
    assert binary_search([], 42) == -1


def test_single_element():
    """Single element present returns 0, absent returns -1."""
    assert binary_search([100], 100) == 0
    assert binary_search([100], 50) == -1


def test_target_outside_bounds():
    """Edge cases: target smaller than minimum or greater than maximum."""
    arr = [10, 20, 30, 40]
    assert binary_search(arr, 5) == -1
    assert binary_search(arr, 99) == -1


def test_target_missing_in_between():
    """Target falls between existing elements but is absent."""
    arr = [1, 3, 7, 15, 31]
    assert binary_search(arr, 2) == -1
    assert binary_search(arr, 10) == -1


def test_list_with_duplicates():
    """Edge case not in instructor tests: list with duplicate target values."""
    arr = [1, 2, 4, 4, 4, 9]
    res = binary_search(arr, 4)
    assert res in (2, 3, 4)


def test_negative_numbers():
    """Edge case: sorted list containing negative integers."""
    arr = [-50, -20, -10, 0, 15, 30]
    assert binary_search(arr, -20) == 1
    assert binary_search(arr, 0) == 3
    assert binary_search(arr, -100) == -1
