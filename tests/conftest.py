import pytest

from actors.dealer import Dealer
from actors.player import Player
from actors.participant import Participant
from cards.card import Card
from cards.deck import Deck
from cards.hand import Hand
from cards.table import Table


@pytest.fixture
def custom_ranks():
    return ['20', '30', '40']


@pytest.fixture
def custom_suits():
    return ['Apples', 'Oranges']


@pytest.fixture(params=['2', 'A', 'J'])
def test_rank(request):
    return request.param


@pytest.fixture(params=['D', 'H'])
def test_suit(request):
    return request.param


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


@pytest.fixture
def deck():
    return Deck()


@pytest.fixture
def hand(card_one, card_two):
    return Hand(card_one, card_two)


@pytest.fixture
def participant():
    return Participant()


@pytest.fixture
def dealer(deck):
    return Dealer(deck)


@pytest.fixture(params=['Michael M'])
def test_name(request):
    return request.param


@pytest.fixture
def player(test_name):
    return Player(test_name)


@pytest.fixture
def deck_with_discard(deck):
    deck.discard_pile.extend(deck[:3])
    del deck[:3]
    return deck


@pytest.fixture
def table(dealer, player):
    return Table(dealer, [player])
