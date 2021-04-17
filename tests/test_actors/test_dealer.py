from actors.dealer import Dealer


def test_dealer_initialization(deck):
    assert isinstance(Dealer(deck), Dealer)


def test_deal_cards_to_player(dealer, player):
    init_deck_len = len(dealer._deck)
    dealer.deal_cards(2, player)

    assert len(dealer._deck) == init_deck_len - 2
    assert len(player.hand) == 2


def test_deal_cards_to_self(dealer):
    init_deck_len = len(dealer._deck)
    dealer.deal_cards(2, to_self=True)

    assert len(dealer._deck) == init_deck_len - 2


def test_receive_discard(dealer, player):
    dealer.deal_cards(2, player)
    dealer.receive_discard(player.hand)

    assert len(dealer._deck.discard_pile) == 2

