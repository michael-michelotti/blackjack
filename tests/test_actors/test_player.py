from actors.player import Player
from actors.participant import Participant


def test_inheritance(player):
    assert isinstance(player, Participant)


def test_initialization(deck):
    my_player = Player(deck)
    assert isinstance(my_player, Player)