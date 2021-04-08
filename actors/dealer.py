from .participant import Participant


class Dealer(Participant):
    def __init__(self, deck):
        self._deck = deck
        super().__init__()

    def __repr__(self):
        return f'Dealer(deck={self._deck})'

    def deal_cards(self, num_cards, player):
        player.hand.receive_cards(self._deck[:num_cards])
        del self._deck[:num_cards]

    def receive_discard(self, cards):
        self._deck.discard_pile.extend(cards)

    def shuffle_deck(self):
        self._deck.shuffle()
