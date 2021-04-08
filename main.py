from actors import Player, Dealer
from cards import Card, Deck, Hand, Table
from events.registration import handle_player_registration


def main():
    # Initial table setup
    main_deck = Deck()
    dealer = Dealer(main_deck)
    main_table = Table(dealer, players=[])

    # Player registration
    handle_player_registration(main_table)

    # Initial hand dealing
    for player in main_table.players:
        dealer.shuffle_deck()
        dealer.deal_cards(2, player)
        print(f'{player.name}\'s hand:' + player.hand.render())


if __name__ == '__main__':
    # Main game loop
    main()
