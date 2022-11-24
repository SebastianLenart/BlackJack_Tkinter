from player import Player
from deck import Deck


class Croupier(Player):
    def __init__(self, deck: Deck, list_of_frames):
        super().__init__(deck, list_of_frames)

    def print_deck_of_player(self, who: str):
        super().print_deck_of_player(who)

    def default_parameters(self, deck):
        super().default_parameters(deck)
