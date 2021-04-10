class Card:
    # Class attributes which define what ranks and suits are viable for a card
    ranks_to_values = {str(num): num for num in range(1, 11)}
    ranks_to_values.update({'J': 10, 'Q': 10, 'K': 10, 'A': 11})

    valid_ranks = [str(num) for num in range(2, 11)]
    valid_ranks.extend(['J', 'Q', 'K', 'A'])
    valid_suits = ['S', 'H', 'D', 'C']

    # Beginning of instance attributes
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self._value = None

    def __repr__(self):
        return f'({self._rank} of {self._suit})'

    def __eq__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return (self._rank, self._suit) == (other._rank, other._suit)

    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, value):
        if not isinstance(value, str):
            raise TypeError(f'Rank must be a string.')
        if value not in type(self).valid_ranks:
            raise ValueError(f'Invalid rank: {value}. Rank must be in: {", ".join(type(self).valid_ranks)}')
        self._rank = value

    @property
    def suit(self):
        return self._suit

    @suit.setter
    def suit(self, value):
        if not isinstance(value, str):
            raise TypeError(f'Suit must be a string.')
        if value not in type(self).valid_suits:
            raise ValueError(f'Invalid suit: {value}.Suit must be in: {", ".join(type(self).valid_suits)}')
        self._suit = value

    @property
    def value(self):
        if self._value is None:
            return type(self).ranks_to_values[self.rank]
        else:
            return self._value

    def render(self):
        return f"""
_________
| {self.rank}    {self.rank} |
|        |
|   {self.suit}    |
|        |
| {self.rank}    {self.rank} |
_________
"""


def render_card_back():
    return """_________
|$  $  $|
|       |
|   $   |
|       |
|$  $  $|
---------"""
