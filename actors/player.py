from .participant import Participant


class Player(Participant):
    def __init__(self, name, init_bank=0):
        self.name = name
        self.bank = init_bank
        super().__init__()

    def __repr__(self):
        return f'Player(name={self.name}, bank={self.bank})'

    def bet(self, amount):
        self.bank -= amount
        return self.bank

    def collect(self, amount):
        self.bank += amount
        return self.bank
