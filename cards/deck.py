import itertools
import random

from .card import Card


class Deck:
    def __init__(self, *, valid_ranks=Card.valid_ranks, valid_suits=Card.valid_suits):
        self.discard_pile = []
        self.deck = [Card(valid_ranks, valid_suits)
                     for valid_ranks, valid_suits
                     in itertools.product(valid_ranks, valid_suits)]
        self.participants = []

    def __repr__(self):
        return f'Deck(cards={len(self.deck)}, discard={len(self.discard_pile)})'

    def __len__(self):
        return len(self.deck)

    def __getitem__(self, idx):
        if isinstance(idx, int):
            if idx >= len(self.deck) or idx < -len(self.deck):
                return IndexError('The deck does not have that many cards!')

        return self.deck[idx]

    def __iter__(self):
        return self.DeckIterator(self)

    class DeckIterator:
        def __init__(self, deck_obj):
            self._deck_obj = deck_obj
            self._index = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self._index >= len(self._deck_obj):
                raise StopIteration
            next_val = self._deck_obj[self._index]
            self._index += 1
            return next_val

    def deal(self, num_cards):
        if not isinstance(num_cards, int):
            raise TypeError('You can only deal a number of cards')
        if num_cards > len(self.deck):
            raise IndexError('There are not that many cards left in the deck')
        if num_cards <= 0:
            raise ValueError('You can only deal a positive number of cards')
        dealt_cards = self.deck[:num_cards]
        del self.deck[:num_cards]
        return dealt_cards

    def discard(self, cards):
        if not all(isinstance(card, Card) for card in cards):
            raise TypeError('Can only discard a list of Cards')
        if not isinstance(cards, list):
            raise TypeError('You can only discard a list of Cards')
        self.discard_pile.extend(cards)

    def shuffle(self):
        random.shuffle(self.deck)

    def reshuffle(self):
        self.deck.extend(self.discard_pile)
        self.discard_pile = []
        random.shuffle(self.deck)

    def burn(self, num_cards):
        if not isinstance(num_cards, int):
            raise TypeError(f'You can only burn an integer number of cards. You tried: {type(num_cards)}')
        if num_cards > len(self.deck):
            raise IndexError('There are not that many cards left in the deck')
        if num_cards <= 0:
            raise ValueError('You can only burn a positive number of cards')

        self.discard_pile.extend(self.deck[:num_cards])
        del self.deck[:num_cards]

    def add_participant(self, participant):
        # if not isinstance(participant, Participant):
        #     raise TypeError('All members of the game must be a Participant object.')
        self.participants.append(participant)
