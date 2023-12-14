from typing import List


def roll_stones_north(stones: List[List[str]]) -> List[List[str]]:
    rows, cols = len(stones), len(stones[0])
    rolling_stones = [0] * cols
    last_solid_stone = [-1] * cols

    for col_idx in range(cols):
        for row_idx in range(rows):
            stone = stones[row_idx][col_idx]

            if stone == "O":
                rolling_stones[col_idx] += 1

            if stone == "#" or row_idx == rows - 1:
                for i in range(last_solid_stone[col_idx] + 1, row_idx + 1):
                    if rolling_stones[col_idx] > 0:
                        stones[i][col_idx] = "O"
                        rolling_stones[col_idx] -= 1
                    elif not stones[i][col_idx] == "#":
                        stones[i][col_idx] = "."

                last_solid_stone[col_idx] = row_idx

    return stones


def count_stone_weights(stones: List[List[str]]) -> int:
    total_weight = 0
    for col_idx, col in enumerate(stones):
        for stone in col:
            if stone == "O":
                total_weight += len(stones) - col_idx
    return total_weight


def rotate_stones(stones: List[List[str]]) -> List[List[str]]:
    return [
        [stones[j][i] for j in range(len(stones) - 1, -1, -1)]
        for i in range(len(stones[0]))
    ]


def cycle_stones(stones: List[List[str]]) -> List[List[str]]:
    # North
    stones = roll_stones_north(stones)
    stones = rotate_stones(stones)

    # West
    stones = roll_stones_north(stones)
    stones = rotate_stones(stones)

    # South
    stones = roll_stones_north(stones)
    stones = rotate_stones(stones)

    # East
    stones = roll_stones_north(stones)
    stones = rotate_stones(stones)

    return stones


def part2(stones: List[List[str]]) -> int | None:
    num_iterations = 1000000000
    seen_stones = {}
    loop_start_idx = None

    for i in range(num_iterations):
        stones_str = str(stones)
        if stones_str in seen_stones:
            loop_start_idx = seen_stones[stones_str]
            break
        seen_stones[stones_str] = i

        stones = cycle_stones(stones)

    if loop_start_idx is not None:
        loop_length = len(seen_stones) - loop_start_idx
        remaining_iterations = (num_iterations - loop_start_idx) % loop_length

        for i in range(remaining_iterations):
            stones = cycle_stones(stones)

        return count_stone_weights(stones)

    return None


def main():
    with open("day14/input.txt") as f:
        input_data = f.read().splitlines()

    stones: List[List[str]] = [[stone for stone in row] for row in input_data]

    stones = roll_stones_north(stones)

    total_weight_on_north = count_stone_weights(stones)
    print("Part one:", total_weight_on_north)

    stones: List[List[str]] = [[stone for stone in row] for row in input_data]
    total_weight_on_north = part2(stones)
    print("Part two:", total_weight_on_north)


if __name__ == "__main__":
    main()
