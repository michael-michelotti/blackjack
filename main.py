from actors import Dealer
from cards import Deck, Table
from events.registration import handle_player_registration
from events.dealing import handle_initial_deal
from events.turns import handle_player_turns, handle_determine_winner


def main():
    playing = True
    while playing:
        # Initial table setup
        main_deck = Deck()
        dealer = Dealer(main_deck)
        main_table = Table(dealer, players=[])

        # Player registration
        handle_player_registration(main_table)

        # Initial hand dealing
        dealer.shuffle_deck()
        handle_initial_deal(main_table)

        # Player turns
        handle_player_turns(main_table)

        # Calculate winner
        handle_determine_winner(main_table)

        continue_playing = input('Would you like to play another hand (Y/n)?')
        if continue_playing != 'Y':
            playing = False


if __name__ == '__main__':
    # Main game loop
    main()
