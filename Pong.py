"""
Pong.py
Scripted by: Philipp Koehler, Lars Kuehmichel
Description: Pong Game created as an exercise.
"""

import pygame as pg
import utils
import time
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

# checking player model size
p_width, p_height = utils.get_image_size(player_img_path)
b_width, b_height = utils.get_image_size(ball_img_path)

p1 = Player("Lars", True, [20, (screen_height - p_height) / 2])
p2 = Player("Felipperinerinerinerinerinerinerino der übelste dude of Doomness ( ͡° ͜ʖ ͡°)", True, [screen_width - 20 - p_width, (screen_height - p_height) / 2])

ball_startpos = [(screen_width - b_width) / 2, (screen_height - b_height) / 2]
ball = Ball(ball_startpos)

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
        check_collision(ball, p1, p2)
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
    ball.get_pos()[0] += ball.get_vel()[0] * ball.get_speed()
    ball.get_pos()[1] += ball.get_vel()[1] * ball.get_speed()
    if ball.get_pos()[1] < 0 or ball.get_pos()[1] > (screen_height - b_height):
        ball.get_vel()[1] = - ball.get_vel()[1]
    if ball.get_pos()[0] <= 0 or ball.get_pos()[0] >= screen_width:
        ball.set_pos(ball_startpos)
        ball.set_random_vel()


def check_collision(ball, p1, p2):
    ball_rect = pg.Rect(ball.get_pos()[0], ball.get_pos()[1], b_width, b_height)
    p1_rect = pg.Rect(p1.get_pos()[0], p1.get_pos()[1], p_width, p_height)
    p2_rect = pg.Rect(p2.get_pos()[0], p2.get_pos()[1], p_width, p_height)

    if pg.Rect.colliderect(ball_rect, p1_rect):
        handle_collision(ball, ball_rect, p1_rect)

    elif pg.Rect.colliderect(ball_rect, p2_rect):
        handle_collision(ball, ball_rect, p2_rect)


def handle_collision(ball, ball_rect, p_rect):
    if (time.time() - ball.get_last_collision()) < (1.2 / ball.get_speed()):
        return

    clipping_rect = pg.Rect.clip(ball_rect, p_rect)

    if clipping_rect.width < clipping_rect.height:
        ball.get_vel()[0] = - ball.get_vel()[0]
    elif clipping_rect.width == clipping_rect.height:
        ball.get_vel()[0] = - ball.get_vel()[0]
        ball.get_vel()[1] = - ball.get_vel()[1]
    else:
        ball.get_vel()[1] = - ball.get_vel()[1]

    ball_positioning(ball)

    ball.set_last_collision(time.time())







loop()



