class EngineSchematicAnalyzer:
    directions = [
        (-1, -1),  # Top-left
        (-1, 0),  # Up
        (-1, 1),  # Top-right
        (0, -1),  # Left
        (0, 1),  # Right
        (1, -1),  # Bottom-left
        (1, 0),  # Down
        (1, 1),  # Bottom-right
    ]

    def __init__(self, schematic):
        self.schematic = [list(line) for line in schematic.split("\n")]
        self.processed_locations = set()

    def calculate_sum_of_part_numbers(self):
        total_sum = 0
        for i, row in enumerate(self.schematic):
            j = 0
            while j < len(row):
                if row[j].isdigit() and (i, j) not in self.processed_locations:
                    part_number = self._get_full_part_number(i, j)
                    self.processed_locations.update(
                        (i, col_index)
                        for col_index in range(j, j + len(str(part_number)))
                    )

                    if any(
                        self._is_adjacent_to_symbol(i, col_index)
                        for col_index in range(j, j + len(str(part_number)))
                    ):
                        total_sum += part_number
                    j += len(str(part_number)) - 1
                j += 1

        return total_sum

    def calculate_sum_of_all_gear_ratios(self):
        total_sum = 0
        for i, row in enumerate(self.schematic):
            for j, char in enumerate(row):
                total_sum += self._get_gear_ratio(i, j) if char == "*" else 0

        return total_sum

    def _get_gear_ratio(self, row, col):
        adjacent_numbers = []
        for dx, dy in self.directions:
            adjacent_row, adjacent_col = row + dx, col + dy
            if 0 <= adjacent_row < len(self.schematic) and 0 <= adjacent_col < len(
                self.schematic[adjacent_row]
            ):
                if self.schematic[adjacent_row][adjacent_col].isdigit():
                    part_number = self._get_full_part_number(adjacent_row, adjacent_col)
                    if part_number not in adjacent_numbers:
                        adjacent_numbers.append(part_number)

        if len(adjacent_numbers) == 2:
            return adjacent_numbers[0] * adjacent_numbers[1]
        return 0

    def _get_full_part_number(self, row, col):
        # start with the digit at (row, col)
        number_str = self.schematic[row][col]

        # fan out to the left
        left_col = col - 1
        while left_col >= 0 and self.schematic[row][left_col].isdigit():
            number_str = self.schematic[row][left_col] + number_str
            left_col -= 1

        # fan out to the right
        right_col = col + 1
        while (
            right_col < len(self.schematic[row])
            and self.schematic[row][right_col].isdigit()
        ):
            number_str += self.schematic[row][right_col]
            right_col += 1

        return int(number_str)

    def _is_valid_symbol(self, char):
        return not (char.isdigit() or char == ".")

    def _is_adjacent_to_symbol(self, row, col):
        for dx, dy in self.directions:
            if 0 <= row + dx < len(self.schematic) and 0 <= col + dy < len(
                self.schematic[row + dx]
            ):
                if self._is_valid_symbol(self.schematic[row + dx][col + dy]):
                    return True
        return False


def main():
    with open("day03/input.txt") as file:
        engine_schematic = file.read()

    analyzer = EngineSchematicAnalyzer(engine_schematic)
    sum_of_part_numbers = analyzer.calculate_sum_of_part_numbers()
    print("Part one", sum_of_part_numbers)

    sum_of_gear_ratios = analyzer.calculate_sum_of_all_gear_ratios()
    print("Part two", sum_of_gear_ratios)


if __name__ == "__main__":
    main()
