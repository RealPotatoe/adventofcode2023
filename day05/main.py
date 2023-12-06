from collections import defaultdict
from typing import Any


class ConversionMap:
    def __init__(self, from_attr: str, to_attr: str) -> None:
        self.from_attr = from_attr
        self.to_attr = to_attr
        self.rules = []

    def add_rule(self, rule: "ConversionMapRule") -> None:
        self.rules.append(rule)

    def convert(self, seed: "Seed") -> None:
        for rule in self.rules:
            if seed.attributes[self.from_attr] in rule:
                seed.attributes[self.to_attr] = rule.convert(
                    seed.attributes[self.from_attr]
                )
                return

        seed.attributes[self.to_attr] = seed.attributes[self.from_attr]

    def convert_number(self, seed: int) -> int:
        for rule in self.rules:
            if seed in rule:
                return rule.convert(seed)

        return seed


class ConversionMapRule:
    def __init__(self, dest_start: int, src_start: int, range: int) -> None:
        self.dest_start = dest_start
        self.src_start = src_start
        self.range = range

    def convert(self, seed: int) -> int:
        return self.dest_start + (seed - self.src_start)

    def __contains__(self, seed: int) -> bool:
        return self.src_start <= seed < self.src_start + self.range


class Seed:
    def __init__(self, seed_num: int, range: int) -> None:
        self.seed_num = seed_num
        self.range = range
        self.attributes = defaultdict(int)
        self.attributes["seed"] = seed_num

    def __repr__(self) -> str:
        return f"Seed({self.seed_num}, {self.range})"

    def __contains__(self, seed_num: int) -> bool:
        return self.seed_num <= seed_num < self.seed_num + self.range


def populate_conversion_maps(input_data: Any) -> list[ConversionMap]:
    conversion_maps = []
    input_data = input_data[2:]

    for line in input_data:
        if not line:
            continue

        if line[0].isalpha():
            from_attr, _, to_attr = line.split()[0].split("-")
            conversion_maps.append(ConversionMap(from_attr, to_attr))
            continue

        dest_start, src_start, rng = [int(x) for x in line.split()]
        conversion_maps[-1].add_rule(ConversionMapRule(dest_start, src_start, rng))

    return conversion_maps


def populate_reverse_conversion_maps(conversion_maps: list[ConversionMap]) -> None:
    reverse_conversion_maps = []
    for conversion_map in conversion_maps[::-1]:
        reverse_conversion_map = ConversionMap(
            conversion_map.to_attr, conversion_map.from_attr
        )

        for rule in conversion_map.rules:
            reverse_conversion_map.add_rule(
                ConversionMapRule(rule.src_start, rule.dest_start, rule.range)
            )

        reverse_conversion_maps.append(reverse_conversion_map)

    return reverse_conversion_maps


def part1(input_data: Any) -> int:
    # Populate seeds
    seeds = [
        Seed(int(seed_num), 1)
        for seed_num in input_data[0].split(":")[1].strip().split()
    ]

    # Populate conversion maps

    conversion_maps = populate_conversion_maps(input_data)

    # Convert seeds

    for conversion_map in conversion_maps:
        for seed in seeds:
            conversion_map.convert(seed)

    min_attribute = min(
        [seed.attributes[conversion_maps[-1].to_attr] for seed in seeds]
    )
    return min_attribute


def part2(input_data: Any) -> int:
    # Populate seeds
    seeds_data = input_data[0].split(":")[1].strip().split()
    tuple_list = [
        (seeds_data[i], seeds_data[i + 1]) for i in range(0, len(seeds_data), 2)
    ]
    initial_seeds = [Seed(int(seed_num), int(range)) for seed_num, range in tuple_list]

    # Populate conversion maps

    conversion_maps = populate_conversion_maps(input_data)

    reverse_conversion_maps = populate_reverse_conversion_maps(conversion_maps)

    # Backtrack seeds

    MAX_VALUE = 486613012
    initial_value = 0
    tmp = 1
    while True:
        value = initial_value

        for reverse_conversion_map in reverse_conversion_maps:
            value = reverse_conversion_map.convert_number(value)

        if any([value in seed for seed in initial_seeds]):
            break

        percent = (initial_value / MAX_VALUE) * 100
        if percent > tmp:
            tmp += 0.01
            print(f"{percent:.2f}%")
        initial_value += 1

    return initial_value


def main():
    input_file_path = "day05/input.txt"

    with open(input_file_path, "r") as file:
        input_data = file.read().splitlines()

    solution1 = part1(input_data)
    print("Part one:", solution1)

    solution2 = part2(input_data)
    print("Part two:", solution2)


if __name__ == "__main__":
    main()
