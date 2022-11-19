from card import Card, InvalidValue, InvalidColor
import pytest


def test_creation():
    card = Card("hearts", "Ace")
    print(card.value)  # python -m pytest -vvv -s card_test.py
    assert card.color == "\u2661"
    assert card.value == "Ace"


# def test_creation_wrong_value():
#     with pytest.raises(IndexError) as message:
#         card = Card("hearts", "A")
#         assert message == "Invalid card value"

# def test_creation_wrong_color():
#     with pytest.raises(KeyError) as message:
#         card = Card("xxx", "Ace")
#         assert message == "Invalid card value"

def test_creation_wrong_value():
    with pytest.raises(InvalidValue) as message:
        card = Card("hearts", "A")
        assert message == "Invalid card value"


def test_creation_wrong_color():
    with pytest.raises(InvalidColor) as message:
        card = Card("xxx", "Ace")
        assert message == "Invalid card value"


def test_card_represenatation():
    card = Card('hearts', 'Ace')
    assert repr(card) == 'Ace -> \u2661'
