from .card import Card


class Hand:
    def __init__(self, *cards):
        self.cards = list(cards)
        self._value = None

    def __len__(self):
        return len(self._cards)

    def __repr__(self):
        return f'Hand({", ".join(repr(card) for card in self._cards)})'

    @property
    def cards(self):
        return self._cards

    @cards.setter
    def cards(self, new_cards):
        if not all(isinstance(card, Card) for card in new_cards):
            raise TypeError('Every member of a Hand must be a Card.')
        self._cards = new_cards

    @property
    def value(self):
        if self._value is None:
            self._value = sum(card.value for card in self._cards)
        return self._value

    def render(self):
        return f'{"".join(card.render() for card in self._cards)}'

    def receive_cards(self, cards):
        self._cards.extend(cards)
