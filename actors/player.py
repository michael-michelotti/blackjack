import itertools

from .participant import Participant


class Player(Participant):
    player_id = itertools.count(1)

    def __init__(self, name, init_bank=0):
        self.name = name
        self.bank = init_bank
        self.id = next(type(self).player_id)
        super().__init__()

    def __repr__(self):
        return f'Player(name={self.name}, bank={self.bank})'

    def bet(self, amount):
        self.bank -= amount
        return self.bank

    def collect(self, amount):
        self.bank += amount
        return self.bank
