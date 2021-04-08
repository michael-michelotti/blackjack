from cards.hand import Hand


class Participant:
    def __init__(self, deck):
        self.deck = deck
        self.hand = Hand()

    def hit(self):
        self.hand.cards.append(self.deck.deal(1))

    @staticmethod
    def stay():
        return None
