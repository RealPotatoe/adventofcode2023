from typing import List


def part1(histories: List[List[List[int]]]):
    predictions = []

    for history in histories:
        while any(history[-1]):
            differences = []
            for i in range(1, len(history[-1])):
                differences.append(history[-1][i] - history[-1][i - 1])
            history.append(differences)

        # Predict the next value for each history
        prediction = 0
        for change_list in history:
            next_value = change_list[-1] + history[-1][-1]
            prediction += next_value

        predictions.append(prediction)

    return sum(predictions)


def main():
    with open("day09/input.txt") as f:
        input_data = f.read().splitlines()

    histories = [[[int(num) for num in line.split()]] for line in input_data]

    sum_of_predictions = part1(histories)
    print("Part one:", sum_of_predictions)

    reversed_histories = [
        [[int(num) for num in line.split()][::-1]] for line in input_data
    ]

    sum_of_predictions_backwards = part1(reversed_histories)
    print("Part two:", sum_of_predictions_backwards)


if __name__ == "__main__":
    main()
