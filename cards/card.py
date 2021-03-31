class Card:
    # Class attributes which define what ranks and suits are viable for a card
    ranks_to_values = {str(num): num for num in range(1, 11)}
    ranks_to_values.update(
        {
            'J': 10,
            'Q': 10,
            'K': 10,
            'A': 11
        }
    )

    valid_ranks = [str(num) for num in range(1, 11)]
    valid_ranks.extend(['J', 'Q', 'K', 'A'])
    valid_suits = ['H', 'D', 'C', 'S']

    # Beginning of instance attributes
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit
        self.value = type(self).ranks_to_values[rank]

    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, value):
        if not isinstance(value, str):
            raise TypeError(f'Rank must be a string in: {", ".join(type(self).valid_ranks)}')
        if value not in type(self).valid_ranks:
            raise ValueError(f'Invalid rank: {value}. Rank must be in: {", ".join(type(self).valid_ranks)}')
        self._rank = value

    @property
    def suit(self):
        return self._rank

    @suit.setter
    def suit(self, value):
        if not isinstance(value, str):
            raise TypeError(f'Suit must be a string in: {", ".join(type(self).valid_suits)}')
        if value not in type(self).valid_suits:
            raise ValueError(f'Invalid suit: {value}.Suit must be in: {", ".join(type(self).valid_suits)}')
        self._suit = value

    def render(self):
        return f"""
        ________________
        | {self.rank}    {self.rank}  |
        |                        |
        |                        |
        |                        |
        |        {self.suit}        |
        |                        |
        |                        |
        | {self.rank}    {self.rank}    |
        _________________
        """
