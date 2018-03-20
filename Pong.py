"""
Pong.py
Scripted by: Philipp Koehler, Lars Kuehmichel
Description: Pong Game created as an exercise.
"""

import pygame as pg
import utils
import key_listener
import os
from player import Player
from ball import Ball
from button import Button

# window and general game settings
screen_width = 800
screen_height = 800
fullscreen = False
# causes lag if above ~ 300, default: 144
tickrate = 144
# default: 720
player_speed = 720
box_size = 30


# useful colours
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
buttonhover = (50, 50, 50)

# Maximum concurrent balls, set 0 for no limit
max_balls = 300

player_img_path = "resources/BouncePads/default.png"
ball_img_path = "resources/Balls/default.png"
font_path = "resources/Fonts/block_merged.ttf"

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

# creating player objects
p1 = Player("Lars", True, [20, (screen_height - p_height) / 2])
p2 = Player("Felipper, aka 1 dude", True, [screen_width - 20 - p_width, (screen_height - p_height) / 2])

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

    menutitle = font.render("Main Menu", False, black)
    menutitle_rect = menutitle.get_rect()
    menutitle_rect.center = ((screen_width/2), (screen_height / 4))

    playbutton = Button("Play", font2, (screen_height / 4 + menutitle.get_rect().height + 70), screen_width)
    modebutton = Button("Modes", font2, (playbutton.start_height + playbutton.height + 30), screen_width)
    settingsbutton = Button("Settings", font2, (modebutton.start_height + modebutton.height + 30), screen_width)
    exitbutton = Button("Exit", font2, (settingsbutton.start_height + settingsbutton.height + 30), screen_width)

    while menu:
        events = pg.event.get()
        pressed = key_listener.menuchecks(events)
        if pressed == "escape":
            pg.quit()
            exit(0)

        # Check for button clicks
        if playbutton.is_clicked(events):
            game_loop()
            return
        if modebutton.is_clicked(events):
            print("No Modes available yet")
        if settingsbutton.is_clicked(events):
            settings_loop()
            return
        if exitbutton.is_clicked(events):
            pg.quit()
            exit(0)

        # drawing menu title and button texts
        screen.fill(white)
        screen.blit(menutitle, menutitle_rect)
        playbutton.draw(screen)
        modebutton.draw(screen)
        settingsbutton.draw(screen)
        exitbutton.draw(screen)

        pg.display.update()

    # menu tickrate
    # default: 30
    clock.tick(30)


def settings_loop():
    settings = True
    while settings:
        events = pg.event.get()
        mouse = pg.mouse.get_pos()

        screen.fill(white)

        # Menu Title

        settingstitle = font.render("Settings", False, black)
        settingstitle_rect = settingstitle.get_rect()
        settingstitle_rect.center = ((screen_width / 2), (screen_height / 4))

        # Resolutions Button

        resbuttontext = "Resolution"
        resbutton, res_sur, res_rect = utils.create_button(resbuttontext, (screen_height / 4 +
                                                                           settingstitle.get_rect().height + 70),
                                                              font2, screen_width)

        # Return Button

        returnbuttontext = "Return"
        returnbutton, return_sur, return_rect = utils.create_button(returnbuttontext, (resbutton.center[1] +
                                                                    resbutton.height), font2, screen_width)

        # button functions

        pressed = key_listener.menuchecks(events)

        if pressed == "leftclick":
            if resbutton.collidepoint(mouse[0], mouse[1]):
                resolutions_loop()
                return
            if returnbutton.collidepoint(mouse[0], mouse[1]):
                menu_loop()
                return
        elif pressed == "escape":
            menu_loop()
            return

        # drawing resolutions button with hover effect
        if resbutton.collidepoint(mouse[0], mouse[1]):
            pg.draw.rect(screen, buttonhover, resbutton)
        else:
            pg.draw.rect(screen, black, resbutton)

        # drawing return button with hover effect
        if returnbutton.collidepoint(mouse[0], mouse[1]):
            pg.draw.rect(screen, buttonhover, returnbutton)
        else:
            pg.draw.rect(screen, black, returnbutton)

        screen.blit(settingstitle, settingstitle_rect)
        screen.blit(res_sur, res_rect)
        screen.blit(return_sur, return_rect)

        pg.display.update()


