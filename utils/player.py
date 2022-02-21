from typing import List


from card import Card
from random import randint

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
        a turn_count on 0 and an empty history """
        self.cards: List[Card] = cards
        self.turn_count: int = 0
        self.number_of_cards: int = len(cards)
        self.history: List[Card] = []
        self.name = name

    def play(self) -> Card:
        """Randomly pick a card for the player to play
        and returns that card"""
        random_card_index = randint(0, self.number_of_cards)
        card = self.cards.pop(random_card_index)
        self.turn_count += 1
        self.number_of_cards -= 1
        self.history.append(card)
        print(f"{self.name} {self.turn_count} played: {card.getValue()} {card.getSymbol()}")
        return card

    def deal(self,card: Card) -> None:
        """Deals a new card to the players hand"""
        self.cards.append(card)
        self.number_of_cards += 1
        

