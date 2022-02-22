import imp
from utils.game import Board
from utils.player import Player
from toml import load


parsed_toml = load("config.toml")

   
player_names = parsed_toml["Players"]["names"]
human_players = parsed_toml["Players"]["humans"]
players = []

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
    
