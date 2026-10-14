def insertion_sort(arr: list[int]) -> list[int]:
    """Sort a list of numbers in-place using insertion sort and return the sorted list.

    Difference from C++:
    In C++, std::vector<int> requires explicit type declarations, manual memory management
    under the hood, and a rigid type signature. In Python, lists are dynamic references,
    bounds-checking is enforced at runtime, and returning the list reference allows
    chaining without separate function signatures.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
