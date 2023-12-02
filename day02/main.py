import functools
from typing import Dict, List


def is_game_possible(game: str, cubes: Dict[str, int]) -> bool:
    game_parts = [
        part.strip().split(",") for part in game.split(":")[1].strip().split(";")
    ]
    for game_part in game_parts:
        for cube in game_part:
            count, color = cube.strip().split()
            if cubes.get(color, 0) < int(count):
                return False
    return True


def sum_possible_game_ids(games: List[str], cubes: Dict[str, int]) -> int:
    possible_game_ids = []
    for game in games:
        game_id = int(game.split(":")[0].split()[1])
        if is_game_possible(game, cubes):
            possible_game_ids.append(game_id)
    return sum(possible_game_ids)


def get_fewest_cubes(game: str) -> Dict[str, int]:
    game_parts = [
        part.strip().split(",") for part in game.split(":")[1].strip().split(";")
    ]
    fewest_cubes = {}
    for game_part in game_parts:
        for cube in game_part:
            count, color = cube.strip().split()
            if (
                fewest_cubes.get(color, 0) < int(count)
                or fewest_cubes.get(color, 0) == 0
            ):
                fewest_cubes[color] = int(count)
    return fewest_cubes


def sum_power_cubes(games: List[str]) -> int:
    power_cubes = []
    for game in games:
        fewest_cubes = get_fewest_cubes(game)
        power_cubes.append(
            functools.reduce(
                lambda a, b: a * b, [fewest_cubes[color] for color in fewest_cubes]
            )
        )
    return sum(power_cubes)


def main():
    input_file_path: str = "day02/input.txt"

    games = []
    with open(input_file_path, "r") as file:
        for line in file:
            games.append(line.strip())

    cubes = {"red": 12, "green": 13, "blue": 14}

    sum_ids = sum_possible_game_ids(games, cubes)
    print("Part one:", sum_ids)

    sum_power = sum_power_cubes(games)
    print("Part two:", sum_power)


if __name__ == "__main__":
    main()
