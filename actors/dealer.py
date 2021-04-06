from .participant import Participant


class Dealer(Participant):
    def __init__(self, deck):
        self.players = []
        super().__init__(deck)

    def add_player(self, player):
        self.players.append(player)

    def deal_deck(self, *, initial_hand=False):
        for player in self.players:
            player.hand.append(self.deck.deal(2 if initial_hand else 1))
