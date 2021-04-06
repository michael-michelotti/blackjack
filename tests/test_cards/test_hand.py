import pytest

from cards.card import Card
from cards.hand import Hand


@pytest.fixture
def test_card_one():
    return Card('J', 'S')


@pytest.fixture
def test_card_two():
    return Card('2', 'C')


@pytest.fixture
def hand(test_card_one, test_card_two):
    return Hand(test_card_one, test_card_two)


def test_hand_instantiation(test_card_one, test_card_two):
    my_hand = Hand(test_card_one, test_card_two)
    assert isinstance(my_hand, Hand)
    assert all(isinstance(card, Card) for card in my_hand.cards)


@pytest.mark.parametrize(
    ('card_one', 'card_two'),
    [
        (Card('J', 'S'), ('A', 'D')),
        (['7', 'H'], Card('8', 'C'))
    ]
)
def test_invalid_hand_instantiation(card_one, card_two):
    with pytest.raises(TypeError):
        Hand(card_one, card_two)


def test_hand_value_property(hand, test_card_one, test_card_two):
    assert hand.value == test_card_one.value + test_card_two.value


def test_hand_render(hand):
    assert isinstance(hand.render(), str)
