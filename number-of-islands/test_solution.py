import random
import sys

import pytest

from solution import bfs, count_islands, dfs_recursive, dfs_stack

FLOODS = [bfs, dfs_stack, dfs_recursive]

GRID = [list(row) for row in (
    "1100011",
    "1110001",
    "0110100",
    "0000110",
    "1000010",
)]


def reference(grid):
    """Union-find: an independent way to count connected land."""
    rows, cols = len(grid), len(grid[0]) if grid else 0
    parent = {(r, c): (r, c) for r in range(rows) for c in range(cols) if grid[r][c] == "1"}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for r, c in parent:
        for nb in ((r + 1, c), (r, c + 1)):
            if nb in parent:
                parent[find((r, c))] = find(nb)
    return len({find(x) for x in parent})


@pytest.mark.parametrize("flood", FLOODS)
def test_video_grid(flood):
    assert count_islands(GRID, flood) == 4


@pytest.mark.parametrize("flood", FLOODS)
@pytest.mark.parametrize("grid, want", [
    ([], 0),
    ([[]], 0),
    ([["0"]], 0),
    ([["1"]], 1),
    ([list("101"), list("010"), list("101")], 5),   # diagonals do not connect
    ([list("10"), list("01")], 2),
    ([list("111"), list("111")], 1),
])
def test_edges(flood, grid, want):
    assert count_islands(grid, flood) == want


@pytest.mark.parametrize("flood", FLOODS)
def test_fuzz_against_union_find(flood):
    rng = random.Random(7)
    for _ in range(2000):
        rows, cols = rng.randint(1, 9), rng.randint(1, 9)
        p = rng.random()
        grid = [["1" if rng.random() < p else "0" for _ in range(cols)] for _ in range(rows)]
        assert count_islands(grid, flood) == reference(grid)


def test_recursive_dfs_hits_the_recursion_limit():
    """A 100 x 100 all-land grid needs far more than Python's default 1,000 frames."""
    grid = [["1"] * 100 for _ in range(100)]
    assert sys.getrecursionlimit() == 1000
    with pytest.raises(RecursionError):
        count_islands(grid, dfs_recursive)
    assert count_islands(grid, bfs) == 1
    assert count_islands(grid, dfs_stack) == 1
