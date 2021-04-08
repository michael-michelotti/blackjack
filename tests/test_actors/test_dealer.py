from actors.dealer import Dealer


def test_dealer_initialization(deck):
    assert isinstance(Dealer, Dealer(deck))


def test_dealer_add_player(dealer, player):
    assert dealer.players == []
    dealer.add_player(player)
    assert len(dealer.players) == 1
    assert dealer.players[0] is player


def test_deal_round(dealer_with_player):
    player = dealer_with_player.players[0]
    init_deck_len = len(dealer_with_player.deck)
    init_player_hand = player.hand
    dealer_with_player.deal_deck()

    assert len(dealer_with_player.deck) == init_deck_len - 1
    assert len(init_player_hand) == player.hand - 1


def test_deal_round_initial_hand(dealer_with_player):
    player = dealer_with_player.players[0]
    init_deck_len = len(dealer_with_player.deck)
    init_player_hand = player.hand
    dealer_with_player.deal_deck(initial_hand=True)

    assert len(dealer_with_player.deck) == init_deck_len - 1
    assert len(init_player_hand) == player.hand - 1


def test_deal_cards(dealer_with_player):
    num_cards = 3
    player = dealer_with_player.players[0]
    init_deck_len = len(dealer_with_player.deck)
    assert player.hand == []
    dealer_with_player.deal_cards(num_cards)
    assert len(dealer_with_player.deck) == init_deck_len - num_cards
    assert len(player.hand) == num_cards
