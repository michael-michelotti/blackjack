import pytest

from cards.card import Card
from cards.hand import Hand


def test_instantiation(card_one, card_two):
    my_hand = Hand(card_one, card_two)
    assert isinstance(my_hand, Hand)
    assert all(isinstance(card, Card) for card in my_hand.cards)


@pytest.mark.parametrize(
    ('inv_card_one', 'inv_card_two'),
    [
        (Card('J', 'S'), ('A', 'D')),
        (['7', 'H'], Card('8', 'C'))
    ])
def test_invalid_instantiation(inv_card_one, inv_card_two):
    with pytest.raises(TypeError):
        Hand(inv_card_one, inv_card_two)


def test_value_property(hand, card_one, card_two):
    """Test a "regular" hand"""
    assert hand.value == card_one.value + card_two.value


def test_value_over_21_with_ace(card_one, card_two):
    """Test hand with an ace and value over 21"""
    over_21_hand = Hand(Card('A', 'D'), Card('J', 'S'), Card('3', 'C'))
    assert over_21_hand.value == 14


def test_render(hand):
    assert isinstance(hand.render(), str)


def test_subscripting(hand, card_one, card_two):
    assert hand[0] is card_one
    assert hand[1] is card_two


def test_length(hand):
    assert len(hand) == 2


def test_receive_cards(hand, card_one_clone):
    assert len(hand) == 2
    hand.receive_cards(card_one_clone)
    assert len(hand) == 3
    assert hand[-1] is card_one_clone
