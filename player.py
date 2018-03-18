"""
player.py
Subclass for Pong.py
Scripted by: Philipp Koehler, Lars Kuehmichel
Description: Defines the player object and common properties
"""


class Player:
    name = "Digga aldah"
    size = 1
    human = True
    keys = [False, False]
    pos = [0, 0]

    def __init__(self, name, human, pos):
        self.name = name
        self.human = human
        self.pos = pos

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_human(self, human):
        self.human = human

    def get_human(self):
        return self.human

    def get_keys(self):
        return self.keys

    def get_pos(self):
        return self.pos