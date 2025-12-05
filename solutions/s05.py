def parse_ranges(data):
    bounds = []

    for range in data.splitlines():
        lo, hi = range.split("-")
        # denote lo vs hi with second element
        bounds.append((int(lo), False))
        bounds.append((int(hi), True))

    bounds = sorted(bounds)

    ranges = []
    last = None
    depth = 0

    for b, hi in bounds:
        if depth == 0:
            # account for two ranges ending/starting on the same point
            if b == last and ranges:
                ranges.pop()
                depth = 1
                continue
            last = b

        if hi:
            depth -= 1
        else:
            depth += 1

        if depth == 0:
            ranges.append((last, b))

    return ranges


def parse(data: str):
    raw_ranges, ids = data.strip().split("\n\n")

    ranges = parse_ranges(raw_ranges)

    return ranges, [int(id) for id in ids.splitlines()]


def a(data: str):
    ranges, ids = parse(data)

    count = 0

    for id in ids:
        for range in ranges:
            if id >= range[0] and id <= range[1]:
                count += 1
                break

    return count


def b(data: str):
    ranges, _ = parse(data)

    return sum(1 + b - a for a, b in ranges)
