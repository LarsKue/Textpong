"""
key_listener.py
Subclass for Pong.py
Scripted by: Philipp Koehler, Lars Kuehmichel
"""


from pygame.locals import *
import pygame as pg


def keychecks(p1, p2, events):
    for event in events:
        # checking if the player presses the close window button (X at top right)
        if event.type == pg.QUIT:
            pg.quit()
            exit(0)

        # checking for key down presses
        if event.type == pg.KEYDOWN:
            if event.key == K_ESCAPE:
                return True
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

    return False


def introchecks(events):
    for event in events:
        if event.type == pg.QUIT:
            pg.quit()
            exit(0)
        # skipping menus upon left clicking or hitting Escape
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                return True
        if event.type == pg.KEYDOWN:
            if event.key == K_ESCAPE:
                return True
    return False


def menuchecks(events):
    for event in events:
        if event.type == pg.QUIT:
            pg.quit()
            exit(0)
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                return "leftclick"
        if event.type == pg.KEYDOWN:
            if event.key == K_ESCAPE:
                return "escape"


def pausechecks(events):
    for event in events:
        if event.type == pg.QUIT:
            pg.quit()
            exit(0)
        if event.type == pg.KEYDOWN:
            if event.key == K_ESCAPE:
                return True
    return False
