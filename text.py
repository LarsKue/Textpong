"""
text.py
Subclass for Pong.py
Scripted by: Philipp Koehler, Lars Kuehmichel
Description: Defines the text object and common properties
"""

import pygame as pg


class Text:
    def __init__(self, text, font, color, center_x, center_y):
        self.text = text
        self.font = font
        self.color = color
        self.center_x = center_x
        self.center_y = center_y

        self.text_obj = None
        self.text_rect = None

        self.update()

    def set_text(self, text):
        self.text = text
        self.update()

    def set_font(self, font):
        self.font = font
        self.update()

    def set_color(self, color):
        self.color = color
        self.text_obj = self.font.render(self.text, False, color)

    def set_pos(self, center_x, center_y):
        self.center_x = center_x
        self.center_y = center_y
        self.text_rect.center = (self.center_x, self.center_y)

    def get_rect(self):
        return self.text_rect

    def update(self):
        self.text_obj = self.font.render(self.text, False, self.color)
        self.text_rect = self.text_obj.get_rect()
        self.text_rect.center = (self.center_x, self.center_y)

    def draw(self, screen):
        screen.blit(self.text_obj, self.text_rect)
