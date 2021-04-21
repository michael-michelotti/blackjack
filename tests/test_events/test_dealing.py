import pytest

from events.dealing import handle_initial_deal


def test_dealer_cards(table):
    test_dealer = table.dealer
    assert len(test_dealer.hand) == 0
    handle_initial_deal(table)
    assert len(test_dealer.hand) == 2


def test_player_cards(table):
    test_player = table.players[0]
    assert len(test_player.hand) == 0
    handle_initial_deal(table)
    assert len(test_player.hand) == 2


def test_card_render(table, capfd):
    handle_initial_deal(table)
    out, err = capfd.readouterr()
    assert out == "Dealer's Cards:\n"
