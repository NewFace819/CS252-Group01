"""W2-4: tests for NewFace819's W1-4 binary_search."""
from members.newface819.w1.translate import binary_search


def test_finds_first_and_last() -> None:
    items = [2, 4, 6, 8, 10]
    assert binary_search(items, 2) == 0
    assert binary_search(items, 10) == 4


def test_single_element() -> None:
    assert binary_search([7], 7) == 0
    assert binary_search([7], 3) == -1
    assert binary_search([7], 9) == -1


def test_target_outside_range() -> None:
    items = [10, 20, 30]
    assert binary_search(items, 5) == -1
    assert binary_search(items, 35) == -1


def test_every_element_is_found() -> None:
    items = list(range(0, 100, 3))
    for i, x in enumerate(items):
        assert binary_search(items, x) == i


def test_negative_numbers_and_floats() -> None:
    assert binary_search([-9, -4, 0, 3], -4) == 1
    assert binary_search([0.5, 1.5, 2.5], 2.5) == 2
    assert binary_search([0.5, 1.5, 2.5], 2.0) == -1


def test_duplicates_return_a_matching_index() -> None:
    # Edge case the instructor's tests miss: with repeated keys any matching index is fine.
    items = [1, 3, 3, 3, 5]
    assert items[binary_search(items, 3)] == 3


def test_does_not_change_the_list() -> None:
    items = [1, 2, 3, 4]
    binary_search(items, 3)
    assert items == [1, 2, 3, 4]
