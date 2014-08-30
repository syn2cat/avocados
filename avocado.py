#!/usr/bin/env python3

import pygame, random
from support import operations

class Avocado:

    def __init__(self, screen, color, size, filename='img/AvoCado_0.png'):
        print('New avocado is ' + ','.join(str(color)))
        self.screen = screen
        self.screen_width, self.screen_height = screen.get_size()
        self.x = random.randint(0, self.screen_width)
        self.y = 0  # change this to start somewhere above the screen
        self.w , self.y = size

        self.i = pygame.image.load(filename).convert_alpha()
        operations.color_surface(self.i, color)
        self.image = pygame.transform.scale(self.i, (self.w, self.y))
        self.pycard = self.image.get_rect()

        self.init_pos()
        self.step_x = 10
        self.step_y = 10
        self.is_destroyed = False

    def init_pos(self):
        self.pycard.x = random.randint(0, self.screen_width)
        self.pycard.y = random.randint(20, 70)
        self.is_destroyed = False

    def collides(self, click):
        """
        Checks whether this object collides with the given position
        in click
        """
        mousex, mousey = click
        if self.pycard.left < mousex and self.pycard.right > mousex and \
                self.pycard.top < mousey and self.pycard.bottom > mousey:
            self.destroy()
            return True
        return False
        #if collision then self.destroy()

    def destroy(self):
        """destroys this object"""
        self.is_destroyed = True

    def move(self):
        if self.pycard.right > self.screen_width or self.pycard.left < 0:
            self.step_x = -self.step_x
        if self.is_destroyed or self.pycard.bottom > self.screen_height \
                or self.pycard.top < 0:
            print('platch')
            return False
        print(self.pycard.x, self.pycard.y)
        self.pycard.x += self.step_x
        self.pycard.y += self.step_y
        return True
