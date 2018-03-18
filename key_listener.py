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

        # checking for key down presses
        if event.type == pg.KEYDOWN:
            if event.key == K_ESCAPE:
                pg.quit()
                exit(0)
            if event.key == K_w or event.key == K_a:
                p1.get_keys()[0] = True
            if event.key == K_s or event.key == K_d:
                p1.get_keys()[1] = True
            if event.key == K_UP or event.key == K_LEFT:
                p2.get_keys()[0] = True
            if event.key == K_DOWN or event.key == K_RIGHT:
                p2.get_keys()[1] = True

        # checking for key releases
        if event.type == pg.KEYUP:
            if event.key == pg.K_w or event.key == K_a:
                p1.get_keys()[0] = False
            if event.key == pg.K_s or event.key == K_d:
                p1.get_keys()[1] = False
            if event.key == pg.K_UP or event.key == K_LEFT:
                p2.get_keys()[0] = False
            if event.key == pg.K_DOWN or event.key == K_RIGHT:
                p2.get_keys()[1] = False


def introchecks():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit(0)
        # skipping menus upon left clicking or hitting Escape
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                return False
        if event.type == pg.KEYDOWN:
            if event.key == K_ESCAPE:
                return False
    return True


def menuchecks():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit(0)
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                return "leftclick"
        if event.type == pg.KEYDOWN:
            if event.key == K_ESCAPE:
                return "escape"
