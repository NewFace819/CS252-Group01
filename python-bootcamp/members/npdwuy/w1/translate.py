def transpose(m: list[list[int]]) -> list[list[int]]:
    """Return the transpose of matrix m (rows become columns).

    Difference from C++: the C++ version allocates a result
    vector<vector<int>>(cols, vector<int>(rows)) and fills it with two nested
    index loops. In Python, zip(*m) pairs up the i-th element of every row,
    so each tuple it yields is already one column; no indexes or
    pre-allocation are needed.
    """
    return [list(col) for col in zip(*m)]
