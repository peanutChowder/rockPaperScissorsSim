from gameIcons.Icons import Icons

class Paper(Icons):
    iconClass = "Paper"
    def __init__(self, id) -> None:
        super().__init__(id, "icons/paper.png", Paper.iconClass)