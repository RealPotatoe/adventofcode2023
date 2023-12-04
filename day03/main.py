class PartNumber:
    def __init__(self, value, row, start_col, end_col):
        self.value = value
        self.row = row
        self.start_col = start_col
        self.end_col = end_col
        self.engine_parts = []

    def adjacent(self, other: "EnginePart"):
        if (
            self.row == other.row
            or self.row == other.row + 1
            or self.row == other.row - 1
        ) and (other.col >= self.start_col - 1 and other.col <= self.end_col + 1):
            return True
        return False

    def add_engine_part(self, engine_part):
        if engine_part not in self.engine_parts:
            self.engine_parts.append(engine_part)

    def __str__(self) -> str:
        return f"{self.value} {self.row} {self.start_col} {self.end_col} {'Connected' if len(self.engine_parts) > 0 else 'Not connected'}"


class EnginePart:
    def __init__(self, symbol, row, col):
        self.symbol = symbol
        self.row = row
        self.col = col
        self.part_numbers = []

    def add_part_number(self, part_number):
        self.part_numbers.append(part_number)

    def __str__(self) -> str:
        return f"{self.symbol} {self.row} {self.col} {self.part_numbers}"


class EngineSchematic:
    def __init__(self, engine_schematic):
        self.engine_schematic = engine_schematic
        self.max_row = len(engine_schematic)
        self.max_col = len(engine_schematic[0])
        self.engine_parts = []
        self.part_numbers = []

    def get_data(self):
        for row in range(self.max_row):
            current_part_number = ""
            for col in range(self.max_col):
                position = self.engine_schematic[row][col]

                if not position.isdigit():
                    if current_part_number != "":
                        self.part_numbers.append(
                            PartNumber(
                                int(current_part_number),
                                row,
                                col - len(current_part_number),
                                col - 1,
                            )
                        )
                    current_part_number = ""

                    if self.is_special_symbol(position):
                        self.engine_parts.append(EnginePart(position, row, col))

                if position.isdigit():
                    current_part_number += position
            if current_part_number != "":
                self.part_numbers.append(
                    PartNumber(
                        int(current_part_number),
                        row,
                        col - len(current_part_number),
                        col - 1,
                    )
                )

        for engine_part in self.engine_parts:
            for part_number in self.part_numbers:
                if part_number.adjacent(engine_part):
                    engine_part.add_part_number(part_number)
                    part_number.add_engine_part(engine_part)

    @staticmethod
    def is_special_symbol(position):
        return not position.isdigit() and position != "."


def main():
    engine_schematic = []
    "day03/input.txt"
    with open("./day03/input.txt") as f:
        for line in f:
            engine_schematic.append(line.strip())

    # engine_schematic = [
    #     "467..114..",
    #     "...*......",
    #     "..35..633.",
    #     "......#...",
    #     "617*......",
    #     ".....+.58.",
    #     "..592.....",
    #     "......755.",
    #     "...$.*....",
    #     ".664.598..",
    # ]

    sum_of_part_numbers = 0

    engine_schematic = EngineSchematic(engine_schematic)

    engine_schematic.get_data()

    for part_number in engine_schematic.part_numbers:
        print(part_number)

    for part_number in engine_schematic.part_numbers:
        if len(part_number.engine_parts) >= 1:
            sum_of_part_numbers += part_number.value

    print("Part one:", sum_of_part_numbers)


if __name__ == "__main__":
    main()
