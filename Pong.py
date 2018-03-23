"""
Pong.py
Scripted by: Philipp Koehler, Lars Kuehmichel
Description: Pong Game created as an exercise.
"""

import pygame as pg
import utils
import key_listener
import os
import numpy as np
from player import Player
from ball import Ball
from button import Button
from text import Text

# window and general game settings
screen_width = 1280
screen_height = 720
fullscreen = False
# causes lag if above ~ 300, default: 144
tickrate = 144
tickrate_menu = 30
# default: 720
player_speed = 720
box_size = 30

# Modi
multiball = True

# useful colours
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
grey = (50, 50, 50)
light_grey = (100, 100, 100)

# Maximum concurrent balls, set 0 for no limit
max_balls = 500

player_img_path = "resources/BouncePads/default.png"
ball_img_path = "resources/Balls/default.png"
font_path = "resources/Fonts/block_merged.ttf"

# window starts centered
os.environ['SDL_VIDEO_CENTERED'] = '1'
pg.init()
pg.display.set_caption("Pong")

icon = pg.image.load("resources/default_icon.png")
pg.display.set_icon(icon)

# hiding the cursor if the game is played in full screen mode
if fullscreen:
    screen = pg.display.set_mode((screen_width, screen_height), pg.FULLSCREEN)
    pg.mouse.set_visible(False)
else:
    screen = pg.display.set_mode((screen_width, screen_height))

clock = pg.time.Clock()

# checking player model size
p_width, p_height = utils.get_image_size(player_img_path)
b_width, b_height = utils.get_image_size(ball_img_path)

startpos_p1 = [20, (screen_height - p_height) / 2]
startpos_p2 = [screen_width - 20 - p_width, (screen_height - p_height) / 2]

# creating player objects
p1 = Player("Lars", True, startpos_p1)
p2 = Player("Felipper, aka 1 dude", True, startpos_p2)

balls_list = []

# useful fonts
font_size = 40
font = pg.font.Font(font_path, font_size)

font_size = 20
font2 = pg.font.Font(font_path, font_size)

# score screen
score_p1 = font.render("0", False, white)
score_p2 = font.render("0", False, white)
score_minus = font.render("-", False, white)

name_p1 = font2.render("", False, white)
name_p2 = font2.render("", False, white)

ball_startpos = [(screen_width - b_width) / 2, (screen_height - b_height) / 2]
ball = Ball(ball_startpos)
balls_list.append(ball)

player_im = pg.image.load(player_img_path)
ball_im = pg.image.load(ball_img_path)


def game_intro():
    intro = True
    # time delay for fullscreen to establish
    pg.time.delay(2500)
    # default: -225
    fade = -255
    wait = 0

    while intro:
        events = pg.event.get()
        if key_listener.introchecks(events):
            menu_loop()
            return

        screen.fill(white)
        title = font.render("Pong", False, black)
        title.set_alpha(255 - abs(fade))
        title_rect = title.get_rect()
        title_rect.center = ((screen_width / 2), (screen_height / 2))
        screen.blit(title, title_rect)

        pg.time.delay(1)
        pg.display.update()

        if fade == 0 and wait <= 200:
            wait += 1
        else:
            fade += 1

        if fade > 255:
            menu_loop()
            return

        clock.tick(tickrate)


def menu_loop():
    pg.mouse.set_visible(True)
    menu = True

    menutitle = Text("Main Menu", font, black, (screen_width / 2), (screen_height / 8))

    playbutton = Button("Play", font2, menutitle.get_rect(), 30)
    modebutton = Button("Modes", font2, playbutton.get_rect(), 30)
    settingsbutton = Button("Settings", font2, modebutton.get_rect(), 30)
    exitbutton = Button("Exit", font2, settingsbutton.get_rect(), 30)
    i = 0

    while menu:
        events = pg.event.get()
        pressed = key_listener.menuchecks(events)
        if pressed == "escape":
            pg.quit()
            exit(0)

        # Check for button clicks
        if playbutton.is_clicked(events):
            start_new_game()
            return
        if modebutton.is_clicked(events):
            print("No Modes available yet")
            playbutton.text = str(i)
            playbutton.update()
            i += 1
        if settingsbutton.is_clicked(events):
            settings_loop()
            return
        if exitbutton.is_clicked(events):
            pg.quit()
            exit(0)

        # drawing menu title and button texts
        screen.fill(white)
        menutitle.draw(screen)
        playbutton.draw(screen)
        modebutton.draw(screen)
        settingsbutton.draw(screen)
        exitbutton.draw(screen)

        pg.display.update()

        clock.tick(tickrate_menu)


