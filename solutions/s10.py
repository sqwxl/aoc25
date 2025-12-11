type Machine = tuple[int, list[int], list[int]]


def parse(data: str) -> list[Machine]:
    machines: list[Machine] = []

    for line in data.splitlines():
        i = line.index("]")
        j = line.index("(")
        k = line.index("{")

        lights = int("".join(["1" if c == "#" else "0" for c in line[1:i]]), 2)
        buttons = [sum(int("1" + "0" * (i - int(n) - 2), 2) for n in b[1:-1].split(",")) for b in line[j:k].strip().split(" ")]
        joltages = [int(n) for n in line[k + 1 : -1].strip().split(",")]

        machines.append((lights, buttons, joltages))

    return machines


def a(data: str):
    machines = parse(data)
    total = 0

    for lights, buttons, _ in machines:
        queue = [(0, 0)]  # (state, steps)
        visited = {0}

        while queue:
            state, n = queue.pop(0)

            if state == lights:
                total += n
                break

            for b in buttons:
                s = state ^ b
                if s not in visited:
                    visited.add(s)
                    queue.append((s, n + 1))

    return total


def b(data: str):
    pass
