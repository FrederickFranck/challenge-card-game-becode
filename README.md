# Challenge-card-game-becode [Nice to haves]
A Simple Card Game

The game will divide 52 cards (13 ranks of each suit) across all the players. Then all players will play a card and whoever plays the highest ranking card gets 1 point. The first player who gets to the maximum points wins the game.

If there are human players in the game, they will get asked each round which card they want to play.

### Installation
clone the repository to your machine
```bash
git clone -b nice-to-haves https://github.com/FrederickFranck/challenge-card-game-becode.git
```
Install the toml library
```bash
pip install toml
```

### Usage
run the main file to start the game
```bash
python main.py
```

#### Configuration
In the config.toml file there are a few settings you can change:

##### The players 
To change the amount of players just add or remove names to the list *player_names*. (You can also changer the playernames this way)
```toml
#config.toml
player_names = ["Andre", "Barry", "Carla", "Frederick"]
```

##### Human players
This will change the first *n* players in the list to the amount of humans 

```toml
#config.toml
humans = 1
```

##### Max Score
This will change how many points people need to get to win the game
```toml
#config.toml
max_points = 3
```


## Versions
There is also another version available with only the must have features see [here](https://github.com/FrederickFranck/challenge-card-game-becode/tree/must-haves#challenge-card-game-becode-must-haves).