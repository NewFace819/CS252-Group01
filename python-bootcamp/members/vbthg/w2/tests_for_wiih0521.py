"""W2-4 cross-member tests for wiih0521's W1 insertion sort.

The instructor checks only [3, 1, 2] and []. Duplicates, signed values,
already-sorted input, and the documented in-place return are additional cases.
"""

from members.wiih0521.w1.translate import insertion_sort


def test_unsorted_values():
    assert insertion_sort([3, 1, 2]) == [1, 2, 3]


def test_empty_list():
    assert insertion_sort([]) == []


def test_single_value():
    assert insertion_sort([7]) == [7]


def test_already_sorted_values():
    assert insertion_sort([-2, 0, 4, 9]) == [-2, 0, 4, 9]


def test_reverse_order():
    assert insertion_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_duplicates_are_not_dropped():
    assert insertion_sort([3, 1, 3, 1, 2]) == [1, 1, 2, 3, 3]


def test_all_equal_values():
    assert insertion_sort([2, 2, 2, 2]) == [2, 2, 2, 2]


def test_negative_zero_and_large_integers():
    assert insertion_sort([10**30, 0, -7, -(10**30), 7]) == [-(10**30), -7, 0, 7, 10**30]


def test_mutates_and_returns_the_original_list():
    values = [4, 1, 3, 2]
    result = insertion_sort(values)
    assert result is values
    assert values == [1, 2, 3, 4]
