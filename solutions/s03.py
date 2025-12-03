def parse(data: str) -> list[list[int]]:
    return [[int(d) for d in bank] for bank in data.splitlines()]


def largest_digits(bank: list[int], n: int):
    digits = [0] * n  # the indices of the digits we find
    d = 0  # the digit we're looking for; 0 <= d < n

    while d < n:
        if d > 0:
            # increment the previous digit's index
            digits[d] = digits[d - 1] + 1

        i = digits[d]

        while i + n - d <= len(bank):
            if bank[i] > bank[digits[d]]:
                digits[d] = i
            i += 1

        d += 1

    return int("".join(str(bank[d]) for d in digits))


def a(data: str):
    return sum(largest_digits(d, 2) for d in parse(data))


def b(data: str):
    return sum(largest_digits(d, 12) for d in parse(data))
