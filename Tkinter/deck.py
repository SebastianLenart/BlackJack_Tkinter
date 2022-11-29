from card import Card
import random
from exceptions import NotEnoughCards
import os
from word2number import w2n
from tkinter import *
from PIL import ImageTk, Image


class Deck():
    PATH_ICONS2 = "C:\\Users\\Sebastian\\priv_BlackJack\\icons"
    PATH_ICONS = "C:\\Users\Dell\\priv_BlackJack\\icons"

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

    def __init__(self, list_frames):
        self.list_of_frames = list_frames
        self.table_frame = self.list_of_frames[1]
        self.table_frame["bg"] = "green"
        self.cards = []
        self.value_of_cards = []
        self.colour = ["Clubs", "Diamonds", "Hearts", "Spades"]
        self.figure2 = ["2", "3", "4", "5", "6", "7",
                       "8", "9", "10", "J", "Q", "K", "A"]
        self.figure = ["A"]
        self.direction = os.listdir(self.PATH_ICONS)
        self.image_list = []

    def insert_cards(self):
        counter = [0]  # mutable type
        for fig in self.figure:
            for col in self.colour:
                self.cards.append(Card(fig, col))
                self.cards[-1].set_value(self.VALUES[fig])
                self.insert_image(self.cards[-1])
        random.shuffle(self.cards)

    def insert_image(self, card: Card):
        for file in self.direction:
            full_path = self.PATH_ICONS + "\\" + file
            try:
                if w2n.word_to_num(file) == int(card.get_figure()) and card.get_colour() in file:
                    card.set_image_path(full_path)
                    self.direction.remove(file)
                    return
            except ValueError:
                if file.split(" ")[0][0] == card.get_figure() and card.get_colour() in file:
                    card.set_image_path(full_path)
                    self.direction.remove(file)
                    return

    def appear_all_card(self):
        # scrollbar = Scrollbar(self.table_frame, orient='vertical') # command
        # scrollbar.grid(row=0, column=99, rowspan=99, sticky=NS)
        row = 0
        col = 0
        for nr, card in enumerate(self.cards):
            card.set_image(card.get_image_path())
            my_img = card.get_image()
            if nr % 7 == 0:
                row += 1
                col = 0
            col += 1
            my_label = Label(self.table_frame, image=card.get_image()).grid(row=row, column=col)

    def print_card(self):
        for card in self.cards:
            print(card)

    def give_card(self):
        try:
            return self.cards.pop()
        except IndexError:
            raise NotEnoughCards("Not enough cards in deck")
