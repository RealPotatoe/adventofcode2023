def extract_numbers_numerical(line):
    return [int(char) for char in line if char.isdigit()]


def extract_numbers_all(line):
    return [find_first_number(line), find_first_number(line, reverse=True)]


def find_first_number(line, reverse=False):
    numbers_dict = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    current_word = ""

    for char in line if not reverse else line[::-1]:
        if char.isdigit():
            return int(char)
        elif char.isalpha():
            current_word += char

        for number in numbers_dict:
            if number in (current_word if not reverse else current_word[::-1]):
                return int(numbers_dict[number])


txt = "day01/input.txt"

part1 = 0
part2 = 0

with open(txt) as f:
    for line in f:
        digits_numeric = extract_numbers_numerical(line)
        part1 += digits_numeric[0] * 10 + digits_numeric[-1]

        digits_spelled_out = extract_numbers_all(line)
        part2 += digits_spelled_out[0] * 10 + digits_spelled_out[-1]

print("Part one:", part1)
print("Part two:", part2)
