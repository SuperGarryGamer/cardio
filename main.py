from cardio import *

dk = shuffle(generateDeck())

alice = Player("Alice")
bob = Player("Bob")

move_card(dk, alice)
move_card(dk, bob)

print(f"Alice's card: {getName(alice.cards[0], True)}")
print(f"Bob's card: {getName(bob.cards[0], True)}")
