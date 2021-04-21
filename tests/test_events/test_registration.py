import events
from events.registration import handle_player_registration, single_player_registration


def test_handle_player_registration(table):
    events.input = lambda: 'Michael M'
