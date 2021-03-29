import pytest

from cards import Card


@pytest.fixture
def card():
    return Card('A', 'D')


@pytest.fixture
def ranks_to_values():
    non_face_cards = {str(num): num for num in range(1, 11)}
    return non_face_cards.update(
        {
            'J': 10,
            'Q': 10,
            'K': 10,
            'A': 11
        }
    )


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
