import pytest

from cards.hand import Hand
from cards.card import Card
from cards.deck import Deck
from actors.participant import Participant


@pytest.fixture
def test_card_one():
    return Card('10', 'D')


@pytest.fixture
def test_card_two():
    return Card('6', 'S')


@pytest.fixture
def hand(test_card_one, test_card_two):
    return Hand(test_card_one, test_card_two)


@pytest.fixture
def deck():
    return Deck()


@pytest.fixture
def test_participant(deck):
    return Participant(deck)


def test_participant_initialization(deck):
    assert isinstance(Participant(deck), Participant)


@pytest.mark.parametrize(
    'invalid_deck',
    [
        (Card('J', 'S')),
        (('J', 'S'), Card('9', 'D'))
    ]
)
def test_participant_invalid_initialization(invalid_deck):
    with pytest.raises(TypeError):
        Participant(invalid_deck)


def test_participant_hit_method(test_participant):
    assert test_participant.hand == []
    test_participant.hit()
    assert len(test_participant.hand) == 1


def test_participant_stay_method(test_participant):
    assert test_participant.hand == []
    test_participant.stay()
    assert len(test_participant.hand) == 0

