"""W2-4 Tests for npdwuy's W1-4: transpose (matrix transposition).

Rotation: THA Anh reviews Đức Huy (@npdwuy).
"""

import sys
from pathlib import Path

# Ensure python-bootcamp/ is on sys.path
_BOOTCAMP = Path(__file__).resolve().parents[3]
if str(_BOOTCAMP) not in sys.path:
    sys.path.insert(0, str(_BOOTCAMP))

from members.npdwuy.w1.translate import transpose  # noqa: E402


# --- Happy-path tests ---


def test_transpose_2x3():
    matrix = [[1, 2, 3], [4, 5, 6]]
    expected = [[1, 4], [2, 5], [3, 6]]
    assert transpose(matrix) == expected


def test_transpose_3x3_square():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    expected = [
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],
    ]
    assert transpose(matrix) == expected


def test_transpose_with_negatives_and_zeros():
    matrix = [[-1, 0], [0, -5]]
    expected = [[-1, 0], [0, -5]]
    assert transpose(matrix) == expected


# --- Boundary / Dimension tests ---


def test_transpose_single_element():
    """1x1 matrix should remain 1x1."""
    assert transpose([[42]]) == [[42]]


def test_transpose_single_row():
    """1xN matrix transposes to Nx1."""
    assert transpose([[1, 2, 3, 4]]) == [[1], [2], [3], [4]]


def test_transpose_single_column():
    """Nx1 matrix transposes to 1xN."""
    assert transpose([[1], [2], [3], [4]]) == [[1, 2, 3, 4]]


def test_transpose_empty():
    assert transpose([]) == []


# --- Edge case not covered by instructor tests ---


def test_transpose_idempotent_double_transpose():
    """(M^T)^T == M for any rectangular matrix."""
    matrix = [[10, 20, 30], [40, 50, 60]]
    assert transpose(transpose(matrix)) == matrix
