_icons = ["♥", "♦", "♣", "♠"]
_values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

# Escape codes to print the cards with colors
_C_BLACK = "\033[30;47m"
_C_RED = "\033[31;47m"
_C_END = "\033[0m"


class Symbol:
    """Class that represents a symbol on a card

    Attributes:
        icon: A single character string out of the list _icons
        color: A string based on the icon either "red" or "black"
    """

    def __init__(self, icon: str) -> None:
        """Creates Symbol with icon and color based of the icon"""
        self.icon: str = icon

        if icon == "♥" or icon == "♦":
            self.color: str = "red"
        if icon == "♣" or icon == "♠":
            self.color: str = "black"

    def __str__(self) -> str:
        if self.color == "red":
            return f"{_C_RED}{self.icon}{_C_END}"
        else:
            return f"{_C_BLACK}{self.icon}{_C_END}"


class Card(Symbol):
    """Class that represents a playing card

    Attributes:
        value: A string out of the list _values

    Inherited Attributes from Symbol:
        icon: A single character string out of the list _icons
        color: A string based on the icon either "red" or "black"

    """

    def __init__(self, icon: str, value: str) -> None:
        """Creates Card with with icon and color based of the icon
        and assigns a value"""
        super().__init__(icon)
        self.value: str = value

    def __str__(self) -> str:
        if self.color == "red":
            return f"{_C_RED}{self.value:2}{self.icon}{_C_END} "
        else:
            return f"{_C_BLACK}{self.value:2}{self.icon}{_C_END} "

    def __repr__(self) -> str:
        if self.color == "red":
            return f"{_C_RED}{self.value:2}{self.icon}{_C_END} "
        else:
            return f"{_C_BLACK}{self.value:2}{self.icon}{_C_END} "
