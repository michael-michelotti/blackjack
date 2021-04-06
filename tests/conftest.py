import pytest

from cards.card import Card
from cards.deck import Deck
from cards.hand import Hand


@pytest.fixture
def test_rank():
    return 'A'


@pytest.fixture
def test_suit():
    return 'D'


@pytest.fixture
def card_one(test_rank, test_suit):
    return Card(test_rank, test_suit)


@pytest.fixture
def card_one_clone(test_rank, test_suit):
    return Card(test_rank, test_suit)


@pytest.fixture
def card_two():
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


@pytest.fixture()
def deck():
    return Deck()


@pytest.fixture
def hand(test_card_one, test_card_two):
    return Hand(test_card_one, test_card_two)
