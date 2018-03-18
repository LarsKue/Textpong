"""
ball.py
Subclass for Pong.py
Scripted by: Philipp Koehler, Lars Kuehmichel
Description: Defines the ball object and common properties
"""

import random
import numpy as np


class Ball:

    def __init__(self, pos):
        self.pos = [pos[0], pos[1]]
        self.speed = 860
        self.vel = [1, 1]
        self.last_collision = 0

        self.set_random_vel()

    def set_pos(self, pos):
        self.pos = [pos[0], pos[1]]

    def get_pos(self):
        return self.pos

    def get_vel(self):
        return self.vel

    def set_speed(self, speed):
        self.speed = speed

    def get_speed(self):
        return self.speed

    def set_last_collision(self, last_collision):
        self.last_collision = last_collision

    def get_last_collision(self):
        return self.last_collision

    def set_random_vel(self):
        x = random.uniform(0.35, 0.9)
        y = np.sqrt(1 - x ** 2)

        if random.randint(0, 1) == 0:
            x = -x
        if random.randint(0, 1) == 0:
            y = -y


        self.vel = [x, y]
