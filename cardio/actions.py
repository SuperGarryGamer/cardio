import Deck, Card, random

ranks: list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "Jack", "Queen", "King", "Ace"]
suits: list = ["Spades", "Clubs", "Hearts", "Diamonds"]

def generateDeck() -> Deck:
    cards = [Card(rank, suit) for rank in ranks for suit in suits]
    return Deck()

def shuffle(deck: Deck) -> Deck:
    return random.shuffle(Deck.cards)