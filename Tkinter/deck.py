from card import Card
import random
from exceptions import NotEnoughCards
import os
from word2number import w2n
from tkinter import *
from PIL import ImageTk, Image


class Deck():
    PATH_ICONS = "C:\\Users\\Sebastian\\priv_BlackJack\\icons"
    PATH_ICONS2 = "C:\\Users\Dell\\priv_BlackJack\\icons"

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

    def __init__(self, container):
        # super().__init__(container)
        self.cards = []
        self.value_of_cards = []
        self.colour = ["Clubs", "Diamonds", "Hearts", "Spades"]
        self.figure = ["2", "3", "4", "5", "6", "7",
                       "8", "9", "10", "J", "Q", "K", "A"]
        self.direction = os.listdir(self.PATH_ICONS)
        self.image_list = []
        self.main_frame = container

        buttontest = Button(self.main_frame, text="testbutton").grid(row=0, column=0)

    def insert_cards(self):
        counter = [0] # mutable type
        for fig in self.figure:
            for col in self.colour:
                self.cards.append(Card(fig, col))
                self.cards[-1].set_value(self.VALUES[fig])
                self.insert_image(self.cards[-1], counter)
        random.shuffle(self.cards)

    def insert_image(self, card: Card, counter):
        for file in self.direction:
            full_path = self.PATH_ICONS + "\\" + file
            try:
                if w2n.word_to_num(file) == int(card.get_figure()) and card.get_colour() in file:
                    card.set_image(full_path)
                    self.direction.remove(file)
                    counter[0] += 1
                    self.appear_card(full_path, *counter)

                    # print(*counter)
                    return
            except ValueError:
                if file.split(" ")[0][0] == card.get_figure() and card.get_colour() in file:
                    card.set_image(full_path)
                    self.direction.remove(file)
                    counter[0] += 1
                    self.appear_card(full_path, *counter)
                    # print(*counter)
                    return

    def appear_card(self, path: str, counter: int):
        image = Image.open(path)
        img = image.resize((int(image.width / 7), int(image.height / 7)))
        global my_img
        my_img = ImageTk.PhotoImage(img)
        self.image_list.append(my_img)
        # work below
        # my_label = Label(self, image=self.image_list[-1]).grid(row=1, column=0+(counter))
        # print(2)


    def print_card(self):
        for card in self.cards:
            print(card)
        # print(*tuple(self.cards))

    def give_card(self):
        try:
            return self.cards.pop()
        except IndexError:
            raise NotEnoughCards("Not enough cards in deck")
