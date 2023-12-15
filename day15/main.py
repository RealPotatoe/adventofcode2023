import re
from collections import defaultdict
from functools import reduce
from typing import Tuple


def hash(s: str) -> int:
    return reduce(lambda x, y: (x + ord(y)) * 17 % 256, s, 0)


def main():
    with open("day15/input.txt") as f:
        input_file = f.read()

    initialization_sequence = [step.strip() for step in input_file.split(",")]

    sum_of_hashes = sum(hash(step) for step in initialization_sequence)

    print(f"Part one: {sum_of_hashes}")

    boxes = defaultdict(list)

    for step in initialization_sequence:
        label, new_lense = re.split("[-=]", step)
        box = boxes[hash(label)]

        value: Tuple[str, int] = (label, int(new_lense)) if new_lense else None

        if "-" in step:
            for i, lense in enumerate(box):
                if lense[0] == label:
                    box.pop(i)
                    break
        else:
            for i, lense in enumerate(box):
                if lense[0] == label:
                    box[i] = value
                    break
            else:
                box.append(value)

    sum_of_boxes = sum(
        (num_box + 1) * (i + 1) * lense[1]
        for num_box, box in boxes.items()
        for i, lense in enumerate(box)
    )

    print(f"Part two: {sum_of_boxes}")


if __name__ == "__main__":
    main()