def settings_loop():
    settings = True

    # creating submenu title
    settingstitle = Text("Settings", font, black, screen_width / 2, screen_height / 4)

    # creating buttons
    resbutton = Button("Resolution", font2, settingstitle.get_rect(), 30)
    returnbutton = Button("Return", font2, resbutton.get_rect(), 30)

    while settings:
        events = pg.event.get()
        # checking button presses
        if key_listener.menuchecks(events) == "escape":
            menu_loop()
            return
        if resbutton.is_clicked(events):
            resolutions_loop()
            return
        if returnbutton.is_clicked(events):
            menu_loop()
            return

        # drawing buttons
        screen.fill(white)
        settingstitle.draw(screen)
        resbutton.draw(screen)

        pg.display.update()
        clock.tick(tickrate_menu)


def resolutions_loop():
    global fullscreen, screen_width, screen_height, screen
    resolutions = True

    # creating submenu title
    restitle = Text("Select a Resolution", font, black, screen_width / 2, screen_height / 15)

    # creating fullscreen toggle button
    fullscrnbutton = Button("Toggle Fullscreen: OFF", font2, restitle.get_rect(), 30)
    if fullscreen:
        fullscrnbutton.text = "Toggle Fullscreen: ON"

    fullscrnbutton.width = 400
    fullscrnbutton.update()

    # creating resolution buttons
    # 600 x 600
    res_1_button = Button("600 x 600", font2, fullscrnbutton.get_rect(), 30)

    # 1280 x 720
    res_2_button = Button("1280 x 720", font2, res_1_button.get_rect(), 30)

    # 1920 x 1080
    res_3_button = Button("1920 x 1080", font2, res_2_button.get_rect(), 30)

    # 2560 x 1440
    res_4_button = Button("2560 x 1440", font2, res_3_button.get_rect(), 30)

    while resolutions:
        events = pg.event.get()

        if key_listener.menuchecks(events) == "escape":
            settings_loop()
            return
        if fullscrnbutton.is_clicked(events):
            if fullscreen:
                fullscreen = False
                screen = pg.display.set_mode((screen_width, screen_height))
                resolutions_loop()
                return
            else:
                fullscreen = True
                screen = pg.display.set_mode((screen_width, screen_height), pg.FULLSCREEN)
                resolutions_loop()
                return
        if res_1_button.is_clicked(events):
            update_resolution(600, 600)
            resolutions_loop()
            return
        if res_2_button.is_clicked(events):
            update_resolution(1280, 720)
            resolutions_loop()
            return
        if res_3_button.is_clicked(events):
            update_resolution(1920, 1080)
            resolutions_loop()
            return
        if res_4_button.is_clicked(events):
            update_resolution(2560, 1440)
            resolutions_loop()
            return

        screen.fill(white)
        restitle.draw(screen)
        fullscrnbutton.draw(screen)
        res_1_button.draw(screen)
        res_2_button.draw(screen)
        res_3_button.draw(screen)
        res_4_button.draw(screen)

        pg.display.update()
        clock.tick(tickrate_menu)


