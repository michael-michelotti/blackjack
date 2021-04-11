import itertools

from actors.player import Player
from actors.participant import Participant


def test_inheritance(player):
    assert isinstance(player, Participant)


def test_initialization(test_name):
    my_player = Player(test_name)
    assert isinstance(my_player, Player)


def test_name_property(player, test_name):
    assert player.name == test_name


def test_player_id():
    Player.player_id = itertools.count(1)
    player_one = Player('Kushol')
    player_two = Player('Kejin')

    assert player_one.id == 1
    assert player_two.id == 2


def test_default_init_bank_property(player):
    assert player.bank == 0


def test_init_bank_property(test_name):
    my_player = Player(test_name, init_bank=5000)
    assert my_player.bank == 5000
