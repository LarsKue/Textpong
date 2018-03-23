"""
text.py
Subclass for Pong.py
Scripted by: Philipp Koehler, Lars Kuehmichel
Description: Defines the text object and common properties
"""


class Text:
    def __init__(self, text, font, color, x, y):
        self.text = text
        self.font = font
        self.color = color
        self.x = x
        self.y = y

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

    def set_pos(self, x, y):
        raise NotImplementedError  # you want to override this on the child classes

    def get_rect(self):
        return self.text_rect

    def update(self):
        self.text_obj = self.font.render(self.text, False, self.color)
        self.text_rect = self.text_obj.get_rect()
        self.set_pos(self.x, self.y)

    def draw(self, screen):
        screen.blit(self.text_obj, self.text_rect)


class TextLeft(Text):
    def __init__(self, text, font, color, left, top):
        super(TextLeft, self).__init__(text, font, color, left, top)

    def set_pos(self, left, top):
        self.x = left
        self.y = top
        self.text_rect.left = left
        self.text_rect.top = top


class TextRight(Text):
    def __init__(self, text, font, color, right, top):
        super(TextRight, self).__init__(text, font, color, right, top)

    def set_pos(self, right, top):
        self.x = right
        self.y = top
        self.text_rect.right = right
        self.text_rect.top = top


class TextCenter(Text):
    def __init__(self, text, font, color, center, top):
        super(TextCenter, self).__init__(text, font, color, center, top)

    def set_pos(self, center, top):
        self.x = center
        self.y = top
        self.text_rect.center = (center, top)
        self.text_rect.top = top
