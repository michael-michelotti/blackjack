import pytest

from cards.deck import Deck
from cards.card import Card


def test_deck_instantiation():
    my_deck = Deck()
    assert isinstance(my_deck, Deck)
    assert all(isinstance(card, Card) for card in my_deck)


@pytest.mark.parametrize(
    ('ranks', 'suits'),
    [
        ([1, 2], ['H', 'D']),
        (['5', '10'], [4, 7]),
        (2, ['H', 'D'])
    ]
)
def test_invalid_deck_instantiation(ranks, suits):
    with pytest.raises(TypeError):
        Deck(valid_ranks=ranks, valid_suits=suits)


def test_deck_deck_attribute(deck):
    assert isinstance(deck.deck, list)


def test_deck_discard_attribute(deck):
    assert deck.discard_pile == []


def test_deck_deal_method(deck):
    init_len = len(deck)
    hand = deck.deal(2)
    assert len(deck) == init_len - 2
    assert len(hand) == 2
    assert all(isinstance(card, Card) for card in hand)


@pytest.mark.parametrize(
    ('num', 'error'),
    (
        [-4, ValueError],
        [500, IndexError],
        ['4', TypeError]
    )
)
def test_deal_invalid_input_type(deck, num, error):
    with pytest.raises(error):
        deck.deal(num)


def test_deck_discard_method(deck):
    hand = deck.deal(2)
    deck.discard(hand)
    assert len(deck.discard_pile) == 2
    assert all(isinstance(card, Card) for card in deck.discard_pile)


@pytest.mark.parametrize(
    'cards',
    [
        [('J', 'C'), Card('10', 'S')],
        Card('J', 'S'),
        (Card('A', 'D'), Card('4', 'H'))
    ]
)
def test_deck_invalid_discards(deck, cards):
    with pytest.raises(TypeError):
        deck.discard(cards)


def test_deck_shuffle_method(deck):
    assert deck.shuffle() is None


def test_deck_reshuffle_method(deck):
    init_len = len(deck)
    hand = deck.deal(2)
    deck.discard(hand)
    deck.reshuffle()
    assert len(deck) == init_len


def test_deck_burn_method(deck):
    init_len = len(deck)
    deck.burn(5)
    assert len(deck.discard_pile) == 5
    assert len(deck) == init_len - 5

