from collections import defaultdict
from typing import Dict, List, Tuple

import numpy as np


def part1(lr_instructions: List[int], directions: Dict[str, Tuple[str, str]]) -> int:
    start = "AAA"
    end = "ZZZ"

    current_position = start
    counter = 0
    total_steps = 0

    while current_position != end:
        print(
            f"Current position: {current_position} - {directions[current_position]}, next instruction: {lr_instructions[counter]}"
        )
        current_position = directions[current_position][lr_instructions[counter]]
        counter = (counter + 1) % len(lr_instructions)
        total_steps += 1

    return total_steps


def part2(lr_instructions: List[int], directions: Dict[str, Tuple[str, str]]) -> int:
    start = [node for node in directions if node.endswith("A")]
    end = [node for node in directions if node.endswith("Z")]

    step_count = []

    for node in start:
        counter = 0
        while node not in end:
            node = directions[node][lr_instructions[counter % len(lr_instructions)]]
            counter += 1
        step_count.append(counter)

    return np.lcm.reduce(step_count)  # Lowest common multiple of all step counts


def main() -> None:
    with open("day08/input.txt") as f:
        input_data = f.read().splitlines()

    lr_instructions = [0 if char == "L" else 1 for char in input_data[0]]

    directions = defaultdict(tuple)

    for line in input_data[2:]:
        key, value = map(str.strip, line.split("="))
        value = tuple(v.strip() for v in value[1:-1].split(","))
        directions[key] = value

    total_steps = part1(lr_instructions, directions)
    print("Part 1:", total_steps)

    ghost_steps = part2(lr_instructions, directions)
    print("Part 2:", ghost_steps)


if __name__ == "__main__":
    main()
