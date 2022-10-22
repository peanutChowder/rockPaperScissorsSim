import pygame, sys

import GameLogic

TEAM_SIZES = 10
WINDOW_SIZE = (1200, 800)

pygame.init()


def handleQuit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def main():
    pygame.init()

    GL = GameLogic.GameLogic()
    GL.initIcons(TEAM_SIZES)
    GL.initRandomLocations(*WINDOW_SIZE)
    GL.initRandomSpeeds()


    screen = pygame.display.set_mode(WINDOW_SIZE)

    while True:
        handleQuit()
        screen.fill((255,255,255))
        
        for icon in GL.getIconObjs():
            GL.iconWindowBounce(icon, WINDOW_SIZE)
            icon.move()
            screen.blit(icon.getImg(), icon.getImgRect())
        pygame.display.flip()

        pygame.time.delay(10)

main()

