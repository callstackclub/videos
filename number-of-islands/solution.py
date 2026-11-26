"""Number of Islands: count groups of "1" cells joined up, down, left or right.

One outer scan finds each new island; a flood fill (BFS, stack DFS or recursive DFS)
marks the whole island as seen so it is never counted twice.
"""
from collections import deque


def neighbors(grid, r, c):
    for nr, nc in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
            if grid[nr][nc] == "1":
                yield nr, nc


def bfs(grid, r, c, seen):
    seen.add((r, c))
    queue = deque([(r, c)])
    while queue:
        cr, cc = queue.popleft()          # oldest cell first: rings
        for nb in neighbors(grid, cr, cc):
            if nb not in seen:
                seen.add(nb)              # mark when it joins the queue
                queue.append(nb)


def dfs_stack(grid, r, c, seen):
    seen.add((r, c))
    stack = [(r, c)]
    while stack:
        cr, cc = stack.pop()              # newest cell first: dives deep
        for nb in neighbors(grid, cr, cc):
            if nb not in seen:
                seen.add(nb)
                stack.append(nb)


def dfs_recursive(grid, r, c, seen):
    seen.add((r, c))
    for nb in neighbors(grid, r, c):
        if nb not in seen:
            dfs_recursive(grid, *nb, seen)


def count_islands(grid, flood=bfs):
    if not grid or not grid[0]:
        return 0
    seen, islands = set(), 0
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == "1" and (r, c) not in seen:
                islands += 1
                flood(grid, r, c, seen)
    return islands
