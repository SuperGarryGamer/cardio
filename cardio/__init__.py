import random

class Card():

    def about(self) -> tuple:
        return (self.rank, self.suit)

    def __init__(self, rank: int, suit: int):
        self.rank = rank
        self.suit = suit

class Deck():

    def get_name(self):
        return "Deck"

    def print_cards(self):
        print([getName(card) for card in self.cards])

    def __init__(self, cards: list=[]):
        self.cards = cards

class Player(Deck):
    
    def get_name(self):
        return self.name

    def print_cards(self, short: bool=False):
        print([get_card_name(card, True) if short else get_card_name(card) for card in self.cards])
        
    def __init__(self, name: str, is_human: True):
        self.name = name
        self.cards = []
        self.is_human = is_human

ranks: list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "Jack", "Queen", "King", "Ace"]
suits: list = ["Spades", "Clubs", "Hearts", "Diamonds"]
short_ranks: list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K", "A"]
short_suits: list = ["♤", "♧", "♥", "♦"]

def generate_deck() -> Deck:
    cards = [Card(rank, suit) for rank in range(len(ranks)) for suit in range(len(suits))]
    return Deck(cards)

def shuffle(deck: Deck) -> Deck:
    new_cards = list(deck.cards)
    random.shuffle(new_cards)
    return Deck(new_cards)

def get_card_name(card: Card, short: bool=False) -> str:
    abt = card.about()
    if short:
        return f"{short_ranks[abt[0]]}{short_suits[abt[1]]}"
    else:
        return f"{ranks[abt[0]]} of {suits[abt[1]]}"

def move_card(giver, taker, count: int=1):
    print(f"{taker.get_name()} takes {count} card{'s' if count != 1 else ''} from {giver.get_name()}")

    for i in range(count):
        taken = giver.cards.pop()
        taker.cards.append(taken)