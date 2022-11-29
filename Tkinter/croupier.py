from tkinter import font

from player import Player
from deck import Deck
from card import Card
from tkinter import *
from PIL import ImageTk, Image


class Croupier(Player):
    def __init__(self, deck: Deck, list_of_frames, top_table):
        super().__init__(deck, list_of_frames)
        self.top_table = top_table
        self.player_score_label = Label(self.top_table, text=f"Croupier {self.list_of_sum}", font=("Arial", 26))
        self.player_score_label.pack(side=TOP, fill="x", expand=False)
        # self.cards_label = [] # in player
        self.default_card = Card()
        # self.player_score_label.pack()

    def print_deck_of_player(self, who: str):
        super().print_deck_of_player(who)

    def display_cards(self):
        for card in self.cards_label:
            card.destroy()

        for nr, card in enumerate(self.deck_of_player.cards):
            card_label = Label(self.top_table, image=card.get_image())
            card_label.pack(side=LEFT)
            self.cards_label.append(card_label)
        if len(self.deck_of_player.cards) == 1:
            self.default_card.set_image_path(self.PATH_DEFAULT_CARD)
            default_card_label = Label(self.top_table, image=self.default_card.get_image())
            default_card_label.pack(side=LEFT)
            self.cards_label.append(default_card_label)
        self.player_score_label.configure(text=f"Croupier {self.list_of_sum}")

    def default_parameters(self, deck):
        super().default_parameters(deck)
        for widget in self.top_table.pack_slaves():
            del widget
