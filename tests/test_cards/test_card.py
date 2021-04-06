import pytest

from cards.card import Card


@pytest.fixture
def test_rank():
    return 'A'


@pytest.fixture
def test_suit():
    return 'D'


@pytest.fixture
def card(test_rank, test_suit):
    return Card(test_rank, test_suit)


@pytest.fixture
def same_card(test_rank, test_suit):
    return Card(test_rank, test_suit)


@pytest.fixture
def diff_card():
    return Card('10', 'S')


@pytest.fixture
def ranks_to_values():
    non_face_cards = {str(num): num for num in range(1, 11)}
    non_face_cards.update(
        {
            'J': 10,
            'Q': 10,
            'K': 10,
            'A': 11
        }
    )
    return non_face_cards


@pytest.mark.parametrize(
    ('rank', 'suit'),
    (
        ('A', 'D'),
        ('Q', 'S'),
        ('2', 'H')
    )
)
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
    )
)
def test_card_init_value_errors(rank, suit):
    with pytest.raises(ValueError):
        Card(rank, suit)


@pytest.mark.parametrize(
    ('rank', 'suit'),
    (
        (7, 'D'),
        ('A', 10),
        ('7', ['D', 'H'])
    )
)
def test_card_init_type_errors(rank, suit):
    with pytest.raises(TypeError):
        Card(rank, suit)


def test_card_equality(card, same_card, diff_card):
    assert card == same_card
    assert card != diff_card


def test_card_render(card):
    assert isinstance(card.render(), str)


def test_card_suit(card, test_suit):
    assert card.suit == test_suit


def test_card_rank(card, test_rank):
    assert card.rank == test_rank


def test_card_value(card, ranks_to_values, test_rank):
    assert card.value == ranks_to_values[test_rank]
