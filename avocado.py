#!/usr/bin/env python3

import pygame, random
from support import operations

class Avocado:

    def __init__(self, screen, color, size, target, filename='img/AvoCado_0.png'):

        # HELP please!!
        # We randomly decide whether we should instanciate or not
        # I'd rather just not return an instance,
        # but I don't know how to do that :(
        if random.randint(0,1) == 0:
            self.is_falling = False
            self.has_been_pinned = False
            return None

        # Set up our instance variables
        self.screen = screen
        self.color = color
        self.target = target
        self.screen_width, self.screen_height = screen.get_size()
        self.w, self.y = size

        # Initialize the image
        self.i = pygame.image.load(filename).convert_alpha()
        operations.color_surface(self.i, color)
        self.image = pygame.transform.scale(self.i, (self.w, self.y))
        self.rect = self.image.get_rect()

        # Set the avocado's initial position and velocity
        self.init_pos()
        self.vx = 2
        self.vy = 4

        self.is_falling = True
        self.has_been_pinned = False


    def setTargetColor(self, targetColor):
        self.target = targetColor


    def blitme(self):
        self.screen.blit(self.image, self.rect)


    def init_pos(self):
        self.rect.x = random.randint(0, self.screen_width)
        self.rect.y = random.randint(20, 70)


    def isHit(self, click):
        """
        Checks whether this object collides with the given position
        of a mouse-click. Return true is the correct color was hit and
        false if it was the wrong one.
        Just returns void if no avocado was hit
        """
        mousex, mousey = click
        if self.rect.left < mousex and self.rect.right > mousex and \
            self.rect.top < mousey and self.rect.bottom > mousey:

            if self.color == self.target:
                self.has_been_pinned = True
                return True
            else:
                return False


    def exists(self):
        return not self.has_been_pinned and self.is_falling


    def move(self):
        if not self.has_been_pinned:
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
            print('DEBUG :: splatsh!')
            return True


    def destroy(self):
        del(self)