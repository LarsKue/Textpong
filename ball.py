"""
ball.py
Subclass for Pong.py
Scripted by: Philipp Koehler, Lars Kuehmichel
Description: Defines the ball object and common properties
"""


class Ball:

    def __init__(self, pos):
        self.pos = pos
        self.vel = [1, 0]

    def get_pos(self):
        return self.pos

    def get_vel(self):
        return self.vel
