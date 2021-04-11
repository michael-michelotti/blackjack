from cards.hand import Hand
from actors.participant import Participant

# Added a comment


def test_initialization():
    assert isinstance(Participant(), Participant)


def test_participant_hand_property(participant):
    assert isinstance(participant.hand, Hand)
    assert len(participant.hand) == 0
