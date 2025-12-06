from operator import add, mul
from re import findall


def op(char: str):
    match char:
        case "+":
            return add
        case "*":
            return mul
    raise


def compute(problem):
    nums, op = problem

    res = nums[0]
    for n in nums[1:]:
        res = op(res, n)

    return res


def parse_a(data: str):
    lines = data.splitlines()
    ops = [op(c) for c in findall(r"\+|\*", lines.pop())]

    numbers = [[int(n) for n in findall(r"\d+", line)] for line in lines]

    problems = list(zip(zip(*numbers), ops))

    return problems


def parse_b(data: str):
    lines = data.splitlines()
    ops = [op(c) for c in reversed(findall(r"\+|\*", lines.pop()))]

    h = len(lines)
    w = len(lines[0])

    numbers = [[]]

    for j in reversed(range(w)):
        n = ""
        for i in range(h):
            c = lines[i][j]
            if c != " ":
                n += c
        if n:
            numbers[-1].append(int(n))
        elif numbers[-1]:
            numbers.append([])

    problems = list(zip(numbers, ops))

    return problems


def a(data: str):
    problems = parse_a(data)
    return sum(compute(p) for p in problems)


def b(data: str):
    problems = parse_b(data)
    return sum(compute(p) for p in problems)
