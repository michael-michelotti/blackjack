from actors import Player, Dealer
from cards import Card, Deck, Hand, Table


main_deck = Deck()

dealer = Dealer(main_deck)

player_one = Player(main_deck, 'Michael')
player_two = Player(main_deck, 'Kushol')

dealer.add_player(player_one)
dealer.add_player(player_two)

dealer.deal_round(initial_hand=True)

print(player_one.hand.value)

print('Hello')
