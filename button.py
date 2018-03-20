"""
button.py
Subclass for Pong.py
Scripted by: Philipp Koehler, Lars Kuehmichel
Description: Defines the button object and common properties
"""

import pygame as pg


class Button:
    def __init__(self, text, font, start_height, screen_width):
        self.text = text
        self.font = font
        self.start_height = start_height
        self.screen_width = screen_width
        self.width = 325
        self.height = 100
        self.text_color = [255, 255, 255]
        self.text_hover_color = [255, 0, 255]
        self.box_color = [0, 0, 0]
        self.box_hover_color = [50, 50, 50]

        self.button = pg.Rect(0, 0, self.width, self.height)
        self.button.center = (self.screen_width / 2, self.start_height)

        self.button_text = font.render(text, False, self.text_color)
        self.button_text_rect = self.button_text.get_rect()
        self.button_text_rect.center = self.button.center

    def draw(self, screen):
        # Draw box
        if self.hovering():
            pg.draw.rect(screen, self.box_hover_color, self.button)
            self.button_text = self.font.render(self.text, False, self.text_hover_color)
        else:
            pg.draw.rect(screen, self.box_color, self.button)
            self.button_text = self.font.render(self.text, False, self.text_color)

        # Draw text
        screen.blit(self.button_text, self.button_text_rect)

    def is_clicked(self, events):
        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.hovering():
                        return True
        return False

    def hovering(self):
        mouse = pg.mouse.get_pos()
        return self.button.collidepoint(mouse[0], mouse[1])
