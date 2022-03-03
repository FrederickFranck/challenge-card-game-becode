from typing import List
from .player import Player
from .player import Deck
from .card import Card


class Board:
    """Class that represents the entire game state

    Attributes:
        players: a List of players
        turn_count: an Integer which counts how many turns have passed
        active_cards: a List of cards that contains the last card played by each player
        history_cards: a List of cards that contains all cards played excluding <active_cards>
    """

    def __init__(self, players: List[Player]) -> None:
        """Creates a Board class with a list of players , an empty history and a turn_count at 0"""
        self.players: List[Player] = players
        self.turn_count: int = 0
        self.active_cards: List[Card] = []
        self.history_cards: List[Card] = []
        self.deck: Deck = Deck()

    def can_play(self) -> bool:
        """Checks if there is any player who can still play cards"""
        for player in self.players:
            if player.cards:
                return True

    def start_game(self) -> None:
        """Starts the game
        Fills & Shuffles the Deck
        Distributes them evenly over the players
        Each player plays one card each turn until they have no cards left
        Updates the active_cards & the history
        Prints the turn count , active cards & the number of played cards each turn
        """
        self.deck.fill_deck()
        self.deck.shuffle()
        self.deck.distribute(self.players)

        while self.can_play():
            for card in self.active_cards:
                self.history_cards.append(card)
            self.active_cards = []
            self.play_turn()

        print(f"The Game ended, Everyone is out of cards")

    def play_turn(self) -> None:
        """Plays 1 turn
        Makes every player (who still has cards) play 1 card
        Also advances the turn counter
        Prints the turn count , active cards & the number of played cards
        """
        self.turn_count += 1
        for player in self.players:
            played_card = player.play()
            self.active_cards.append(played_card)

        print(
            f"Turn: {self.turn_count}, active cards : {self.active_cards} , history : {len(self.history_cards)}\n"
        )

    def __str__(self) -> str:
        """Returns a string representation of the class"""
        ret = ""
        ret += f"Turn: {self.turn_count}, Active_Cards: {self.active_cards}, History: {len(self.history_cards)}\n"
        for player in self.players:
            ret += str(player)
            ret += "\n"
        return ret