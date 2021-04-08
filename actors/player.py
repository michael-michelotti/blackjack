from .participant import Participant


class Player(Participant):
    def __init__(self, deck, name, init_bank=0):
        self.name = name
        self.bank = init_bank
        super().__init__(deck)

    def __repr__(self):
        return f'Player(name={self.name}, bank={self.bank})'

    def bet(self, amount):
        self.bank -= amount
        return self.bank

    def collect(self, amount):
        self.bank += amount
        return self.bank
