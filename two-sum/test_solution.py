import pytest
from solution import two_sum, two_sum_brute

CASES = [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
    ([-1, -2, -3, -4, -5], -8, [2, 4]),
    ([0, 4, 3, 0], 0, [0, 3]),
    ([1, 5, 9, 2, 8], 10, [0, 2]),
]


@pytest.mark.parametrize("fn", [two_sum, two_sum_brute])
@pytest.mark.parametrize("nums,target,expected", CASES)
def test_two_sum(fn, nums, target, expected):
    assert sorted(fn(nums, target)) == expected


def test_does_not_reuse_same_element():
    assert two_sum([5, 1, 4], 10) == []
