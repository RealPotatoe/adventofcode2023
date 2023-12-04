from collections import defaultdict
from typing import List


class Scratchcard:
    def __init__(self, card_id: int, winning_numbers: List[int], scratch_numbers: List[int]):
        self.card_id = card_id
        self.winning_numbers = winning_numbers
        self.scratch_numbers = scratch_numbers
        self.value = 0

    def get_matching_numbers(self) -> int:
        matching_numbers = 0
        for scratch_number in self.scratch_numbers:
            if scratch_number in self.winning_numbers:
                matching_numbers += 1
        return matching_numbers

    def get_value(self) -> int:
        self.value = 0
        for scratch_number in self.scratch_numbers:
            if scratch_number in self.winning_numbers:
                if self.value == 0:
                    self.value = 1
                else:
                    self.value *= 2
        return self.value


def main():
    scratchcard_table = [
        "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
        "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
        "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
        "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
        "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
        "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
    ]

    with open("day04/input.txt", "r") as file:
        scratchcard_table = file.read().splitlines()

    scratchcards = [
        Scratchcard(
            int(scratchcard.split(":")[0].split()[1]),
            [int(num) for num in scratchcard.split(":")[1].split("|")[0].split()],
            [int(num) for num in scratchcard.split(":")[1].split("|")[1].split()],
        )
        for scratchcard in scratchcard_table
    ]

    # Part one

    sum_of_values = sum(scratchcard.get_value() for scratchcard in scratchcards)

    print("Part one:", sum_of_values)

    # Part two

    scratchcards_dict = {scratchcard.card_id: 1 for scratchcard in scratchcards}

    for scratchcard in scratchcards:
        matching_numbers = scratchcard.get_matching_numbers()
        if matching_numbers > 0:
            for i in range(1, matching_numbers + 1):
                scratchcards_dict[scratchcard.card_id + i] += scratchcards_dict[scratchcard.card_id]

    total_cards = sum(scratchcards_dict.values())

    print("Part two:", total_cards)


if __name__ == "__main__":
    main()
