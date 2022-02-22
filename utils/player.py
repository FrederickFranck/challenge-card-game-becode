from tkinter import N
from tkinter.messagebox import NO
from typing import List
from .card import Card
from random import randint
from random import shuffle


class Player:
    """Represents a Player

    Attributes:
        cards: a List of cards in the player's hand
        turn_count: an Integer representing the number of turns the player took
        number_of_cards: an Integer representing the amount of cards in a player's hand
        history: a List of Cards that contains all cards previously played by the player
        is_human: a boolean which represents if the player is a human or robot
        points: and integer which represents the amount of points the player currently has
    """

    _icons = ["🤖","😀"]

    def __init__(self, name: str,is_human=False) -> None:
        """Creates a Player with an empty list of cards, the amount of cards in hand
        a turn_count on 0 and an empty history"""
        self.cards: List[Card] = []
        self.turn_count: int = 0
        self.number_of_cards: int = len(self.cards)
        self.history: List[Card] = []
        self.name: str = name
        self.is_human: bool = is_human
        self.points: int = 0

    def play(self) -> Card:
        """Randomly pick a card for the player to play
        and returns that card"""
        if (self.cards):
            if(not self.is_human):
                random_card_index = randint(0, self.number_of_cards - 1)
                chosen_card = self.cards.pop(random_card_index)
            
            elif(self.is_human):
                chosen_card = self.cards.pop(self.choose_card())

            self.turn_count += 1
            self.number_of_cards -= 1
            self.history.append(chosen_card)
            print(f"{self.name:10}{Player._icons[self.is_human]} Score:{self.points:2} played: {str(chosen_card)}")
            return chosen_card
        else:
            return None
    
    def make_human(self) -> None:
        """Turns a robot player into a human player"""
        self.is_human = True

    def choose_card(self) -> Card:
        """This function will display a players current hand and ask which card they want to play"""
        hand = ""
        choice = -1
        for index, card in enumerate(self.cards):
            hand += f" {index:2}:{card} "
        hand +="\n"
        print(f"Player: {self.name}")
        while True:
            try:
                print(hand)
                choice = int(input(f"Which card do you want to play ?(0-{len(self.cards)-1})"))
            except ValueError:
                print("Incorrect input please try again")
                continue
            if(choice < 0 or choice >= len(self.cards)):
                print("Incorrect input please try again")

            else:
                break
        
        return choice   

    def deal(self, card: Card) -> None:
        """Deals a new card to the players hand"""
        self.cards.append(card)
        self.number_of_cards = len(self.cards)

    def add_point(self) -> None:
        self.points += 1

    def get_points(self) -> int:
        return self.points

    def __str__(self) -> str:
        """Returns a string representation of the class"""
        return f"{self.name:15} Hand:{str(self.cards)}"


class Deck:
    """Class that represents an entire 52 card deck

    Attributes:
        cards: a list of cards left in the deck
    """

    def __init__(self) -> None:
        """Creates Deck class with no cards"""
        self.cards: List[Card] = []

    def fill_deck(self) -> None:
        """Fills deck with 52 cards (13 values of 4 icons)"""
        _icons = ["♥", "♦", "♣", "♠"]
        _values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
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
        """Given a list of players divides card evenly among them"""
        while self.cards:
            for player in players:
                if self.cards:
                    player.deal(self.draw())

    def __str__(self) -> str:
        """Returns a string representation of the class"""
        ret = ""
        for card in self.cards:
            ret += str(card)
        return ret
