class Table:
    def __init__(self, dealer, players):
        self.dealer = dealer
        self.players = players
        self.participants = players.append(dealer)

    def __repr__(self):
        return f'Table(dealer={self.dealer}, players={self.players})'

    def render(self):
        return f'{"".join(hand.render() for hand in self.participants)}'
