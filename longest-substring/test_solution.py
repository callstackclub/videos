import pytest
from solution import longest_substring_bruteforce, longest_substring_window

@pytest.mark.parametrize("func", [longest_substring_bruteforce, longest_substring_window])
def test_examples(func):
    assert func("abcabcbb") == 3
    assert func("bbbbb") == 1
    assert func("pwwkew") == 3
    assert func("") == 0
    assert func("a") == 1

def test_all_unique():
    s = "abcdef"
    assert longest_substring_window(s) == len(s)
    assert longest_substring_bruteforce(s) == len(s)

def test_random():
    s = "abcaefgh"
    expected = 7  # "bcaefgh"
    assert longest_substring_window(s) == expected
    assert longest_substring_bruteforce(s) == expected
