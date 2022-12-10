from deck import Deck
from human import Human
from croupier import Croupier
from exceptions import GaveOverHumanEmptyWallet
from tkinter import *


class Game:
    STOP_ADD_CROUPIER = 17
    BLACK_JACK = 21
    AMOUNT_OF_BOXES = 2
    DICTIONARY_AWARDS = {
        "1": 0,
        "2": 1,
        "3": 2.5,
        "4": 2,
        "5": 0.5
    }
    VALUE_OF_BET = {
        "50": 50,
        "100": 100,
        "500": 500,
        "1000": 1000,
        "2002": 2002
    }

    def __init__(self, list_of_frames):
        self.list_of_frames = list_of_frames
        self.frame_of_results = self.list_of_frames[2]
        self.frame_table = self.list_of_frames[1]
        self.frame_of_buttons = self.list_of_frames[0]
        self.frame_of_results.set_parent(self)
        self.frame_of_buttons.set_parent(self)
        self.top_table = None
        self.middle_table = None
        self.bottom_table = None
        self.create_frames_in_table()
        self.deck = Deck(self.list_of_frames)
        self.human = Human(self.deck, self.list_of_frames, self.middle_table)
        self.croupier = Croupier(self.deck, self.list_of_frames, self.top_table)
        self.mode_split = False
        self.deck.insert_cards()
        self.initialization()
        self.winner = None
        self.winnerbox1 = None
        self.winnerbox2 = None

    def create_frames_in_table(self):
        self.top_table = Frame(self.frame_table, bg="#166B37")
        self.middle_table = Frame(self.frame_table, bg="grey")
        self.top_table.pack(fill=BOTH, expand=True)
        self.middle_table.pack(fill=BOTH, expand=True)
        self.top_table.pack_propagate(False)
        self.middle_table.pack_propagate(False)

    def initialization(self):
        self.frame_of_results.all_money_label.configure(text=f"All money: {self.human.get_all_money()}")
        self.frame_of_results.update_labels()

    def hit(self):
        self.human.insert_cards(1)
        self.human.display_cards()
        self.print_deck_of_player()

    def hit_second_box(self):
        self.human.insert_cards(1, self.human.deck_of_player2_after_split,
                                self.human.list_of_sum2_after_split,
                                self.human.amount_of_cards2_after_split)
        self.print_deck_of_player()
        self.human.display_cards_after_split()

    def stand(self, box=""):
        while self.croupier.get_best_value() < self.STOP_ADD_CROUPIER:
            self.croupier.insert_cards(1)
        self.print_deck_of_player()
        self.croupier.display_cards()
        self.check_result(self.human.get_best_value(), box)

    def double(self):
        self.make_bet(self.human.get_value_of_bet())
        self.frame_of_results.all_money_label.configure(text=f"All money: {self.human.get_all_money()}")
        self.human.insert_cards(1)
        self.human.display_cards()
        if self.human.check_max_value() > self.BLACK_JACK:
            self.print_deck_of_player()
            self.human.display_cards()
            self.check_result(self.human.get_best_value())
        else:
            self.stand()

    def split(self):
        self.bottom_table = Frame(self.frame_table, bg="#166B37")
        self.bottom_table.pack(fill=BOTH, expand=True)
        self.bottom_table.pack_propagate(False)
        self.human.set_parent_bottom_table(self.bottom_table)
        self.mode_split = True
        self.human.split_deck()
        self.print_deck_of_player()

    def blackjack(self):
        if self.human.get_best_value() == self.BLACK_JACK and self.human.amount_of_cards == 2:
            list_of_ten_or_eleven = [10, 11]
            if self.croupier.get_best_value() not in list_of_ten_or_eleven:
                self.winner = "HUMAN WIN"
                print("HUMAN WIN")
                self.get_standard_award("3")
            if self.croupier.deck_of_player.cards[0].get_value() in [10, 11]:
                self.croupier.insert_cards(1)
                self.croupier.display_cards()
                if self.croupier.get_best_value() == self.BLACK_JACK:
                    self.print_deck_of_player()
                    self.winner = "DRAW"
                    print("DRAW")
                    self.get_standard_award("2")
                else:
                    self.print_deck_of_player()
                    self.winner = "HUMAN WIN"
                    print("HUMAN WIN")
                    self.get_standard_award("3")
        else:
            print("You have not BlackJack")

    def check_split(self):
        if (self.human.amount_of_cards == 2 and
                self.human.deck_of_player.cards[0].get_figure() == self.human.deck_of_player.cards[1].get_figure()):
            return False
        return True

    def check_result(self, human_result, box="", secondbox=False):
        win = None
        if human_result > self.BLACK_JACK:
            win = "HUMAN LOST"
            print("HUMAN LOST", box)
            self.get_standard_award("1")
        elif self.croupier.get_best_value() > self.BLACK_JACK:
            win = "HUMAN WIN"
            print("HUMAN WIN", box)
            self.get_standard_award("4")
        elif self.croupier.get_best_value() == human_result:
            win = "DRAW"
            print("DRAW", box)
            self.get_standard_award("2")
        elif human_result > self.croupier.get_best_value():
            win = "HUMAN WIN"
            print("HUMAN WIN", box)
            self.get_standard_award("4")
        elif human_result < self.croupier.get_best_value():
            win = "HUMAN LOST"
            print("HUMAN LOST", box)
            self.get_standard_award("1")

        if self.mode_split:
            if not secondbox:
                self.winnerbox1 = win
            else:
                self.winnerbox2 = win
        else:
            self.winner = win

    @staticmethod
    def print_deck(deck: Deck):
        deck.print_card()

    def print_deck_of_player(self):
        if not self.mode_split:
            self.human.print_deck_of_player("human:    ")
        else:
            self.human.print_split_deck("human:    ")
        self.croupier.print_deck_of_player("croupier: ")

    def insurance(self):
        if self.croupier.get_best_value() == 11 and self.croupier.amount_of_cards == 1:
            self.frame_of_buttons.insurance_button.configure(state=NORMAL)
            self.frame_of_buttons.hit_button.configure(state=NORMAL)
            return True
        else:
            self.human.insert_cards(2)
            self.human.display_cards()
            self.check_conditions_buttons()
            return False

    def first_hand(self):
        self.croupier.insert_cards(1)
        self.croupier.display_cards()
        self.insurance()

    def make_bet(self, value=50):
        print("make bet: ", value)
        self.human.update_debt_of_human(value)

    def get_standard_award(self, mode: str):
        self.human.add_award(self.DICTIONARY_AWARDS[mode] * self.human.get_value_of_bet())
        print(self.human.get_all_money())

    def next_game(self):
        for widget in self.top_table.winfo_children():
            if "Croupier" not in widget.cget("text"):
                widget.destroy()
        for widget in self.middle_table.winfo_children():
            if "Human" not in widget.cget("text"):
                widget.destroy()
        if isinstance(self.bottom_table, Frame):
            self.bottom_table.destroy()
        del self.deck
        self.deck = Deck(self.list_of_frames)
        self.deck.insert_cards()
        self.initialization()
        self.human.default_parameters(self.deck)
        self.croupier.default_parameters(self.deck)
        if self.human.all_money <= 0:
            raise GaveOverHumanEmptyWallet("Game over, your wallet is empty!")
        self.frame_of_results.button_confirm.configure(state=NORMAL)
        self.frame_of_buttons.hit_button.configure(state=DISABLED)
        self.frame_of_buttons.stand_button.configure(state=DISABLED)
        self.frame_of_buttons.double_button.configure(state=DISABLED)
        self.frame_of_buttons.split_button.configure(state=DISABLED)
        self.frame_of_buttons.blackjack_button.configure(state=DISABLED)
        self.frame_of_buttons.insurance_button.configure(state=DISABLED)
        self.frame_of_buttons.split_mode = 0
        self.mode_split = False

    def check_conditions_buttons(self):
        self.frame_of_buttons.hit_button.configure(state=NORMAL)
        self.frame_of_buttons.stand_button.configure(state=NORMAL)
        self.frame_of_buttons.double_button.configure(state=NORMAL)
        if not self.check_split():
            self.frame_of_buttons.split_button.configure(state=NORMAL)
        else:
            self.frame_of_buttons.split_button.configure(state=DISABLED)
        if self.human.get_best_value() == self.BLACK_JACK and self.human.amount_of_cards == 2:
            self.frame_of_buttons.blackjack_button.configure(state=NORMAL)
        else:
            self.frame_of_buttons.blackjack_button.configure(state=DISABLED)


if __name__ == "__main__":
    game = Game()
    game.initialization()
