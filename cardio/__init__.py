from typing import Union
import random

class Card():

    def about(self) -> tuple:
        return (self.rank, self.suit)

    def __init__(self, rank: int, suit: int):
        self.rank = rank
        self.suit = suit

class Deck():

    def print_cards(self):
        print([getName(card) for card in self.cards])

    def __init__(self, cards: list=[]):
        self.cards = cards

class Player(Deck):

    def print_cards(self, short: bool=False):
        print([getName(card, True) if short else getName(card) for card in self.cards])
        
    def __init__(self, name: str):
        self.name = name
        self.cards = []

ranks: list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "Jack", "Queen", "King", "Ace"]
suits: list = ["Spades", "Clubs", "Hearts", "Diamonds"]
short_ranks: list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K", "A"]
short_suits: list = ["♤", "♧", "♥", "♦"]

def generateDeck() -> Deck:
    cards = [Card(rank, suit) for rank in range(len(ranks)) for suit in range(len(suits))]
    return Deck(cards)

def shuffle(deck: Deck) -> Deck:
    new_cards = list(deck.cards)
    random.shuffle(new_cards)
    return Deck(new_cards)

def getName(card: Card, short: bool=False) -> str:
    abt = card.about()
    if short:
        return f"{short_ranks[abt[0]]}{short_suits[abt[1]]}"
    else:
        return f"{ranks[abt[0]]} of {suits[abt[1]]}"

def move_card(giver, taker):
    taken = giver.cards.pop()
    taker.cards.append(taken)