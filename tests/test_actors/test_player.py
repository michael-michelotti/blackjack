import itertools

import pytest

from actors.player import Player
from actors.participant import Participant
from cards.hand import Hand


def test_inheritance(player):
    assert isinstance(player, Participant)


def test_initialization(test_name):
    my_player = Player(test_name)
    assert isinstance(my_player, Player)
    assert my_player.bank == 0
    assert isinstance(my_player.hand, Hand)


@pytest.mark.parametrize('name', [['Michael'], 0])
def test_initialization_invalid_name_type(name):
    with pytest.raises(TypeError):
        Player(name)


@pytest.mark.parametrize('name', ['', 'Mi_chael', 'Ke7in'])
def test_initialization_invalid_name_value(name):
    with pytest.raises(ValueError):
        Player(name)


def test_name_property(player, test_name):
    assert player.name == test_name


def test_player_id():
    Player.player_id = itertools.count(1)
    player_one = Player('Kushol')
    player_two = Player('Kejin')

    assert player_one._id == 1
    assert player_two._id == 2


def test_init_bank_property(test_name):
    my_player = Player(test_name, init_bank=5000)
    assert my_player.bank == 5000


@pytest.mark.parametrize('bank_val', ['500', [200], 2+1j])
def test_init_bank_property_invalid_type(test_name, bank_val):
    with pytest.raises(TypeError):
        Player(test_name, init_bank=bank_val)


@pytest.mark.parametrize('bank_val', [-1])
def test_init_bank_property_invalid_value(test_name, bank_val):
    with pytest.raises(ValueError):
        Player(test_name, init_bank=bank_val)
