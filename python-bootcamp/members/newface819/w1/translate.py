def binary_search(items, target):
    """
    Find the index of the target in the sorted list items using binary search.
    If the target is not found, return -1.
   """
    lo = 0
    hi = len(items) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if items[mid] == target:
            return mid
        elif items[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
