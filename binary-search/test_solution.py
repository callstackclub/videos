import bisect
import random

import pytest
from solution import binary_search, search_first

A = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]


@pytest.mark.parametrize("fn", [binary_search, search_first])
@pytest.mark.parametrize("target,expected", [(23, 5), (2, 0), (91, 9), (40, -1), (1, -1), (100, -1)])
def test_examples(fn, target, expected):
    assert fn(A, target) == expected


@pytest.mark.parametrize("fn", [binary_search, search_first])
def test_empty_and_single(fn):
    assert fn([], 3) == -1
    assert fn([3], 3) == 0
    assert fn([3], 4) == -1


def test_half_open_returns_first_duplicate():
    assert search_first([1, 2, 2, 2, 3], 2) == 1


def test_random_against_bisect():
    rng = random.Random(42)
    for _ in range(5000):
        a = sorted(rng.choices(range(30), k=rng.randint(0, 25)))
        t = rng.randint(-2, 32)
        i = binary_search(a, t)
        assert (i == -1 and t not in a) or a[i] == t
        j = bisect.bisect_left(a, t)
        assert search_first(a, t) == (j if j < len(a) and a[j] == t else -1)
