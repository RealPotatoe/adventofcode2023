from collections import defaultdict
from typing import Any, List

TYPE_VALUES = {
    "Five of a kind": 7,
    "Four of a kind": 6,
    "Full house": 5,
    "Three of a kind": 4,
    "Two pair": 3,
    "One pair": 2,
    "High card": 1,
}

VALUES = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "J": 1,  # Jack is worth the least for part 2
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}


class CamelCard:
    def __init__(self, label: str) -> None:
        self.label = label

    def __repr__(self) -> str:
        return f"CamelCard({self.label})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, CamelCard):
            raise TypeError("Comparison must involve CamelCard objects")
        return self.label == other.label

    def _compare(self, other: object, op: callable) -> bool:
        if not isinstance(other, CamelCard):
            raise TypeError("Comparison must involve CamelCard objects")
        return op(VALUES[self.label], VALUES[other.label])

    def __lt__(self, other: object) -> bool:
        return self._compare(other, lambda x, y: x < y)

    def __gt__(self, other: object) -> bool:
        return self._compare(other, lambda x, y: x > y)

    def __le__(self, other: object) -> bool:
        return self._compare(other, lambda x, y: x <= y)

    def __ge__(self, other: object) -> bool:
        return self._compare(other, lambda x, y: x >= y)

    def __ne__(self, other: object) -> bool:
        return self._compare(other, lambda x, y: x != y)


class CamelDeck:
    def __init__(self, cards: List[CamelCard], bid: int) -> None:
        self.cards = cards
        self.bid = bid

    def sort(self) -> None:
        self.cards.sort(key=lambda x: x.label, reverse=True)

    def getType(self) -> int:
        card_counts = defaultdict(int)

        jack_count = 0

        for card in self.cards:
            if card.label == "J":
                jack_count += 1
            else:
                card_counts[card.label] += 1

        if 5 in card_counts.values():
            return TYPE_VALUES["Five of a kind"]

        if 4 in card_counts.values() and jack_count == 1:
            return TYPE_VALUES["Five of a kind"]

        if 3 in card_counts.values() and jack_count == 2:
            return TYPE_VALUES["Five of a kind"]

        if 2 in card_counts.values() and jack_count == 3:
            return TYPE_VALUES["Five of a kind"]

        if 1 in card_counts.values() and jack_count == 4:
            return TYPE_VALUES["Five of a kind"]

        if jack_count == 5:
            return TYPE_VALUES["Five of a kind"]

        if 4 in card_counts.values():
            return TYPE_VALUES["Four of a kind"]

        if 3 in card_counts.values() and jack_count == 1:
            return TYPE_VALUES["Four of a kind"]

        if 2 in card_counts.values() and jack_count == 2:
            return TYPE_VALUES["Four of a kind"]

        if 1 in card_counts.values() and jack_count == 3:
            return TYPE_VALUES["Four of a kind"]

        if 3 in card_counts.values() and 2 in card_counts.values():
            return TYPE_VALUES["Full house"]

        if 2 in card_counts.values() and jack_count >= 1:
            if list(card_counts.values()).count(2) == 2:
                return TYPE_VALUES["Full house"]

            if 1 in card_counts.values() and jack_count == 2:
                return TYPE_VALUES["Full house"]

            if jack_count == 3:
                return TYPE_VALUES["Full house"]

        if list(card_counts.values()).count(1) == 2 and jack_count == 3:
            return TYPE_VALUES["Full house"]

        if 3 in card_counts.values():
            return TYPE_VALUES["Three of a kind"]

        if 2 in card_counts.values() and jack_count == 1:
            return TYPE_VALUES["Three of a kind"]

        if 1 in card_counts.values() and jack_count == 2:
            return TYPE_VALUES["Three of a kind"]

        if jack_count == 3:
            return TYPE_VALUES["Three of a kind"]

        if list(card_counts.values()).count(2) == 2:
            return TYPE_VALUES["Two pair"]

        if 2 in card_counts.values():
            return TYPE_VALUES["One pair"]

        if 1 in card_counts.values() and jack_count == 1:
            return TYPE_VALUES["One pair"]

        return TYPE_VALUES["High card"]

    def __iter__(self) -> iter:
        return iter(self.cards)

    def __repr__(self) -> str:
        return f"CamelDeck({self.cards}, {self.bid})"

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, CamelDeck):
            raise TypeError("Comparison must involve CamelDeck objects")
        if self.getType() != other.getType():
            return self.getType() < other.getType()

        for card1, card2 in zip(self.cards, other.cards):
            if card1 != card2:
                return card1 < card2

        return False

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, CamelDeck):
            raise TypeError("Comparison must involve CamelDeck objects")
        if self.getType() != other.getType():
            return self.getType() > other.getType()

        for card1, card2 in zip(self.cards, other.cards):
            if card1 != card2:
                return card1 > card2

        return False

    def __le__(self, other: object) -> bool:
        if not isinstance(other, CamelDeck):
            raise TypeError("Comparison must involve CamelDeck objects")
        if self.getType() != other.getType():
            return self.getType() <= other.getType()

        for card1, card2 in zip(self.cards, other.cards):
            if card1 != card2:
                return card1 <= card2

        return True

    def __ge__(self, other: object) -> bool:
        if not isinstance(other, CamelDeck):
            raise TypeError("Comparison must involve CamelDeck objects")
        if self.getType() != other.getType():
            return self.getType() >= other.getType()

        for card1, card2 in zip(self.cards, other.cards):
            if card1 != card2:
                return card1 >= card2

        return True

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, CamelDeck):
            raise TypeError("Comparison must involve CamelDeck objects")
        if self.getType() != other.getType():
            return self.getType() == other.getType()

        for card1, card2 in zip(self.cards, other.cards):
            if card1 != card2:
                return card1 == card2

        return True

    def __ne__(self, other: object) -> bool:
        if not isinstance(other, CamelDeck):
            raise TypeError("Comparison must involve CamelDeck objects")
        if self.getType() != other.getType():
            return self.getType() != other.getType()

        for card1, card2 in zip(self.cards, other.cards):
            if card1 != card2:
                return card1 != card2

        return False


def part1(input_data: Any) -> int:
    decks = []

    for deck in input_data:
        cards, bid = deck.split()
        cards = [CamelCard(x) for x in cards]
        bid = int(bid)
        camel_deck = CamelDeck(cards, bid)
        # camel_deck.sort()
        decks.append(camel_deck)

    decks.sort()

    ranks = [0] * len(decks)

    for i in range(len(decks)):
        if i == 0:
            ranks[i] = 1
            continue

        if decks[i] == decks[i - 1]:
            ranks[i] = ranks[i - 1]

        else:
            ranks[i] = ranks[i - 1] + 1

    # print(ranks)

    deck_dict = {rank: deck for rank, deck in zip(ranks, decks)}
    for rank, deck in deck_dict.items():
        # print(f"{rank}: {deck}")
        pass

    return sum([rank * deck.bid for rank, deck in zip(ranks, decks)])


def main():
    with open("day07/input.txt") as f:
        input_data = f.read().splitlines()

    total_winnings = part1(input_data)
    print(total_winnings)


if __name__ == "__main__":
    main()
