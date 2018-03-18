# Pong.py
# Scripted by: Philipp Koehler, Lars Kuehmichel
# Description: Pong Game created as an exercise.

import pygame as pg
import utils

screen_width = 1280
screen_height = 720
black = (0, 0, 0)
white = (255, 255, 255)

pg.init()
pg.display.set_caption('Pong')

screen = pg.display.set_mode((screen_width, screen_height))
clock = pg.time.Clock()

# initializing WASD keys (where a is equal to w and d is equal to s)
keys = [False, False]

player = pg.image.load("resources/BouncePadSmall.png")

# checking player model size
p_width, p_height = utils.get_image_size("resources/BouncePadSmall.png")

# defining player starting position
# BouncePadSmall.png is 125 pixels high and we want the player to start centered
player_pos = [20, (screen_height - 125) / 2]

running = True


def loop():
    import key_listener
    # loop for as long as running is true
    while running:
        key_listener.keychecks(keys)
        if keys[0]:
            player_pos[1] -= 5
        if keys[1]:
            player_pos[1] += 5
        if player_pos[1] < 0:
            player_pos[1] = 0
        if player_pos[1] > (screen_height - 125):
            player_pos[1] = screen_height - 125

        # fill the screen with black before drawing anything
        screen.fill(black)
        # draw the player at the given position
        screen.blit(player, player_pos)
        # update the screen
        pg.display.update()

        clock.tick(144)





loop()



