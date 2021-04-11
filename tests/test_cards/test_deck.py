import pytest

from cards.deck import Deck
from cards.card import Card


def test_instantiation():
    my_deck = Deck()
    assert isinstance(my_deck, Deck)
    assert all(isinstance(card, Card) for card in my_deck)


@pytest.mark.skip
def test_instantiation_custom_ranks_and_suits(custom_ranks, custom_suits):
    """Test ability to supply deck with custom ranks and suits - not currently implemented"""
    my_deck = Deck(valid_ranks=custom_ranks, valid_suits=custom_suits)
    assert len(my_deck) == len(custom_ranks) * len(custom_suits)
    assert all(isinstance(card, Card) for card in my_deck)


@pytest.mark.skip
@pytest.mark.parametrize(
    ('ranks', 'suits'),
    [
        ([1, 2], ['H', 'D']),
        (['5', '10'], [4, 7]),
        (2, ['H', 'D'])
    ]
)
def test_invalid_instantiation(ranks, suits):
    with pytest.raises(TypeError):
        Deck(valid_ranks=ranks, valid_suits=suits)


def test_length(deck):
    assert len(deck) == len(Card.valid_suits) * len(Card.valid_ranks)


def test_discard_pile_property(deck):
    assert deck.discard_pile == []


def test_iteration(deck):
    for card in deck:
        assert isinstance(card, Card)


def test_shuffle_method(deck):
    assert deck.shuffle() is None


def test_reshuffle_method(deck_with_discard):
    discard_len = len(deck_with_discard.discard_pile)
    init_len = len(deck_with_discard)
    deck_with_discard.reshuffle()
    assert len(deck_with_discard.discard_pile) == 0
    assert len(deck_with_discard) == init_len + discard_len


def test_burn_method(deck):
    init_len = len(deck)
    deck.burn(5)
    assert len(deck.discard_pile) == 5
    assert len(deck) == init_len - 5


@pytest.mark.parametrize('burn_num', ['5', [5], 'five'])
def test_burn_method_invalid_type(deck, burn_num):
    with pytest.raises(TypeError):
        deck.burn(burn_num)


def test_burn_method_out_of_bounds(deck):
    deck_len = len(deck)
    with pytest.raises(IndexError):
        deck.burn(deck_len + 1)


def test_burn_method_invalid_burn_number(deck):
    with pytest.raises(ValueError):
        deck.burn(-1)
