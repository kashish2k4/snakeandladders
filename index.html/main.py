from board import snakes, ladders
from player import Player
from utils import roll_dice

def play_game(players):
    while True:
        for player in players:
            input(f"\n{player.name}'s turn. Press Enter to roll the dice...")
            roll = roll_dice()
            print(f"{player.name} rolled a {roll}")
            player.move(roll)

            if player.position in snakes:
                print(f"Oops! {player.name} got bitten by a snake at {player.position}")
                player.set_position(snakes[player.position])

            elif player.position in ladders:
                print(f"Yay! {player.name} climbed a ladder at {player.position}")
                player.set_position(ladders[player.position])

            print(f"{player.name} is now at position {player.position}")

            if player.has_won():
                print(f"\n🎉🎉 {player.name} wins the game! 🎉🎉")
                return

if __name__ == "__main__":
    print("Welcome to Snake and Ladders Game")
    num_players = int(input("Enter number of players: "))
    players = [Player(input(f"Enter name for Player {i+1}: ")) for i in range(num_players)]
    play_game(players)