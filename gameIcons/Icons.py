import pygame

class Icons():
    imgSize = (30, 30)
    def __init__(self, id: int, png: str, iconClass: str) -> None:
        self.id = id
        self.png = png
        self.velocity = [None, None]
        self.location = [None, None]
        self.iconClass = iconClass

        self.preyOrder = {
            "Rock": "scissors",
            "Paper": "rock",
            "Scissors": "paper"
        }

        img = pygame.image.load(self.png)
        self.img =  pygame.transform.scale(img, Icons.imgSize)
        self.imgRect = self.img.get_rect()

    def setVelocity(self, velX: int, velY: int):
        self.velocity = [velX, velY]

    def getVelocity(self) -> list[int, int]:
        return self.velocity

    def setLocation(self, locX: int, locY: int):
        self.location = [locX, locY]

    def getLocation(self) -> list[int, int]:
        return self.location

    def getImg(self) -> pygame.Surface:
        return self.img

    def getImgRect(self):
        return self.imgRect

    