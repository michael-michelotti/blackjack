import pytest

from cards.card import Card


@pytest.mark.parametrize(
    ('rank', 'suit'),
    (
        ('A', 'D'),
        ('Q', 'S'),
        ('2', 'H')
    ))
def test_card_init(ranks_to_values, rank, suit):
    my_card = Card(rank, suit)
    assert my_card.rank == rank
    assert my_card.suit == suit
    assert my_card.value == ranks_to_values[my_card.rank]


@pytest.mark.parametrize(
    ('rank', 'suit'),
    (
        ('Invalid', 'D'),
        ('D', 'Q'),
        ('7', 'Invalid')
    ))
def test_card_init_value_errors(rank, suit):
    with pytest.raises(ValueError):
        Card(rank, suit)


@pytest.mark.parametrize(
    ('rank', 'suit'),
    (
        (7, 'D'),
        ('A', 10),
        ('7', ['D', 'H'])
    ))
def test_card_init_type_errors(rank, suit):
    with pytest.raises(TypeError):
        Card(rank, suit)


def test_card_equality(card_one, card_one_clone, card_two):
    assert card_one == card_one_clone
    assert card_one != card_two


def test_card_render(card_one):
    assert isinstance(card_one.render(), str)


def test_card_suit(card_one, test_suit):
    assert card_one.suit == test_suit


def test_card_rank(card_one, test_rank):
    assert card_one.rank == test_rank


def test_card_value(card_one, ranks_to_values, test_rank):
    assert card_one.value == ranks_to_values[test_rank]
