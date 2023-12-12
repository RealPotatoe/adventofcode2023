from typing import List, Set, Tuple


def expand_empty_spaces(
    space: List[List[str]], expansion_amount: int = 1
) -> List[List[str]]:
    where_to_insert = []
    for row_id, row in enumerate(space):
        if "#" in row:
            continue
        where_to_insert.append(row_id + 1)

    for row_id in where_to_insert[::-1]:
        for i in range(expansion_amount):
            space.insert(row_id + i, ["."] * len(space[0]))

    where_to_insert = []
    for col_id, col in enumerate(zip(*space)):
        if "#" in col:
            continue
        where_to_insert.append(col_id + 1)

    for col_id in where_to_insert[::-1]:
        for row in space:
            for i in range(expansion_amount):
                row.insert(col_id + i, ".")

    return space


def print_space(galaxy: List[List[str]]) -> None:
    for row in galaxy:
        print("".join(row))


def get_distance(galaxy1: Tuple[int, int], galaxy2: Tuple[int, int]) -> int:
    return abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])


def get_sum_of_distances(galaxies: List[Tuple[int, int]]) -> int:
    sum_of_distances = 0
    visited: Set[Tuple[int, int]] = set()
    for galaxy1 in galaxies:
        for galaxy2 in galaxies:
            if galaxy1 == galaxy2:
                continue
            if (galaxy2, galaxy1) in visited:
                continue
            visited.add((galaxy1, galaxy2))
            sum_of_distances += get_distance(galaxy1, galaxy2)

    return sum_of_distances


def get_sum_of_simulated_distances(space: List[List[str]], steps: int) -> int:
    galaxies = [
        (x, y)
        for x in range(len(space))
        for y in range(len(space[0]))
        if space[x][y] == "#"
    ]

    simulated_galaxies = galaxies.copy()

    for row_num, row in enumerate(space):
        if "#" in row:
            continue
        for galaxy, simulated_galaxy in zip(galaxies, simulated_galaxies):
            if galaxy[1] > row_num:
                simulated_galaxiy = (simulated_galaxy[0], simulated_galaxy[1] + steps)

    for col_num, col in enumerate(zip(*space)):
        if "#" in col:
            continue
        for galaxy, simulated_galaxy in zip(galaxies, simulated_galaxies):
            if galaxy[0] > col_num:
                simulated_galaxiy = (simulated_galaxy[0] + steps, simulated_galaxy[1])

    return get_sum_of_distances(simulated_galaxies)


def main():
    input_file = [
        "...#......",
        ".......#..",
        "#.........",
        "..........",
        "......#...",
        ".#........",
        ".........#",
        "..........",
        ".......#..",
        "#...#.....",
    ]

    # with open("day11/input.txt") as input_file:
    #     input_file = input_file.readlines()

    space = []
    for line in input_file:
        space.append(list(line.strip()))

    expanded_space = expand_empty_spaces(space)

    galaxies = [
        (x, y)
        for x in range(len(expanded_space))
        for y in range(len(expanded_space[0]))
        if expanded_space[x][y] == "#"
    ]

    sum_of_distances = get_sum_of_distances(galaxies)
    print("Part one:", sum_of_distances)

    # older_expanded_space = expand_empty_spaces(space, 1000000)

    galaxies = [
        (x, y)
        for x in range(len(space))
        for y in range(len(space[0]))
        if space[x][y] == "#"
    ]

    sum_of_distances = get_sum_of_simulated_distances(galaxies, 1000000)
    print("Part two:", sum_of_distances)


if __name__ == "__main__":
    main()
