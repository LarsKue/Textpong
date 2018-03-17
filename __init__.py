# Text Pong
# Scripted by: Philipp Koehler, Lars Kuehmichel
# Description: Pong Game created as an exercise.

import pygame as pg
from pygame.locals import *

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
WHITE = (0, 0, 0)

pg.init()
pg.display.set_caption('TextPong')

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pg.time.Clock()

player = pg.image.load("resources/Player.jpg")

running = True

# loop for as long as running is true
while running:
    for event in pg.event.get():
        print(event)
        # checking if the player presses the close window button (X at top right)
        if event.type == pg.QUIT:
            pg.quit()
            exit(0)

    # fill the screen with black before drawing anything
    screen.fill(WHITE)
    # draw the player at the given position
    screen.blit(player, (100, 100))
    # update the screen
    pg.display.update()

    clock.tick(60)