def game_loop():
    if fullscreen:
        pg.mouse.set_visible(False)

    timer_font = pg.font.Font(font_path, 100)
    timer_1 = Text("1", timer_font, white, screen_width / 2, screen_height / 3)
    timer_2 = Text("2", timer_font, white, screen_width / 2, screen_height / 3)
    timer_3 = Text("3", timer_font, white, screen_width / 2, screen_height / 3)
    start_size = 25
    end_size = 110
    size_diff = end_size - start_size

    new_game_timer = 3 * tickrate
    running = True
    while running:
        events = pg.event.get()
        if key_listener.keychecks(p1, p2, events):
            pause_menu()
            return

        # Positions and collisions
        if new_game_timer <= 0:
            positioning(p1)
            positioning(p2)
            for ball in balls_list:
                ball_positioning(ball)
                check_collision(ball, p1, p2)

        # Update score
        global score_p1, score_p2
        score_p1 = font.render(str(p1.score), False, white)
        score_p2 = font.render(str(p2.score), False, white)

        # Update names
        global name_p1, name_p2
        name_p1 = font2.render(p1.name, False, white)
        name_p2 = font2.render(p2.name, False, white)

        # Rendering the game
        # Make background black
        screen.fill(black)

        # Render player at position
        screen.blit(player_im, p1.get_pos())
        screen.blit(player_im, p2.get_pos())

        # Render balls
        for ball in balls_list:
            screen.blit(ball_im, ball.get_pos())

        # Render score
        screen.blit(score_p1, (screen_width / 2 - 20 - score_p1.get_rect().width, 3))
        screen.blit(score_p2, (screen_width / 2 + 20, 3))
        screen.blit(score_minus, (screen_width / 2 - score_minus.get_rect().width / 2, 3))

        # Render player names
        screen.blit(name_p1, (3, 3))
        screen.blit(name_p2, (screen_width - name_p2.get_rect().width - 3, 3))

        # Render timer
        if new_game_timer > 0:
            if new_game_timer <= tickrate:
                # Scale timer
                size = int(round(start_size + size_diff - (new_game_timer / tickrate * size_diff)))
                timer_font2 = pg.font.Font(font_path, size)
                timer_1.set_font(timer_font2)
                timer_1.draw(screen)
            elif new_game_timer <= tickrate * 2:
                size = int(round(start_size + size_diff - ((new_game_timer - tickrate) / tickrate * size_diff)))
                timer_font2 = pg.font.Font(font_path, size)
                timer_2.set_font(timer_font2)
                timer_2.draw(screen)
            elif new_game_timer <= tickrate * 3:
                size = int(round(start_size + size_diff - ((new_game_timer - tickrate * 2) / tickrate * size_diff)))
                timer_font2 = pg.font.Font(font_path, size)
                timer_3.set_font(timer_font2)
                timer_3.draw(screen)
            new_game_timer -= 1

        # update the screen
        pg.display.update()

        # game update rate
        clock.tick(tickrate)


def pause_menu():
    pg.mouse.set_visible(True)

    pausetitle = Text("Pause", font, white, screen_width / 2, screen_height / 4)

    playbutton = Button("Continue", font2, pausetitle.get_rect(), 30)
    playbutton.box_color = light_grey
    playbutton.box_hover_color = white
    playbutton.text_color = white
    playbutton.text_hover_color = black
    playbutton.update()
    exitbutton = Button("Exit", font2, playbutton.get_rect(), 30)
    exitbutton.box_color = light_grey
    exitbutton.box_hover_color = white
    exitbutton.text_color = white
    exitbutton.text_hover_color = black
    exitbutton.update()

    background = pg.Surface([screen_width, screen_height])
    background.fill((0, 0, 0))
    background.set_alpha(25)
    screen.blit(background, [0, 0])
    fade = 15

    pause = True
    while pause:
        events = pg.event.get()
        if key_listener.pausechecks(events):
            game_loop()
            return

        # Multiplies multiple backgrounds to achieve fade effect
        if fade > 0:
            screen.blit(background, [0, 0])
            fade -= 1
            # print((1-255/25/100)**(15-fade))

        if playbutton.is_clicked(events):
            game_loop()
            return
        if exitbutton.is_clicked(events):
            menu_loop()
            return

        pausetitle.draw(screen)
        playbutton.draw(screen)
        exitbutton.draw(screen)
        pg.display.update()

        # menu tickrate
        clock.tick(tickrate_menu)


