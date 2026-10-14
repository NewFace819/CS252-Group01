def binary_search(items, target):
    """
    Find the index of the target in the sorted list items using binary search.
    If the target is not found, return -1.
   """
    left = 0
    right = len(items) - 1
    while left <= right:
        mid = (left + right) // 2
        if items[mid] == target:
            return mid
        elif items[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
