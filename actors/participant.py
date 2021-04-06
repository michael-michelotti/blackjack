class Participant:
    def __init__(self, deck):
        self.deck = deck
        self.hand = []

    def hit(self):
        self.hand.append(self.deck.deal(1))

    @staticmethod
    def stay():
        return None
