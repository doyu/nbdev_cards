# AUTOGENERATED! DO NOT EDIT! File to edit: ../00_deck.ipynb.

# %% auto 0
__all__ = ['Deck', 'draw_n']

# %% ../00_deck.ipynb 3
from .card import *
from fastcore.utils import *
import random

# %% ../00_deck.ipynb 5
class Deck:
    def __init__(self): self.cards = [Card(s, r) for s in range(len(suits)) for r in range(1, len(ranks))]
    def __len__(self): return len(self.cards)
    def __str__(self): return ';'.join(map(str,self.cards))
    def __contains__(self, card): return card in self.cards
    __repr__=__str__
    
    def shuffle(self):
        "Shuffles the cards in this deck"
        random.shuffle(self.cards)

# %% ../00_deck.ipynb 15
@patch
def pop(self:Deck,
       idx:int=-1): # The index of the card to remove, defaulting to the last one
    "Remove one card from the deck"
    return self.cards.pop(idx)

# %% ../00_deck.ipynb 19
@patch
def remove(self:Deck,
        card:Card): # Card to remove
    "Removes `card` from the deck or raises exception if it is not there"
    self.cards.remove(card)

# %% ../00_deck.ipynb 22
def draw_n(n:int, # number of cards to draw
          replace:bool=True): # whether or not draw with replacement
    "Draw `n` cards, with replacement iif `replace`"
    d = Deck()
    d.shuffle()
    if replace: return [d.cards[random.choice(range(len(d.cards)))] for _ in range(n)]
    else: return d.cards[:n]
