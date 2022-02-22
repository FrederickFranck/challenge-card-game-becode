from utils.game import Board
from utils.player import Player

player_names = ["Andre", "Barry", "Carla", "Frederick"]
players = []
print("WOW")
def main():
    """Creates a board with all the players in <player_names>
    and starts the game
    """
    for name in player_names:
        players.append(Player(name))
    board = Board(players)
    board.start_game()


if __name__ == "__main__":
    main()
