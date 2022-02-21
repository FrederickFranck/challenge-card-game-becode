from typing import List
from card import Card
from random import randint
from random import shuffle


class Player:
    """Represents a Player

    Attributes:
        cards: a List of cards in the player's hand
        turn_count: an Integer representing the number of turns the player took
        number_of_cards: an Integer representing the amount of cards in a player's hand
        history: a List of Cards that contains all cards previously played by the player
    """

    def __init__(self, name: str, cards: List[Card]) -> None:
        """Inits a Player with a list of cards, the amount of cards in hand
        a turn_count on 0 and an empty history"""
        self.cards: List[Card] = cards
        self.turn_count: int = 0
        self.number_of_cards: int = len(cards)
        self.history: List[Card] = []
        self.name = name

    def play(self) -> Card:
        """Randomly pick a card for the player to play
        and returns that card"""
        if self.cards:
            random_card_index = randint(0, self.number_of_cards)
            card = self.cards.pop(random_card_index)
            self.turn_count += 1
            self.number_of_cards -= 1
            self.history.append(card)
            print(
                f"{self.name} {self.turn_count} played: {card.getValue()} {card.getIcon()}"
            )
            return card
        else:
            return None

    def deal(self, card: Card) -> None:
        """Deals a new card to the players hand"""
        self.cards.append(card)
        self.number_of_cards += 1


class Deck:
    """Class that represents an entire 52 card deck"""

    def __init__(self) -> None:
        """Inits Deck class with no cards"""
        self.cards: List[Card] = []

    def fill_deck(self) -> None:
        """Fills deck with 52 cards (13 values of 4 icons)"""
        _icons = ["♥", "♦", "♣", "♠"]
        _values = ["A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K"]
        for icon in _icons:
            for value in _values:
                self.cards.append(Card(icon, value))

    def shuffle(self) -> None:
        """Shuffles the list of cards"""
        shuffle(self.cards)

    def draw(self) -> Card:
        """Removes one card from the list and returns it"""
        return self.cards.pop()

    def distribute(self, players: List[Player]) -> None:
        """Given a list of players divides card evenly"""
        while not self.cards:
            for player in players:
                if not self.cards:
                    player.deal(self.draw())
