from .participant import Participant


class Dealer(Participant):
    def __init__(self, deck):
        self.players = []
        super().__init__(deck)

    def __repr(self):
        return f'Dealer(deck={self.deck}, num_players={len(self.players)})'

    def add_player(self, player):
        self.players.append(player)

    def deal_round(self, *, initial_hand=False):
        for player in self.players:
            player.hand.cards.append(self.deck.deal(2 if initial_hand else 1))

    def deal_cards(self, num_cards, player):
        player.hand.cards.append(self.deck.deal(num_cards))
