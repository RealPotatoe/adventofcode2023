from typing import List


def find_mirror_position(pattern: List[str]) -> int | None:
    for i in range(1, len(pattern)):
        for n, row in enumerate(pattern):
            if n == i:
                return i
            mirrored = i * 2 - 1 - n
            if mirrored < len(pattern) and row != pattern[mirrored]:
                break


def flip(pattern: List[str]) -> List[str]:
    return ["".join(chars) for chars in zip(*pattern)]


def find_mirror(pattern: List[str]) -> int | None:
    horizontal_mirror = find_mirror_position(pattern)
    if horizontal_mirror:
        return 100 * horizontal_mirror

    return find_mirror_position(flip(pattern))


def find_smudged_mirror_position(pattern: List[str]) -> int | None:
    for i in range(1, len(pattern)):
        difference = 0
        for n, row in enumerate(pattern):
            if n == i and difference == 1:
                return i
            mirrored = i * 2 - 1 - n
            if mirrored < len(pattern):
                difference += sum(
                    1 for char1, char2 in zip(row, pattern[mirrored]) if char1 != char2
                )
                if difference > 1:
                    break


def find_smudged_mirror(pattern: List[str]) -> int | None:
    horizontal_mirror = find_smudged_mirror_position(pattern)
    if horizontal_mirror:
        return 100 * horizontal_mirror

    return find_smudged_mirror_position(flip(pattern))


def main():
    with open("day13/input.txt") as f:
        input_data = f.read().splitlines()

    patterns: List[List[List[str]]] = [[]]

    while input_data:
        line = input_data.pop(0)
        if not line:
            patterns.append([])
            continue
        patterns[-1].append(list(line))

    sum_of_lines = sum([find_mirror(pattern) for pattern in patterns])
    print("Part one:", sum_of_lines)

    sum_of_lines_smudged = sum([find_smudged_mirror(pattern) for pattern in patterns])
    print("Part two:", sum_of_lines_smudged)


if __name__ == "__main__":
    main()
