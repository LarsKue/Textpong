# key_listener.py
# subclass for Pong.py
# Scripted by: Philipp Koehler, Lars Kuehmichel


from pygame.locals import *
import pygame as pg


def keychecks(keys):
    for event in pg.event.get():
        print(event)
        # checking if the player presses the close window button (X at top right)
        if event.type == pg.QUIT:
            pg.quit()
            exit(0)
        # checking for key down presses (WASD)
        if event.type == pg.KEYDOWN:
            if event.key == K_w or event.key == K_a:
                keys[0] = True
            if event.key == K_s or event.key == K_d:
                keys[1] = True
        # checking for key releases (WASD)
        if event.type == pg.KEYUP:
            if event.key == pg.K_w or event.key == K_a:
                keys[0] = False
            if event.key == pg.K_s or event.key == K_d:
                keys[1] = False
