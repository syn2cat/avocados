#!/usr/bin/env python3

import pygame, random
from support import operations

class Avocado:

    def __init__(self, screen, color, size, select, filename='img/AvoCado_0.png'):
        # We randomly decide whether we should instanciate or not
        if random.randint(0,1) == 0:
            self.is_falling = False
            return None

        print('New avocado is ' + ','.join(str(color)))
        self.screen = screen
        self.color = color
        self.select = select
        self.screen_width, self.screen_height = screen.get_size()
        self.x = random.randint(0, self.screen_width)
        self.y = 0  # change this to start somewhere above the screen
        self.w , self.y = size

        # Initialize the image
        self.i = pygame.image.load(filename).convert_alpha()
        operations.color_surface(self.i, color)
        self.image = pygame.transform.scale(self.i, (self.w, self.y))
        self.rect = self.image.get_rect()

        # Set the avocado's initial position and velocity
        self.init_pos()
        self.vx = 10
        self.vy = 10
        self.is_falling = True


    def blitme(self):
        self.screen.blit(self.image, self.rect)


    def init_pos(self):
        self.rect.x = random.randint(0, self.screen_width)
        self.rect.y = random.randint(20, 70)


    def collides(self, click):
        """
        Checks whether this object collides with the given position
        in click
        """
        mousex, mousey = click
        if self.rect.left < mousex and self.rect.right > mousex and \
                self.rect.top < mousey and self.rect.bottom > mousey and \
				self.color == self.select:
            self.destroy()
            return True

    def destroy(self):
        """destroys this object"""
        del(self)

    def exists(self):
        return self.is_falling


    def move(self):
        if self.rect.right > self.screen_width or self.rect.left < 0:
            self.vx = -self.vy

        if self.hasLanded():
            self.destroy()

        self.rect.x += self.vx
        self.rect.y += self.vy
        return True


    def hasLanded(self):
        if self.rect.bottom > self.screen_height or self.rect.top < 0:
            self.is_falling = False
            print('platch')
            return True


