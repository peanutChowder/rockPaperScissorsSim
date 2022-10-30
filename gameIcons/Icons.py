import pygame

class Icons():
    imgSize = (30, 30)
    iconClasses = ["Rock", "Paper", "Scissors"]

    @staticmethod
    def getPngPath(iconClass: str):
        return f"icons/{iconClass.lower()}.png"

    def __init__(self, idNum: int, iconClass: str) -> None:
        self.velocity = [None, None]
        self.weaknessOrder = {
            "Rock": "Paper",
            "Paper": "Scissors",
            "Scissors": "Rock"
        }

        self.iconClass = iconClass
        self.id = f"{iconClass},{idNum}"
        self.png = Icons.getPngPath(iconClass)
        self.img = self.getPygameImage()
        self.imgRect = self.img.get_rect()
        

    def getPygameImage(self) -> pygame.surface.Surface:
        img = pygame.image.load(self.png)
        return pygame.transform.scale(img, Icons.imgSize)

    def convertClass(self, newClass: str):
        x, y = self.imgRect.center
        self.iconClass = newClass
        self.png = Icons.getPngPath(newClass)
        self.img = self.getPygameImage()
        self.imgRect = self.img.get_rect()
        self.setLocation(x, y)

    def getIconClass(self) -> str:
        return self.iconClass

    def isPreyOf(self, otherIcon: 'Icons'):
        weakness = self.weaknessOrder[self.iconClass]

        return otherIcon.getIconClass() == weakness


    def setVelocity(self, velX: int, velY: int):
        self.velocity = [velX, velY]

    def getVelocity(self) -> list[int, int]:
        return self.velocity

    def setLocation(self, locX: int, locY: int):
        self.imgRect.center = [locX, locY]

    def getLocation(self) -> tuple[float, float]:
        return self.imgRect.center

    def getImg(self) -> pygame.Surface:
        return self.img

    def getImgRect(self):
        return self.imgRect

    def move(self) -> None:
        self.imgRect.x += self.velocity[0]
        self.imgRect.y += self.velocity[1]

    