def resolutions_loop():
    global fullscreen, screen_width, screen_height
    resolutions = True
    while resolutions:
        events = pg.event.get()
        mouse = pg.mouse.get_pos()

        screen.fill(white)

        # Menu Title

        restitle = font.render("Select a Resolution", False, black)
        restitle_rect = restitle.get_rect()
        restitle_rect.center = ((screen_width / 2), (screen_height / 4))

        # Fullscreen Toggle Button

        if fullscreen:
            fullscrnbuttontext = "Toggle Fullscreen: ON"
        else:
            fullscrnbuttontext = "Toggle Fullscreen: OFF"
        fullscrnbutton, fullscrn_sur, fullscrn_rect = utils.create_button(fullscrnbuttontext, (screen_height / 4 +
                                                                           restitle.get_rect().height + 70),
                                                           font2, screen_width)

        # 600 x 600

        res_1_buttontext = "600 x 600"
        res_1_button, res_1_sur, res_1_rect = utils.create_button(res_1_buttontext, (fullscrnbutton.center[1] +
                                                                                       fullscrnbutton.height), font2,
                                                                    screen_width)

        # 1280 x 720

        # button functions

        pressed = key_listener.menuchecks(events)

        if pressed == "leftclick":
            if fullscrnbutton.collidepoint(mouse[0], mouse[1]):
                if fullscreen:
                    fullscreen = False
                else:
                    fullscreen = True
                return
            if res_1_button.collidepoint(mouse[0], mouse[1]):
                screen_width = 600
                screen_height = 600
                return
        elif pressed == "escape":
            settings_loop()
            return


def game_loop():
    if fullscreen:
        pg.mouse.set_visible(False)
    # loop for as long as running is true
    running = True
    while running:
        events = pg.event.get()
        if key_listener.keychecks(p1, p2, events):
            pause_menu()
            return

        # Positions and collisions
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

        # update the screen
        pg.display.update()

        # game update rate
        clock.tick(tickrate)

        # menu_loop()


def pause_menu():
    pg.mouse.set_visible(True)

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

        # Make background transparent

        menutitle = font.render("PAUSE", False, white)
        menutitle_rect = menutitle.get_rect()
        menutitle_rect.center = ((screen_width/2), (screen_height / 2))
        screen.blit(menutitle, menutitle_rect)

        # button = pg.rect(screen, green, (150, 550, 100, 50))
        # buttontext = font2.render("This is a button", False, black)
        # buttontext_rect = buttontext.get_rect()
        # # adjusting button width for the contained text
        # button.width = buttontext_rect.width + 30
        # buttontext_rect.center = button.center
        # screen.blit(buttontext, buttontext_rect)

        pg.display.update()

        # menu tickrate
        # default: 60
        clock.tick(30)


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
    ball.get_pos()[0] += ball.get_vel()[0] * ball.get_speed() / tickrate
    ball.get_pos()[1] += ball.get_vel()[1] * ball.get_speed() / tickrate
    if ball.get_pos()[1] < 0 or ball.get_pos()[1] > (screen_height - b_height):
        ball.get_vel()[1] = - ball.get_vel()[1]
    if ball.get_pos()[0] <= 0:
        p2.score += 1
        ball.set_pos(ball_startpos)
        ball.set_random_vel()
        if len(balls_list) < max_balls or max_balls == 0:
            balls_list.append(Ball(ball_startpos))
    if ball.get_pos()[0] >= screen_width:
        p1.score += 1
        ball.set_pos(ball_startpos)
        ball.set_random_vel()
        if len(balls_list) < max_balls or max_balls == 0:
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

    if clipping_rect.width <= clipping_rect.height:
        ball.get_vel()[0] = - ball.get_vel()[0]
    else:
        ball.get_vel()[1] = - ball.get_vel()[1]

    ball_positioning(ball)

    ball.set_colliding(True)






game_intro()
menu_loop()
# game_loop()



