"""
button.py
Subclass for Pong.py
Scripted by: Philipp Koehler, Lars Kuehmichel
Description: Defines the button object and common properties
"""

import pygame as pg


class Button:
    def __init__(self, text, font, top, space, align=True):
        # If align, then top is a rect and space the space from the rect to this button
        # Else top is the top of this button and space the y value of the middle of this button
        if align:
            self.top = top.bottom + space
            self.middle_x = top.center[0]
        else:
            self.top = top
            self.middle_x = space

        self.text = text
        self.font = font
        self.width = 325
        self.height = 100
        self.text_color = [255, 255, 255]
        self.text_hover_color = [255, 255, 255]
        self.box_color = [0, 0, 0]
        self.box_hover_color = [50, 50, 50]

        self.button_rect = None
        self.button_text_obj = None
        self.button_text_rect = None

        self.update()

    def get_rect(self):
        return self.button_rect

    def update(self):
        self.button_rect = pg.Rect(0, 0, self.width, self.height)
        self.button_rect.center = (self.middle_x, self.top + self.height / 2)

        self.button_text_obj = self.font.render(self.text, False, self.text_color)
        self.button_text_rect = self.button_text_obj.get_rect()
        self.button_text_rect.center = self.button_rect.center

    def draw(self, screen):
        # Draw box
        if self.hovering():
            pg.draw.rect(screen, self.box_hover_color, self.button_rect)
            self.button_text_obj = self.font.render(self.text, False, self.text_hover_color)
        else:
            pg.draw.rect(screen, self.box_color, self.button_rect)
            self.button_text_obj = self.font.render(self.text, False, self.text_color)

        # Draw text
        screen.blit(self.button_text_obj, self.button_text_rect)

    def is_clicked(self, events):
        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.hovering():
                        return True
        return False

    def hovering(self):
        mouse = pg.mouse.get_pos()
        return self.button_rect.collidepoint(mouse[0], mouse[1])
