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
        self.speed = 6
        self.vel = [1, 1]
        self.set_random_vel()

    def set_pos(self, pos):
        self.pos = [pos[0], pos[1]]
        print(pos)

    def get_pos(self):
        return self.pos

    def get_vel(self):
        return self.vel

    def set_speed(self, speed):
        self.speed = speed

    def get_speed(self):
        return self.speed

    def set_random_vel(self):
        x = random.uniform(0.3, 0.85)
        y = np.sqrt(1 - x ** 2)

        if random.randint(0, 1) == 0:
            x = -x
        if random.randint(0, 1) == 0:
            y = -y

        print([x, y])

        self.vel = [x, y]
