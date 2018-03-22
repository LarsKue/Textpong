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
        # default: 860
        self.speed = 860
        self.vel = [1, 1]
        self.colliding = False
        self.just_spawned = True
        self.starting_pos = [pos[0], pos[1]]

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

    def set_colliding(self, colliding):
        self.colliding = colliding

    def is_colliding(self):
        return self.colliding

    def get_velocity(self):
        speed_modifier = 1

        if self.just_spawned:
            speed_modifier = 0.65

        x = self.get_vel()[0] * self.get_speed() * speed_modifier
        y = self.get_vel()[1] * self.get_speed() * speed_modifier

        return [x, y]

    def set_random_vel(self):
        # default: 0.35, 0.9
        x = random.uniform(0.7, 0.99)
        y = np.sqrt(1 - x ** 2)

        if random.randint(0, 1) == 0:
            x = -x
        if random.randint(0, 1) == 0:
            y = -y

        self.vel = [x, y]

    def reset(self):
        self.set_pos(self.starting_pos)
        self.set_random_vel()
        self.just_spawned = True
