#!/usr/bin/env python3

import pygame
import random

class Avocado:

    def __init__(self, screen, color, filename='img/AvoCado_0.png'):
        print('New avocado is ' + ','.join(str(color)))
        self.screen_width, self.screen_height = screen.get_size()
        self.x = random.randint(0, self.screen_width)
        self.y = 0  # change this to start somewhere above the screen
        self.w = 100
        self.y = 100
        self.i = pygame.image.load(filename).convert_alpha()
        self.image = pygame.transform.scale(self.i, (30, 30))
        self.pycard = self.image.get_rect()

        self.pycard.x = random.randint(0, self.screen_width)
        self.pycard.y = random.randint(20, 70)
        self.step_x = 10
        self.step_y = 10
        self.is_falling = True

    def reset(self):
        self.pycard.x = random.randint(0, self.screen_width)
        self.pycard.y = random.randint(0, 50)

    def collides(self, click):
        """
        Checks whether this object collides with the given position
        in click
        """
        return True
        #if collision then self.destroy()

    def destroy(self):
        """destroys this object"""

    def move(self):
        if self.pycard.right > self.screen_width or self.pycard.left < 0:
            self.step_x = -self.step_x
        if self.pycard.bottom > self.screen_height or self.pycard.top < 0:
            print('platch')
            return False
            self.is_falling = False
        self.pycard.x += self.step_x
        self.pycard.y += self.step_y
        return True

