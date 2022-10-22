import gameIcons.Icons, gameIcons.Rock, gameIcons.Paper, gameIcons.Scissors
import random

class GameLogic():
    def __init__(self) -> None:
        self.maxSpeeds = [2, 2]
        self.allIcons = {}

    def getIconObjs(self) -> list[gameIcons.Icons.Icons]:
        return self.allIcons.values()

    def initIcons(self, teamSize):
        for iconClass in [gameIcons.Rock.Rock, gameIcons.Paper.Paper, gameIcons.Scissors.Scissors]:
            for i in range(teamSize):
                self.allIcons[iconClass.iconClass] = iconClass(i)

    def initRandomLocations(self, windowX, windowY):
        for icon in self.allIcons.values():
            locX = random.randint(0, windowX)
            locY = random.randint(0, windowY)

            icon.setLocation(locX, locY)

    def initRandomSpeeds(self):
        for icon in self.allIcons.values():
            velX = random.randint(0, self.maxSpeeds[0])
            velY = random.randint(0, self.maxSpeeds[1])

            icon.setVelocity(velX, velY)

    

