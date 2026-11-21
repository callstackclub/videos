def binary_search(a: list[int], target: int) -> int:
    """Closed interval [lo, hi]: return an index of target in sorted a, or -1."""
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if a[mid] == target:
            return mid
        if a[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def search_first(a: list[int], target: int) -> int:
    """Half-open interval [lo, hi): return the FIRST index of target in sorted a, or -1."""
    lo, hi = 0, len(a)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if a[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo if lo < len(a) and a[lo] == target else -1
