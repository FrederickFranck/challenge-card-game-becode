from typing import List
from player import Player
from player import Deck
from card import Card


class Board:
    """Class that represents the entire game state

    Attributes:
        players: a List of players
        turn_count: an Integer
        active_cards: a List of cards that contains the last card played by each player
        history_cards: a List of cards that contains all cards played excluding <active_cards>
    """

    def __init__(self, players: List[Player]) -> None:
        """Inits a Board class with a list of players , an empty history and a turn_count at 0"""
        self.players: List[Player] = players
        self.turn_count: int = 0
        self.active_cards: List[Card] = []
        self.history_cards: List[Card] = []
        self.deck: Deck = Deck()

    def start_game(self) -> None:
        """Starts the game
        Fills & Shuffles the Deck
        Distributes them evenly over the players
        Each player plays one card each turn until they have no cards left
        Prints the turn count , active cards & the number of played cards each turn
        """
        self.deck.fill_deck()
        self.deck.shuffle()
        self.deck.distribute(self.players)

        self.turn_count += 1
        for player in self.players:
            played_card = player.play()
            self.active_cards.append(played_card)

        print(
            f"Turn: {self.turn_count}, active cards : {self.active_cards} , history : {len(self.history_cards)}"
        )

        self.history_cards.append(self.active_cards)
        self.active_cards = []
