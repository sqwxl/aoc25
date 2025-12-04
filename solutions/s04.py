def parse(data: str) -> list[list[bool]]:
    return [[c == "@" for c in line] for line in data.splitlines()]


def neighbors(grid: list[list[bool]], h: int, w: int, i: int, j: int):
    count = 0

    for k in range(i - 1, i + 2):
        if k < 0 or k >= h:
            continue
        for l in range(j - 1, j + 2):
            if l < 0 or l >= w:
                continue
            if k == i and l == j:
                continue
            if grid[k][l]:
                count += 1

    return count


def a(data: str):
    grid = parse(data)
    h, w = len(grid), len(grid[0])

    count = 0

    for i in range(0, h):
        for j in range(0, w):
            if not grid[i][j]:
                continue
            if neighbors(grid, h, w, i, j) < 4:
                count += 1

    return count


def b(data: str):
    pass
