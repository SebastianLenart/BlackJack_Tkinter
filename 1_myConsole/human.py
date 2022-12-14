from player import Player
from deck import Deck


class Human(Player):
    DEBT = 2000

    def __init__(self, deck: Deck):
        super().__init__(deck)
        self.all_money = self.DEBT
        self.bet = 0
        self.bet2 = 0
        self.deck_of_player2_after_split = Deck()
        self.list_of_sum2_after_split = [0]
        self.amount_of_cards2_after_split = 0

    def print_deck_of_player(self, who: str):
        print(who, "sum: ", self.list_of_sum, " => ", *self.deck_of_player.cards,
              "debt:", self.get_value_of_bet(),
              "sum:", self.get_all_money())

    def print_split_deck(self, who: str):
        print(who, "sum: ", self.list_of_sum, " => ", *self.deck_of_player.cards,
              "debt:", self.get_value_of_bet(), " sum:", self.all_money, "\n\t\t",
              self.list_of_sum2_after_split, " => ", *self.deck_of_player2_after_split.cards,
              "debt:", self.bet2)

    def split_deck(self):  # how to split two as?
        split_card = self.deck_of_player.cards.pop()
        if self.deck_of_player.cards[-1].get_figure() == "A":
            self.list_of_sum = [1, 11]
            self.list_of_sum2_after_split = [1, 11]
        else:
            self.list_of_sum[0] = int(self.list_of_sum[0] / 2)
            self.list_of_sum2_after_split = self.list_of_sum[:]  # We don't want oryginal
        self.amount_of_cards = 1
        self.deck_of_player2_after_split.cards.append(split_card)
        self.amount_of_cards2_after_split = 1

        self.bet2 = self.bet
        self.update_debt_of_human(self.bet2)
        self.bet = self.bet2

    def update_debt_of_human(self, value: int):
        if self.all_money > 0:
            self.bet += value
            self.all_money -= value

    def get_all_money(self):
        return self.all_money

    def add_award(self, value: int):
        self.all_money += value

    def get_value_of_bet(self):
        return self.bet

    def get_best_value_box2(self):
        return max(self.list_of_sum2_after_split)

    def check_max_value_2_box(self):
        return min(self.list_of_sum2_after_split)

    def default_parameters(self, deck):
        super().default_parameters(deck)
        self.bet = 0
        self.bet2 = 0
        del self.deck_of_player2_after_split
        self.deck_of_player2_after_split = Deck()
        self.list_of_sum2_after_split = [0]
        self.amount_of_cards2_after_split = 0
