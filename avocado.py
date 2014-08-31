#!/usr/bin/env python3

import pygame, random
from support import operations

class Avocado:

    def __init__(self, screen, color, size, target, level, filename='img/AvoCado_0.png'):

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
        self.vy = 4 * (level * 0.5)

        # Avocado state
        self.is_still_falling = True
        self.has_been_pinned = False

        # Avocado sounds
        self.click = self.loadClick()
        self.clickFail = self.loadFailClick()


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
                self.is_still_falling = False
                self.click.play()
                return True, self.rect.center
            else:
                self.clickFail.play()
                return False, (0, 0)
        return None, (0, 0)
        # BUG - isHit is called 4 times upon click which makes it return the
        # first time but fail the consecutive times
        #else:
        #    self.clickFail.play()


    def isFalling(self):
        return self.is_still_falling


    def isPinned(self):
        return self.has_been_pinned


    def checkBoundaries(self):
        if self.rect.right > self.screen_width or self.rect.left < 0:
            self.vx = -self.vx


    def move(self):
        if not self.has_been_pinned:
            self.checkBoundaries()

            if self.hasLanded():
                self.destroy()

            self.rect.x += self.vx
            self.rect.y += self.vy
        return True


    def hasLanded(self):
        if self.rect.bottom > self.screen_height or self.rect.top < 0:
            self.is_still_falling = False
            print('DEBUG :: splash!')
            return True


    def loadClick(self, sound=True):
        if not sound:
            return
        return pygame.mixer.Sound("audio/click.wav")


    def loadFailClick(self, sound=True):
        if not sound:
            return
        return pygame.mixer.Sound("audio/poop.wav")


    def destroy(self):
        del(self)
