

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
    _icons = ["♣", "♠", "♦", "♥"]
    

    def __init__(self, icon: str) -> None:
        """Creates Symbol with icon and color based of the icon"""
        self.icon: str = icon

        if icon == "♥" or icon == "♦":
            self.color: str = "red"
        if icon == "♣" or icon == "♠":
            self.color: str = "black"

    def __str__(self) -> str:
        """Returns a string representation of the class"""
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
    _values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self, icon: str, value: str) -> None:
        """Creates Card with with icon and color based of the icon
        and assigns a value"""
        super().__init__(icon)
        self.value: str = value


    #Base comparisons on the index of the _values list e.g. higher in the list means higher value
    #if the values are equal compare the suits , lowest to highest again (♣ < ♠ < ♦ < ♥)
    def __lt__(self,other) -> bool:
        """smaller then operator"""
        if(Card._values.index(self.value) == Card._values.index(other.value)):
            return Symbol._icons.index(self.icon) < Symbol._icons.index(other.icon)
        return Card._values.index(self.value) < Card._values.index(other.value)

    def __eq__(self,other) -> bool:
        """equals operator"""
        return Card._values.index(self.value) == Card._values.index(other.value)

    def __gt__(self,other) -> bool:
        """greater then operator"""
        if(Card._values.index(self.value) == Card._values.index(other.value)):
            return Symbol._icons.index(self.icon) > Symbol._icons.index(other.icon)
        return Card._values.index(self.value) > Card._values.index(other.value)


    def __str__(self) -> str:
        """Returns a string representation of the class"""
        if self.color == "red":
            return f"{_C_RED}{self.value:2}{self.icon}{_C_END} "
        else:
            return f"{_C_BLACK}{self.value:2}{self.icon}{_C_END} "

    def __repr__(self) -> str:
        """Returns a string representation of the class"""
        if self.color == "red":
            return f"{_C_RED}{self.value:2}{self.icon}{_C_END} "
        else:
            return f"{_C_BLACK}{self.value:2}{self.icon}{_C_END} "
