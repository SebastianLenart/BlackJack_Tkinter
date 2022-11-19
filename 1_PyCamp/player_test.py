from player import Player
from card import Card


def test_calculate_player_points():
    # given
    card = Card("spades", 2)
    card2 = Card("hearts", 5)

    # when
    player = Player()
    player.take_card(card)
    player.take_card(card2)

    # then
    assert player.calculate_points() == 7


def test_calculate_player_points_two_aces():
    # given
    card = Card("spades", "Ace")
    card2 = Card("hearts", "Ace")

    # when
    player = Player()
    player.take_card(card)
    player.take_card(card2)

    # then
    assert player.calculate_points() == 21


def test_calculate_player_points_one_ace():
    # given
    card = Card("spades", "Ace")
    card2 = Card("hearts", 2)

    # when
    player = Player()
    player.take_card(card)
    player.take_card(card2)

    # then
    assert player.calculate_points() == 13


def test_calculate_player_points_three_aces():
    # given
    card = Card("spades", "Ace")
    card2 = Card("hearts", "Ace")
    card3 = Card("diamonds", "Ace")

    # when
    player = Player()
    player.take_card(card)
    player.take_card(card2)
    player.take_card(card3)

    # then
    assert player.calculate_points() == 3
