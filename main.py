from operator import le
from typing import List
from utils.game import Board
from utils.player import Player
from toml import load



#Reads all the info from the config.tmol file
parsed_toml = load("config.toml")
player_names: List[str] = parsed_toml["Config"]["players"]
human_players = parsed_toml["Config"]["humans"]

if(human_players >= len(player_names)):
    print("More human players requested then avaible players\nStarting with all human players instead")
    human_players = (len(player_names) - 1)

max_points = parsed_toml["Config"]["max_points"]
players: List[Player] = []

def main():
    """Creates a board with all the players in <player_names>
    and starts the game
    """
    for name in player_names:
        players.append(Player(name))
    for i in range(human_players):
        players[i].make_human()
    board = Board(players,max_points)
    board.start_game()


if __name__ == "__main__":
    main()
    
