import pytest

from cards.card import Card
from cards.hand import Hand


def test_hand_instantiation(card_one, card_two):
    my_hand = Hand(card_one, card_two)
    assert isinstance(my_hand, Hand)
    assert all(isinstance(card, Card) for card in my_hand.cards)


@pytest.mark.parametrize(
    ('inv_card_one', 'inv_card_two'),
    [
        (Card('J', 'S'), ('A', 'D')),
        (['7', 'H'], Card('8', 'C'))
    ]
)
def test_invalid_hand_instantiation(inv_card_one, inv_card_two):
    with pytest.raises(TypeError):
        Hand(inv_card_one, inv_card_two)


def test_hand_value_property(hand, card_one, card_two):
    assert hand.value == card_one.value + card_two.value


def test_hand_render(hand):
    assert isinstance(hand.render(), str)
