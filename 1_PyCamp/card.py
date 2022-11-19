"""BlackJack ASCII Python game"""
class InvalidColor(Exception):
    """Exception when color is invalid"""

class InvalidValue(Exception):
    """Exception when value is invalid"""


class Card:
    """Card Abstraction"""
    possible_colors = {
        "spades": "\u2664",
        "diamonds": "\u2662",
        "hearts": "\u2661",
        "clubs": "\u2667"
    }
    possible_value = list(range(2, 11)) + [
        "Ace",
        "Jack",
        "Queen",
        "King"
    ]

    def __init__(self, color, value):
        if color not in self.possible_colors:
            raise InvalidColor("Invalid color")
        self.color = self.possible_colors[color]
        if value not in self.possible_value:
            raise InvalidValue("Invalid card value")
        self.value = value

    def __repr__(self):
        return f'{self.value} -> {self.color}'

#  pylint card.py
#  pylint card_test.py
