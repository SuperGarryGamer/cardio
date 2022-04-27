class Card():

    def getName(self):
        return f"{self.rank} of {self.suit}"

    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit