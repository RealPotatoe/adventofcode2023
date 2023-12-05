from collections import defaultdict


class ConversionMap:
    def __init__(self, destination_start: int, source_start: int, range: int) -> None:
        self.destination_start = destination_start
        self.source_start = source_start
        self.range = range

    def convert(self, seed: int) -> int:
        if seed not in self:
            raise ValueError(
                f"Seed {seed} is not in range {self.source_start} - {self.source_start + self.range}"
            )

        return self.destination_start + (seed - self.source_start)

    def __contains__(self, seed: int) -> bool:
        return self.source_start <= seed < self.source_start + self.range


def main():
    input_file_path = "day05/test_input.txt"

    with open(input_file_path, "r") as file:
        input_data = file.read().splitlines()

    seeds = [int(seed) for seed in input_data[0].split(":")[1].strip().split()]

    maps = defaultdict(list)

    input_data = input_data[3:]
    stage = 0

    for line in input_data:
        if line == "":
            stage += 1
            continue

        if line[0].isalpha():
            continue

        destination_start, source_start, range = [int(x) for x in line.split()]
        maps[stage].append(ConversionMap(destination_start, source_start, range))

    conversions = defaultdict(int)

    for seed in seeds:
        conversions[seed] = seed

    print("Initial state:", conversions)

    for stage in maps:
        for seed in conversions:
            conversion_found = False
            for conversion_map in maps[stage]:
                if seed in conversion_map:
                    conversions[seed] = conversion_map.convert(seed)
                    conversion_found = True
                    print(f"Stage {stage}: {seed} -> {conversions[seed]}")
                    break
            if not conversion_found:
                print(f"Stage {stage}: {seed} -> {seed} (no conversion found)")

    minimum_seed = min(conversions, key=conversions.get)

    print("Part one:", minimum_seed)


if __name__ == "__main__":
    main()
