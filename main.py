import imp
from typing import List
from utils.game import Board
from utils.player import Player
from toml import load


parsed_toml = load("config.toml")

   
player_names: List[str] = parsed_toml["Config"]["players"]
human_players = parsed_toml["Config"]["humans"]
trump = parsed_toml["Config"]["trump"]
players: List[Player] = []

def main():
    """Creates a board with all the players in <player_names>
    and starts the game
    """
    for name in player_names:
        players.append(Player(name))
    for i in range(human_players):
        players[i].make_human()
    board = Board(players,trump)
    board.start_game()


if __name__ == "__main__":
    main()
    
