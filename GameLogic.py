import gameIcons.Icons, gameIcons.Rock, gameIcons.Paper, gameIcons.Scissors
import random

COLLIDE_OFFSET = 0

class GameLogic():
    def __init__(self) -> None:
        self.maxSpeeds = [2, 2]
        self.allIcons = {}
        self.iconRects = {}

    def getAllIcons(self):
        return self.allIcons

    def getIconObjs(self) -> list[gameIcons.Icons.Icons]:
        return self.allIcons.values()

    def initIcons(self, teamSize):
        for iconClass in [gameIcons.Rock.Rock, gameIcons.Paper.Paper, gameIcons.Scissors.Scissors]:
            for i in range(teamSize):
                self.allIcons[f"{iconClass.iconClass},{i}"] = iconClass(i)

    def initIconsGeneric(self, teamSize):

        for iconClass in gameIcons.Icons.Icons.iconClasses:
            for i in range(teamSize):
                self.allIcons[f"{iconClass},{i}"] = gameIcons.Icons.Icons(i, iconClass)

    def initIconRects(self):
        self.iconRects = {icon.id: icon.getImgRect() for icon in self.getIconObjs()}

    def initRandomLocations(self, windowX, windowY):
        for icon in self.allIcons.values():
            locX = random.randint(0, windowX)
            locY = random.randint(0, windowY)

            icon.setLocation(locX, locY)

    def initRandomSpeeds(self):
        for icon in self.allIcons.values():
            velX = random.randint(-self.maxSpeeds[0], self.maxSpeeds[0])
            velY = random.randint(-self.maxSpeeds[1], self.maxSpeeds[1])

            icon.setVelocity(velX, velY)

    def iconWindowBounce(self, icon: gameIcons.Icons.Icons, windowSize: tuple[int, int]):
        xVel, yVel = icon.getVelocity()

        if icon.getImgRect().left < COLLIDE_OFFSET or icon.getImgRect().right > windowSize[0] - COLLIDE_OFFSET:
            xVel = -xVel
        if icon.getImgRect().top < COLLIDE_OFFSET or icon.getImgRect().bottom > windowSize[1] - COLLIDE_OFFSET:
            yVel = -yVel

        icon.setVelocity(xVel, yVel)

    def handleCollide(self, icon: gameIcons.Icons.Icons):
        self.iconRects.pop(icon.id)
        
        # Collision happened
        collisionInfo =  icon.getImgRect().collidedict(self.iconRects, 1)

        if collisionInfo != None:
            iconId = collisionInfo[0]
            otherIcon = self.allIcons[iconId]

            if icon.isPreyOf(otherIcon):
                icon.convertClass(otherIcon.getIconClass())

            

        self.iconRects[icon.id] = icon.getImgRect()


    

