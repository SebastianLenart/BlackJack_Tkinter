from card import Card
from player import Player
from deck import Deck
from exceptions import GameOverCroupierException, GameOverException, GameOverUserException


class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()

    @staticmethod
    def _print_menu():
        print("Co chcesz zrobic?")
        print("0 - dobieram karte")
        print("1 - pasuje")

    def _croupier_plays(self, user_points):
        croupier = Player()
        while croupier.calculate_points() < user_points:
            croupier.take_card(self.deck.hit())
            print("Krupier: ")
            print(croupier.cards)
            print(croupier.calculate_points())
        return croupier.calculate_points()

    def _user_plays(self):
        user = Player()
        for _ in range(2):
            card = self.deck.hit()
            user.take_card(card)
        while True:
            print(user.cards)
            print(user.calculate_points())
            self._print_menu()
            choice = input("Wybierz 0 lub 1: ")
            if choice == "0":
                user.take_card(self.deck.hit())
            if choice == "1":
                return user.calculate_points()
            else:
                print("Zly wybor")

    def play(self):
        try:
            user_points = self._user_plays()
        except GameOverException as error:
            raise GameOverUserException from error  # what is it ???
        try:
            croupier_points = self._croupier_plays(user_points)
        except GameOverException as error:
            raise GameOverCroupierException from error

        print("Koniec gry wygrana krupiera")
