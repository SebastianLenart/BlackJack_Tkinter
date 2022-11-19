from card import Card
import random
from exceptions import NotEnoughCards


class Deck:
    VALUES = {"2": 2,
              "3": 3,
              "4": 4,
              "5": 5,
              "6": 6,
              "7": 7,
              "8": 8,
              "9": 9,
              "10": 10,
              "J": 10,
              "Q": 10,
              "K": 10,
              "A": 11}

    def __init__(self):
        self.cards = []
        self.value_of_cards = []
        self.colour = ["trefl", "pik", "karo", "kier"]
        self.figure = ["2", "3", "4", "5", "6", "7",
                       "8", "9", "10", "J", "Q", "K", "A"]
        # self.figure = ["2"]

    def insert_cards(self):
        for fig in self.figure:
            for col in self.colour:
                self.cards.append(Card(fig, col))
                self.cards[-1].set_value(self.VALUES[fig])
        random.shuffle(self.cards)

    def print_card(self):
        for card in self.cards:
            print(card)
        # print(*tuple(self.cards))

    def give_card(self):
        try:
            return self.cards.pop()
        except IndexError:
            raise NotEnoughCards("Not enough cards in deck")
