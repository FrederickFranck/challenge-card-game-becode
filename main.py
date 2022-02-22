from msilib.schema import Class
from utils.game import Board
from utils.player import Player

player_names = ["Andre", "Barry", "Carla", "Frederick"]
players = []


def main():
    for name in player_names:
        players.append(Player(name))
    board = Board(players)
    board.start_game()


if __name__ == "__main__":
    main()
