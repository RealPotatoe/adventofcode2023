from typing import Any


class Race:
    def __init__(self, id, time, distance_record):
        self.id = id
        self.time = time
        self.distance_record = distance_record

    def getDistance(self, holding_time: int):
        remaining_time = self.time - holding_time
        return max(remaining_time * holding_time, 0)


def getPossibleRecords(races):
    possibe_records = [0] * len(races)

    for idx, race in enumerate(races):
        for holding_time in range(race.time + 1):
            if race.getDistance(holding_time) > race.distance_record:
                possibe_records[idx] += 1

    result = 1
    for record in possibe_records:
        result *= record

    return result


def part1(input_file: Any) -> int:
    times = [7, 15, 30]
    distances = [9, 40, 200]

    times = [int(x) for x in input_file[0].split(":")[1].split()]
    distances = [int(x) for x in input_file[1].split(":")[1].split()]

    print(times)
    print(distances)

    races = [Race(i, times[i], distances[i]) for i in range(len(times))]

    return getPossibleRecords(races)


def part2(input_file: Any) -> int:
    time = int(input_file[0].split(":")[1].replace(" ", ""))
    distance = int(input_file[1].split(":")[1].replace(" ", ""))

    races = [Race(0, time, distance)]

    return getPossibleRecords(races)


def main():
    with open("day06/input.txt") as file:
        input_data = file.read().splitlines()

    solution = part1(input_data)
    print("Part one:", solution)

    solution = part2(input_data)
    print("Part two:", solution)


if __name__ == "__main__":
    main()
