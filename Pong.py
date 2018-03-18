"""
Pong.py
Scripted by: Philipp Koehler, Lars Kuehmichel
Description: Pong Game created as an exercise.
"""

import pygame as pg
import utils
import key_listener
from player import Player
from ball import Ball

# window and general game settings
screen_width = 1920
screen_height = 1080
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

pg.init()
pg.display.set_caption("Pong")

icon = pg.image.load("resources/default_icon.png")
pg.display.set_icon(icon)

if fullscreen:
    screen = pg.display.set_mode((screen_width, screen_height), pg.FULLSCREEN)
    pg.mouse.set_visible(False)
else:
    screen = pg.display.set_mode((screen_width, screen_height))

clock = pg.time.Clock()

# checking player model size
p_width, p_height = utils.get_image_size(player_img_path)
b_width, b_height = utils.get_image_size(ball_img_path)

p1 = Player("Lars", True, [20, (screen_height - p_height) / 2])
p2 = Player("Felipper, aka 1 dude", True, [screen_width - 20 - p_width, (screen_height - p_height) / 2])

balls_list = []

font_size = 40
font = pg.font.Font(font_path, font_size)

score_p1 = font.render("0", False, white)
score_p2 = font.render("0", False, white)
score_minus = font.render("-", False, white)

font_size = 20
font2 = pg.font.Font(font_path, font_size)

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

    while intro:
        if key_listener.introchecks():
            menu_loop()
            return
        screen.fill(white)
        title = font.render("Pong", False, black)
        title.set_alpha(255 - abs(fade))
        title_rect = title.get_rect()
        title_rect.center = ((screen_width / 2), (screen_height / 2))
        screen.blit(title, title_rect)
        if fade == 0:
            for delay in range(200):
                if not key_listener.introchecks():
                    intro = False
                    break
                pg.time.delay(10)
        pg.time.delay(1)
        pg.display.update()
        fade += 1
        if fade > 255:
            menu_loop()
            return


def menu_loop():
    pg.mouse.set_visible(True)
    menu = True
    while menu:
        mouse = pg.mouse.get_pos()

        pressed = key_listener.menuchecks()
        if pressed == "leftclick":
            game_loop()
            return
        elif pressed == "escape":
            pg.quit()
            exit(0)

        screen.fill(white)

        menutitle = font.render("This is a menu", False, black)
        menutitle_rect = menutitle.get_rect()
        menutitle_rect.center = ((screen_width/2), (screen_height / 4))

        # Play button

        playbuttontext = "Play"
        playbutton, play_sur, play_rect = utils.create_button(text=playbuttontext, startheight=(screen_height / 4 +
                                                                           menutitle.get_rect().height + 70))

        # Modes button

        modebuttontext = "Modes"
        modebutton, mode_sur, mode_rect = utils.create_button(modebuttontext, (playbutton.center[1] + playbutton.height))

        # Settings button

        settingsbuttontext = "Settings"
        settingsbutton, settings_sur, settings_rect = utils.create_button(settingsbuttontext, (modebutton.center[1] +
                                                                                               modebutton.height))

        # Exit button

        exitbuttontext = "Exit"
        exitbutton, exit_sur, exit_rect = utils.create_button(exitbuttontext, (settingsbutton.center[1] +
                                                                               settingsbutton.height))

        # drawing play button with hover effect
        if playbutton.collidepoint(mouse[0], mouse[1]):
            pg.draw.rect(screen, buttonhover, playbutton)
        else:
            pg.draw.rect(screen, black, playbutton)

        # drawing mode button with hover effect
        if modebutton.collidepoint(mouse[0], mouse[1]):
            pg.draw.rect(screen, buttonhover, modebutton)
        else:
            pg.draw.rect(screen, black, modebutton)

        # drawing settings button with hover effect
        if settingsbutton.collidepoint(mouse[0], mouse[1]):
            pg.draw.rect(screen, buttonhover, settingsbutton)
        else:
            pg.draw.rect(screen, black, settingsbutton)

        # drawing exit button with hover effect
        if exitbutton.collidepoint(mouse[0], mouse[1]):
            pg.draw.rect(screen, buttonhover, exitbutton)
        else:
            pg.draw.rect(screen, black, exitbutton)

        # drawing menu title and button texts
        screen.blit(menutitle, menutitle_rect)
        screen.blit(play_sur, play_rect)
        screen.blit(mode_sur, mode_rect)
        screen.blit(settings_sur, settings_rect)
        screen.blit(exit_sur, exit_rect)

        pg.display.update()

    # menu tickrate
    # default: 30
    clock.tick(30)


def game_loop():
    pg.mouse.set_visible(False)
    # loop for as long as running is true
    running = True
    while running:
        if key_listener.keychecks(p1, p2):
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
    pause = True
    while pause:
        if key_listener.pausechecks():
            game_loop()
            return

        # Make background transparent
        background = pg.Surface([screen_width, screen_height])
        background.set_alpha(100)
        screen.blit(background, [0, 0])

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



