from functools import reduce
from operator import mul

type Vec3 = tuple[int, int, int]


def parse(data: str) -> list[Vec3]:
    return [tuple(int(i) for i in line.split(",")[:3]) for line in data.splitlines()]  # pyright: ignore[reportReturnType]


def dist_sq(a: Vec3, b: Vec3) -> int:
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2


class DisjointSet:
    def __init__(self, items: list[Vec3]):
        self.parents = {i: i for i in items}
        self.ranks = {i: 0 for i in items}

    def find(self, i: Vec3):
        if self.parents[i] != i:
            self.parents[i] = self.find(self.parents[i])
        return self.parents[i]

    def union(self, a, b) -> bool:
        a, b = self.find(a), self.find(b)

        if a == b:
            return False

        if self.ranks[a] < self.ranks[b]:
            a, b = b, a

        self.parents[b] = a

        if self.ranks[a] == self.ranks[b]:
            self.ranks[a] += 1

        return True


def a(data: str):
    points = parse(data)
    pairs = [(dist_sq(a, b), a, b) for i, a in enumerate(points[:-1]) for b in points[i + 1 :]]
    pairs.sort()

    ds = DisjointSet(points)

    for _, a, b in pairs[:1000]:
        ds.union(a, b)

    sizes: dict[Vec3, int] = {}

    for p in points:
        root = ds.find(p)
        sizes[root] = sizes.get(root, 0) + 1

    largest = sorted(sizes.values(), reverse=True)

    return reduce(mul, largest[:3])


def b(data: str):
    points = parse(data)
    pairs = [(dist_sq(a, b), a, b) for i, a in enumerate(points[:-1]) for b in points[i + 1 :]]
    pairs.sort()

    ds = DisjointSet(points)

    n_sets = len(points)

    for _, a, b in pairs:
        if ds.union(a, b):
            n_sets -= 1
        if n_sets == 1:
            return a[0] * b[0]
