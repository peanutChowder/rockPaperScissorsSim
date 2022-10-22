from gameIcons.Icons import Icons

class Scissors(Icons):
    iconClass = "Scissors"
    def __init__(self, id) -> None:
        super().__init__(id, "icons/scissors.png", Scissors.iconClass)