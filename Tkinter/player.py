from abc import ABC, abstractmethod

from deck import Deck


class Player(ABC):
    def __init__(self, main_deck: Deck, list_of_frames):
        self.list_of_frames = list_of_frames

        self.deck_of_player = Deck(self.list_of_frames)
        self.main_deck = main_deck
        self.list_of_sum = [0]
        self.amount_of_cards = 0

    def insert_cards(self, amount, deck=None, list_sum=None, amount_cards=None):
        default = False
        if amount_cards is None:
            deck = self.deck_of_player
            list_sum = self.list_of_sum
            amount_cards = self.amount_of_cards
            default = True

        for counter in range(amount):
            deck.cards.append(self.main_deck.give_card())
            amount_cards += 1
            if deck.cards[-1].get_figure() == "A":
                list_sum = self.add_value_of_a(list_sum)
            else:
                for item in range(len(list_sum)):
                    list_sum[item] += deck.cards[-1].get_value()

            if (max(list_sum) > 21) and len(list_sum) == 2:
                list_sum.pop()

        if default:
            self.deck_of_player = deck
            self.list_of_sum = list_sum
            self.amount_of_cards = amount_cards
            # default = False

    @staticmethod
    def add_value_of_a(list_of_sum: list):
        list_of_sum[0] += 1
        if len(list_of_sum) == 2:
            list_of_sum[1] += 1

        if len(list_of_sum) == 1:
            list_of_sum.append(list_of_sum[0] - 1 + 11)
        return list_of_sum

    @abstractmethod
    def print_deck_of_player(self, who: str):
        print(who, "sum: ", self.list_of_sum, " => ", *self.deck_of_player.cards)

    @abstractmethod
    def display_cards(self):
        pass

    def get_best_value(self):
        return max(self.list_of_sum)

    def check_max_value(self):
        return min(self.list_of_sum)

    @abstractmethod
    def default_parameters(self, deck: Deck):
        del self.deck_of_player
        self.deck_of_player = Deck()
        self.list_of_sum = [0]
        self.amount_of_cards = 0
        self.main_deck = deck
