from deck import Deck
from human import Human
from croupier import Croupier
from exceptions import GaveOverHumanEmptyWallet


class Game:
    MENU = """1.) HIT
2.) STAND
3.) DOUBLE
4.) SPLIT
5.) BLACKJACK
6.) INSURANCE
7.) EXIT
Enter your choice: 
"""
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

    def __init__(self):
        self.deck = Deck()
        self.human = Human(self.deck)
        self.croupier = Croupier(self.deck)
        self.mode_split = False
        self.finish = False

    def hit(self):
        self.human.insert_cards(1)
        self.print_deck_of_player()
        if self.human.check_max_value() > self.BLACK_JACK:
            if not self.mode_split:
                self.check_result(self.human.get_best_value(), "Box 1")
            else:
                return True
            return False

    def hit_second_box(self):
        self.human.insert_cards(1, self.human.deck_of_player2_after_split,
                                self.human.list_of_sum2_after_split,
                                self.human.amount_of_cards2_after_split)
        self.print_deck_of_player()
        if self.human.check_max_value_2_box() > self.BLACK_JACK:
            return True

    def stand(self, box=""):
        while self.croupier.get_best_value() < self.STOP_ADD_CROUPIER:
            self.croupier.insert_cards(1)
        self.print_deck_of_player()
        self.check_result(self.human.get_best_value(), box)

    def double(self):
        self.make_bet(self.human.get_value_of_bet())
        self.human.insert_cards(1)
        if self.human.check_max_value() > self.BLACK_JACK:
            self.print_deck_of_player()
            self.check_result(self.human.get_best_value())
        else:
            self.stand()

    def split(self):
        if self.check_split():
            print("Option split is not available. Must be 2 same cards")
            return
        print("Split is OK.")
        self.mode_split = True
        self.human.split_deck()
        self.print_deck_of_player()
        self.insert_card_in_split_mode()
        self.stand("Box 1")
        self.check_result(self.human.get_best_value_box2(), "Box 2")

    def blackjack(self):
        if self.human.get_best_value() == self.BLACK_JACK and self.human.amount_of_cards == 2:
            list_of_ten_or_eleven = [10, 11]
            if self.croupier.get_best_value() not in list_of_ten_or_eleven:
                print("HUMAN WIN")
                self.get_standard_award("3")
            if self.croupier.deck_of_player.cards[0].get_value() in [10, 11]:
                self.croupier.insert_cards(1)
                if self.croupier.get_best_value() == self.BLACK_JACK:
                    self.print_deck_of_player()
                    print("DRAW")
                    self.get_standard_award("2")
                else:
                    self.print_deck_of_player()
                    print("HUMAN WIN")
                    self.get_standard_award("3")
        else:
            print("You have not BlackJack")

    def insurance(self):
        if self.croupier.get_best_value() == 11 and self.croupier.amount_of_cards == 1:
            choice = input("Do you want insurance? 0-no, 1-yes: ")
            while choice not in ["0", "1"]:
                choice = input("Incorrect, Enter correct answer 0-no, 1-yes: ")
            if choice == "1":
                print("INSURANCE")
                self.get_standard_award("5")
                self.next_game()
            else:
                return
        else:
            print("Insurance is not active")

    def check_split(self):
        if (self.human.amount_of_cards == 2 and
                self.human.deck_of_player.cards[0].get_figure() == self.human.deck_of_player.cards[1].get_figure()):
            return False
        print(self.human.amount_of_cards)
        return True

    def insert_card_in_split_mode(self):
        list_of_hits = {"1": self.hit}  # the order matters!
        for counter in range(self.AMOUNT_OF_BOXES):
            condition = True
            while condition:
                select = input(f"0.) STAND \n1.) HIT\nBox {counter + 1}: Choose option: ")
                while select not in ["0", "1"]:
                    select = input(f"Try again\n0.) STAND \n1.) HIT\nBox {counter + 1}: Choose option: ")
                if select == "0":
                    condition = False
                    continue
                try:
                    list_of_hits[select]()
                except IndexError:
                    print("Out of range list. Try again")
            list_of_hits["1"] = self.hit_second_box

    def check_result(self, human_result, box=""):
        if human_result > self.BLACK_JACK:
            print("HUMAN LOST", box)
            self.get_standard_award("1")
        elif self.croupier.get_best_value() > self.BLACK_JACK:
            print("HUMAN WIN", box)
            self.get_standard_award("4")
        elif self.croupier.get_best_value() == human_result:
            print("DRAW", box)
            self.get_standard_award("2")
        elif human_result > self.croupier.get_best_value():
            print("HUMAN WIN", box)
            self.get_standard_award("4")
        elif human_result < self.croupier.get_best_value():
            print("HUMAN LOST", box)
            self.get_standard_award("1")
        else:
            return False

    def initialization(self):
        self.deck.insert_cards()

    @staticmethod
    def print_deck(deck: Deck):
        deck.print_card()

    def print_deck_of_player(self):
        if not self.mode_split:
            self.human.print_deck_of_player("human:    ")
        else:
            self.human.print_split_deck("human:    ")
        self.croupier.print_deck_of_player("croupier: ")

    def first_hand(self):
        self.croupier.insert_cards(1)
        self.insurance()
        self.human.insert_cards(2)

        self.print_deck_of_player()

    def make_bet(self, value=50):
        self.human.update_debt_of_human(value)

    def get_standard_award(self, mode: str):
        self.human.add_award(self.DICTIONARY_AWARDS[mode] * self.human.get_value_of_bet())
        print(self.human.get_all_money())
        self.finish = True

    def next_game(self):
        choice = input("Do you want continue a game?\n0-yes\n1-no\nEnter your choice: ")
        while choice not in ["0", "1"]:
            input("Try again. ")
        if not choice == "1":
            del self.deck
            self.deck = Deck()
            self.initialization()
            self.human.default_parameters(self.deck)
            self.croupier.default_parameters(self.deck)
            if self.human.all_money <= 0:
                raise GaveOverHumanEmptyWallet("Game over, your wallet is empty!")
            self.start_play()
        else:
            exit()

    def start_play(self):
        menu_functions = {
            "1": self.hit,
            "2": self.stand,
            "3": self.double,
            "4": self.split,
            "5": self.blackjack,
            "6": self.insurance,
            "7": exit
        }
        bet = input(f"enter one of the following bet values\n50\n100\n500\n1000\n2002\nYour bet: ")
        while bet not in ["50", "100", "500", "1000", "2002"]:
            bet = input("Try again. ")
        while bet not in ["50", "100", "500", "1000", "2002"] or int(bet) > self.human.all_money :
            bet = input("Too much. You dont have enough money. Enter again: ")
        self.make_bet(self.VALUE_OF_BET[bet])
        self.first_hand()
        while (selection := input(self.MENU)) != "7":
            try:
                menu_functions[selection]()
                if self.finish:
                    self.finish = False
                    self.next_game()
            except KeyError:
                print("Invalid input selected. Try again")
            finally:
                if selection == "7":
                    exit()


if __name__ == "__main__":
    game = Game()
    game.initialization()
    game.start_play()

# do zrobienia:
"""
dymaniczne manu, zmienia sie w zaleznosci od kart split itd  dopiero w tkinter
testy

"""
