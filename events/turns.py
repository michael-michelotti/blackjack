from cards.card import render_card_back


def handle_player_turns(table):
    dealer = table.dealer

    dealer_card = dealer.hand[0]
    print(f'Dealer\'s hand:')
    print(dealer_card.render())
    print(render_card_back())

    for player in table.players:
        print(f'{player.name}\'s turn:')
        print(f'{player.name}\'s hand:')
        print(player.hand.render())

        hit_or_stand = player_hit_or_stand()
        if hit_or_stand == 'stand':
            continue
        else:
            handle_hit(dealer, player)

    handle_hit(dealer, dealer_hit=True)
    print(f'Dealer\'s final hand:')
    print(dealer.hand.render())


def handle_hit(dealer, player=None, *, dealer_hit=False):
    # Handle player hit
    if dealer_hit:
        # Handle dealer hit
        less_than_17 = False if dealer.hand.value < 17 else True
        while not less_than_17:
            dealer.deal_self_cards(1)
            less_than_17 = False if dealer.hand.value < 17 else True
    else:
        bust = False
        while not bust:
            dealer.deal_cards(1, player)
            new_card = player.hand[-1]
            print(f'Dealer delt {new_card.rank} of {new_card.suit}')
            print(f'{player.name}\'s new hand:')
            print(player.hand.render())
            if player.hand.value > 21:
                print(f'{player.name} busted!')
                bust = True
                continue
            hit_again = player_hit_or_stand()
            if hit_again == 'stand':
                break


def handle_stand():
    pass


def player_hit_or_stand():
    hit_or_stand = input('Would you like to hit or stand (enter "hit" or "stand" with no quotes)?')
    if hit_or_stand not in ('hit', 'stand'):
        raise ValueError('You can only enter "hit" or "stand" (with no quotes)')
    return hit_or_stand


def handle_determine_winner(table):
    dealer = table.dealer
    dealer_score = dealer.hand.value

    # Loop over every participant on the table, compare their score to the dealer
    for player in table.players:
        player_score = player.hand.value

        # Handle player win
        if dealer_score < player_score <= 21:
            print(f'{player.name} won this hand!')
        # Handle player loss (dealer outscores player or dealer and player bust)
        elif player_score < dealer_score <= 21 or player_score > 21 and dealer_score > 21:
            print(f'{player.name} lost this hand!')
        # Handle tie
        elif player_score == dealer_score and player_score < 21:
            print(f'{player.name} tied with the dealer this hand.')
