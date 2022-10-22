from gameIcons.Icons import Icons

class Rock(Icons):
    iconClass = "Rock"
    def __init__(self, id) -> None:
        super().__init__(id, "icons/rock.png", Rock.iconClass)