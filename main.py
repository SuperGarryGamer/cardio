from cardio import *

def main(stdscr):
    print("GO FISH - based on cardio")
    playerName = input("Enter your name: ")

    players = [Player("Robot", False), Player(playerName)]
    robot = players[0]
    human = players[1]
    dk = shuffle(Deck())

    move_card(dk, human, 7)
    move_card(dk, robot, 7)

    while len(robot.cards) > 0 and len(human.cards) > 0:
        for player in players:
            print(f"{player.get_name()}'s turn")
            if player.isHuman:
                print("Your cards:")
                for card in player.cards:
                    print(f"{player.cards.index(card)}: {get_card_name(card, True)}")
                possible_ranks = list(dict.fromkeys([card.rank for card in player.cards]))
                print(f"Request a rank {possible_ranks}: ")
