"""
utils.py
Subclass of Pong.py
Scripted by: Philipp Koehler, Lars Kuehmichel
Description: Common utilities and functions
"""


# checking dimensions of an image (e.g. the player's model)
def get_image_size(path):
    import get_image_size
    try:
        width, height = get_image_size.get_image_size(path)
    except get_image_size.UnknownImageFormat:
        width, height = -1, -1

    return width, height


def create_button(text, startheight):
    import pygame as pg
    from Pong import font2, screen_height, screen_width, white

    button = pg.Rect(0, 0, 325, 100)
    buttontext = font2.render(text, False, white)
    buttontext_rect = buttontext.get_rect()

    # adjusting width for contained text
    button.center = (screen_width / 2, startheight + 30)
    buttontext_rect.center = button.center

    return button, buttontext, buttontext_rect
