from .participant import Participant


class Dealer(Participant):
    def __init__(self, deck):
        self.deck = deck
        super().__init__()

    def __repr__(self):
        return f'Dealer(deck={self.deck})'

    def deal_cards(self, num_cards, player):
        deck_stop_index = num_cards - 1
        player.hand.receive_cards(self.deck[:deck_stop_index])
        del self.deck[:deck_stop_index]

    def receive_discard(self, cards):
        self.deck.discard_pile.extend(cards)