def positioning(player):
    # moving the player up or down
    if player.get_keys()[0]:
        player.get_pos()[1] -= 720 / tickrate
    if player.get_keys()[1]:
        player.get_pos()[1] += 720 / tickrate
    # keeping the player in the window
    if player.get_pos()[1] < 0 + box_size:
        player.get_pos()[1] = 0 + box_size
    if player.get_pos()[1] > (screen_height - p_height - box_size):
        player.get_pos()[1] = screen_height - p_height - box_size


def ball_positioning(ball):
    ball.get_pos()[0] += ball.get_velocity()[0] / tickrate
    ball.get_pos()[1] += ball.get_velocity()[1] / tickrate
    if ball.get_pos()[1] < 0 or ball.get_pos()[1] > (screen_height - b_height):
        ball.get_vel()[1] = - ball.get_vel()[1]
    if ball.get_pos()[0] <= 0:
        p2.score += 1
        ball.reset()
        if multiball and len(balls_list) < max_balls or max_balls == 0:
            balls_list.append(Ball(ball_startpos))
    if ball.get_pos()[0] >= screen_width:
        p1.score += 1
        ball.reset()
        if multiball and len(balls_list) < max_balls or max_balls == 0:
            balls_list.append(Ball(ball_startpos))


def check_collision(ball, p1, p2):
    ball_rect = pg.Rect(ball.get_pos()[0], ball.get_pos()[1], b_width, b_height)
    p1_rect = pg.Rect(p1.get_pos()[0], p1.get_pos()[1], p_width, p_height)
    p2_rect = pg.Rect(p2.get_pos()[0], p2.get_pos()[1], p_width, p_height)

    if pg.Rect.colliderect(ball_rect, p1_rect):
        handle_collision(ball, ball_rect, p1_rect)

    elif pg.Rect.colliderect(ball_rect, p2_rect):
        handle_collision(ball, ball_rect, p2_rect)

    else:
        ball.set_colliding(False)


def handle_collision(ball, ball_rect, p_rect):
    if ball.is_colliding():
        return

    clipping_rect = pg.Rect.clip(ball_rect, p_rect)

    # Check for wrong collisions and change directory on collision
    if clipping_rect.width <= clipping_rect.height:
        if p_rect.center[0] < clipping_rect.center[0] and ball.get_vel()[0] > 0:
            return
        elif p_rect.center[0] > clipping_rect.center[0] and ball.get_vel()[0] < 0:
            return

        # Calculate bounce back
        cur_dist = p_rect.center[1] - ball_rect.center[1]
        max_dist = (p_rect.height + ball_rect.height) / 2

        modx = 1
        mody = 1
        if ball.get_vel()[0] > 0:
            modx = -1
        if cur_dist > 0:
            mody = -1

        x = ((1 - abs(cur_dist) / max_dist) * 0.5 + 0.5) * modx
        y = np.sqrt(1 - abs(x) ** 2) * mody

        ball.get_vel()[0] = x
        ball.get_vel()[1] = y

    else:
        if p_rect.center[1] < clipping_rect.center[1] and ball.get_vel()[1] > 0:
            return
        elif p_rect.center[1] > clipping_rect.center[1] and ball.get_vel()[1] < 0:
            return
        ball.get_vel()[1] = - ball.get_vel()[1]

    ball_positioning(ball)

    ball.set_colliding(True)
    ball.just_spawned = False


def start_new_game():
    # Resets players
    p1.reset()
    p2.reset()

    # Resets balls
    del balls_list[:]
    balls_list.append(Ball(ball_startpos))

    # Starts the game
    game_loop()


def update_resolution(width, height):
    global screen, screen_width, screen_height
    screen_width = width
    screen_height = height
    if fullscreen:
        screen = pg.display.set_mode((screen_width, screen_height), pg.FULLSCREEN)
    else:
        screen = pg.display.set_mode((screen_width, screen_height))






game_intro()
menu_loop()
# game_loop()



