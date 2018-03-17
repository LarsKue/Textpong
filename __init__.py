# Text Pong
# Scripted by: Philipp Koehler, Lars Kuehmichel
# Description: Pong Game created as an exercise.

import pygame as pg
from pygame.locals import *

pg.init()
width, height = 640, 480
screen = pg.display.set_mode((width, height))

player = pg.image.load("resources/Player.jpg")

# loop for as long as exit code is 1
while 1:
    # fill the screen with black before drawing anything
    screen.fill(0)
    # draw the player at the given position
    screen.blit(player, (100, 100))
    # update the screen
    pg.display.update()
    for event in pg.event.get():
        # checking if the player presses the close window button (X at top right)
        if event.type == pg.QUIT:
            pg.quit()
            exit(0)
