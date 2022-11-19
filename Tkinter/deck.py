from card import Card
import random
from exceptions import NotEnoughCards
import os
from word2number import w2n
from PIL import ImageTk, Image


class Deck:
    PATH_ICONS = "C:\\Users\\Sebastian\\BlackJack\\Tkinter\\icons"

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
        self.colour = ["Clubs", "Diamonds", "Hearts", "Spades"]
        self.figure = ["2", "3", "4", "5", "6", "7",
                       "8", "9", "10", "J", "Q", "K", "A"]
        self.direction = os.listdir(self.PATH_ICONS)

    def insert_cards(self):
        for fig in self.figure:
            for col in self.colour:
                self.cards.append(Card(fig, col))
                self.cards[-1].set_value(self.VALUES[fig])
                self.insert_image(card=self.cards[-1])
        random.shuffle(self.cards)

    def insert_image(self, card: Card):
        for file in self.direction:
            full_path = self.PATH_ICONS + "\\" + file
            try:
                if w2n.word_to_num(file) == int(card.get_figure()) and card.get_colour() in file:
                    card.set_image(full_path)
                    self.direction.remove(file)
                    return
            except ValueError:
                if file.split(" ")[0][0] == card.get_figure() and card.get_colour() in file:
                    card.set_image(full_path)
                    self.direction.remove(file)
                    return

    def print_card(self):
        for card in self.cards:
            print(card)
        # print(*tuple(self.cards))

    def give_card(self):
        try:
            return self.cards.pop()
        except IndexError:
            raise NotEnoughCards("Not enough cards in deck")
