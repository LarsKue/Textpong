"""
key_listener.py
Subclass for Pong.py
Scripted by: Philipp Koehler, Lars Kuehmichel
"""


from pygame.locals import *
import pygame as pg


def keychecks(p1, p2):
    for event in pg.event.get():
        # checking if the player presses the close window button (X at top right)
        if event.type == pg.QUIT:
            pg.quit()
            exit(0)
        # checking for key down presses (WASD)
        if event.type == pg.KEYDOWN:
            if event.key == K_w or event.key == K_a:
                p1.get_keys()[0] = True
            if event.key == K_s or event.key == K_d:
                p1.get_keys()[1] = True
            if event.key == K_UP or event.key == K_LEFT:
                p2.get_keys()[0] = True
            if event.key == K_DOWN or event.key == K_RIGHT:
                p2.get_keys()[1] = True
        # checking for key releases (WASD)
        if event.type == pg.KEYUP:
            if event.key == pg.K_w or event.key == K_a:
                p1.get_keys()[0] = False
            if event.key == pg.K_s or event.key == K_d:
                p1.get_keys()[1] = False
            if event.key == pg.K_UP or event.key == K_LEFT:
                p2.get_keys()[0] = False
            if event.key == pg.K_DOWN or event.key == K_RIGHT:
                p2.get_keys()[1] = False

