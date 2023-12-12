import time
from functools import cache
from typing import List


def count_valid_patterns(springs: List[str], contiguous_broken: List[int]):
    @cache
    def dp(pos: int, broken_idx: int, result: int = 0) -> int:
        # We have reached the end of the springs.
        if pos >= len(springs):
            # If we have also reached the end of the contiguous broken list,
            # then we have found a valid pattern. Otherwise, we have not.
            return broken_idx == len(contiguous_broken)

        # Fork A: Continue with the next spring.
        # If we land on a workign or unknown spring, we can continue to the next spring.
        if springs[pos] in ".?":
            result += dp(pos + 1, broken_idx)

        # When we went through all the contiguous broken springs, we can return the result.
        if broken_idx == len(contiguous_broken):
            return result

        # Fork B: Place the next block of contiguous broken springs, if possible.
        # We check if we can place the next block of contiguous broken springs.
        # If we can, we continue with the next spring after the contiguous broken springs.
        if (
            springs[pos] in "#?"
            and (
                pos + contiguous_broken[broken_idx] <= len(springs)
                and "." not in springs[pos : pos + contiguous_broken[broken_idx]]
            )
            and (
                pos + contiguous_broken[broken_idx] == len(springs)
                or "#" not in [springs[pos + contiguous_broken[broken_idx]]]
            )
        ):
            result += dp(pos + contiguous_broken[broken_idx] + 1, broken_idx + 1)

        # Fially we return the result.
        return result

    return dp(0, 0)


def main():
    with open("day12/input.txt") as f:
        input_data = f.read().splitlines()

    condition_records = [
        (list(springs), list(map(int, contiguous_broken.split(","))))
        for line in input_data
        for springs, contiguous_broken in [line.split()]
    ]

    for idx, pair in enumerate(condition_records):
        condition_records[idx][0].append("?")
        condition_records[idx] = (pair[0] * 5, pair[1] * 5)
        condition_records[idx][0].pop()

    start_time = time.time()

    sum_of_valid_patterns = sum(
        count_valid_patterns(springs, contiguous_broken)
        for springs, contiguous_broken in condition_records
    )

    end_time = time.time()

    print("Part one:", sum_of_valid_patterns)
    print("Runtime:", end_time - start_time, "seconds")


if __name__ == "__main__":
    main()
