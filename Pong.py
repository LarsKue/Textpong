"""
Pong.py
Scripted by: Philipp Koehler, Lars Kuehmichel
Description: Pong Game created as an exercise.
"""

import pygame as pg
import utils
from player import Player
from ball import Ball

# window and general game settings
screen_width = 1280
screen_height = 720
box_size = 30
black = (0, 0, 0)
white = (255, 255, 255)

player_img_path = "resources/BouncePads/default.png"
ball_img_path = "resources/Balls/default.png"

pg.init()
pg.display.set_caption("Pong")

screen = pg.display.set_mode((screen_width, screen_height))
clock = pg.time.Clock()

# initializing WASD keys (where a is equal to w and d is equal to s)
# keys = [False, False]

# checking player model size
p_width, p_height = utils.get_image_size(player_img_path)
b_width, b_height = utils.get_image_size(ball_img_path)

p1 = Player("Lars", True, [20, (screen_height - p_width) / 2])
p2 = Player("Felipperinerinerinerinerinerinerino der übelste dude of Doomness ( ͡° ͜ʖ ͡°)", True, [screen_width - 20 - p_width, (screen_height - p_width) / 2])

ball = Ball([(screen_width - b_width) / 2, (screen_height - b_height) / 2])

player_im = pg.image.load(player_img_path)
ball_im = pg.image.load(ball_img_path)

running = True


def loop():
    import key_listener
    # loop for as long as running is true
    while running:
        key_listener.keychecks(p1, p2)
        positioning(p1)
        positioning(p2)
        ball_positioning(ball)
        # fill the screen with black before drawing anything
        screen.fill(black)
        # drawing players at the given positions
        screen.blit(player_im, p1.get_pos())
        screen.blit(player_im, p2.get_pos())
        screen.blit(ball_im, ball.get_pos())
        # update the screen
        pg.display.update()
        # game update rate
        clock.tick(144)


def positioning(player):
    # moving the player up or down
    if player.get_keys()[0]:
        player.get_pos()[1] -= 5
    if player.get_keys()[1]:
        player.get_pos()[1] += 5
    # keeping the player in the window
    if player.get_pos()[1] < 0 + box_size:
        player.get_pos()[1] = 0 + box_size
    if player.get_pos()[1] > (screen_height - p_height - box_size):
        player.get_pos()[1] = screen_height - p_height - box_size


def ball_positioning(ball):
    ball.get_pos()[0] += ball.vel()[0]
    ball.get_pos()[1] += ball.vel()[1]


loop()



