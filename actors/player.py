import itertools
import numbers
import string

from .participant import Participant


class Player(Participant):
    player_id = itertools.count(1)

    def __init__(self, name, init_bank=0):
        if not isinstance(name, str):
            raise TypeError(f'Player name must be a string. You tried: {name}')
        if not name or not all(letter in string.ascii_letters + ' ' for letter in name):
            raise ValueError(f'Player name must be only letters. You tried: {name}')
        self.name = name

        if not isinstance(init_bank, numbers.Real):
            raise TypeError(f'Initial bank must be a real number. You tried: {init_bank}')
        if not init_bank >= 0:
            raise ValueError(f'Initial bank must be positive. You tried: {init_bank}')
        self.bank = init_bank
        self._id = next(type(self).player_id)
        super().__init__()

    def __repr__(self):
        return f'Player(name={self.name}, bank={self.bank})'

    def bet(self, amount):
        self.bank -= amount
        return self.bank

    def collect(self, amount):
        self.bank += amount
        return self.bank
