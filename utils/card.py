_icons = ["♥", "♦", "♣", "♠"]
_values = ["A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K"]


class Symbol:
    """Class that represents a symbol on a card

    Attributes:
        icon: A single character string out of the list _icons
        color: A string based on the icon either "red" or "black"
    """

    def __init__(self, icon: str) -> None:
        """Inits Symbol with icon and color based of the icon"""
        self.icon: str = icon

        if icon == "♥" or "♦":
            self.color: str = "red"
        if icon == "♣" or "♠":
            self.color: str = "black"


class Card(Symbol):
    """Class that represents a playing card

    Attributes:
        value: A string out of the list _values
    """

    def __init__(self, icon: str, value: str) -> None:
        """Inits Card with with icon and color based of the icon
        and assigns a value"""
        super.__init__(self, icon)
        self.value: str = value

    def getValue(self) -> str:
        """Returns attribute value"""
        return self.value

    def getIcon(self) -> str:
        """Returns attribute icon"""
        return self.icon
