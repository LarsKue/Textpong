"""
player.py
Subclass for Pong.py
Scripted by: Philipp Koehler, Lars Kuehmichel
Description: Defines the player object and common properties
"""


class Player:

    def __init__(self, name, human, pos):
        self.name = name
        self.human = human
        self.pos = [pos[0], pos[1]]
        self.keys = [False, False]
        self.size = 1
        self.score = 0
        self.startpos = [pos[0], pos[1]]

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

    def reset(self):
        self.pos = [self.startpos[0], self.startpos[1]]
        self.keys = [False, False]
        self.size = 1
        self.score = 0
