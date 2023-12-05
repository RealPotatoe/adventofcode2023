from collections import defaultdict


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


class ConversionMapRule:
    def __init__(self, dest_start: int, src_start: int, rng: int) -> None:
        self.dest_start = dest_start
        self.src_start = src_start
        self.rng = rng

    def convert(self, seed: int) -> int:
        return self.dest_start + (seed - self.src_start)

    def __contains__(self, seed: int) -> bool:
        return self.src_start <= seed < self.src_start + self.rng


class Seed:
    def __init__(self, seed_num: int) -> None:
        self.seed_num = seed_num
        self.attributes = defaultdict(int)
        self.attributes["seed"] = seed_num


def main():
    input_file_path = "day05/input.txt"

    with open(input_file_path, "r") as file:
        input_data = file.read().splitlines()

    # Populate seeds
    seeds = [
        Seed(int(seed_num)) for seed_num in input_data[0].split(":")[1].strip().split()
    ]

    conversion_maps = []
    input_data = input_data[2:]

    # Populate conversion maps
    for line in input_data:
        if not line:
            continue

        if line[0].isalpha():
            from_attr, _, to_attr = line.split()[0].split("-")
            conversion_maps.append(ConversionMap(from_attr, to_attr))
            continue

        dest_start, src_start, rng = [int(x) for x in line.split()]
        conversion_maps[-1].add_rule(ConversionMapRule(dest_start, src_start, rng))

    for conversion_map in conversion_maps:
        for seed in seeds:
            conversion_map.convert(seed)

    min_attribute = min(
        [seed.attributes[conversion_maps[-1].to_attr] for seed in seeds]
    )
    print("Part 1:", min_attribute)


if __name__ == "__main__":
    main()
