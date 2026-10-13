def binary_search(items, target):
    """
    Find the index of the target in the sorted list items using binary search.
    If the target is not found, return -1.
   """
    l = 0
    r = len(items) - 1
    while l <= r:
        mid = (l + r) // 2
        if items[mid] == target:
            return mid
        elif items[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1
