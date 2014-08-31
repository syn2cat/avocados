#!/usr/bin/env python3

import pygame, random, os
from support import operations

class Avocado:

    def __init__(self, screen, boundaries, properties, target, level, filename=os.path.join('img', 'AvoCado_0_PINK.png')):

        # Set up our instance variables
        self.screen = screen
        self.screen_width, self.screen_height = screen.get_size()
        self.avocados = {(255,0,0): os.path.join('img', 'AvoCado_0_RED.png'), \
                         (0,255,0): os.path.join('img', 'AvoCado_0_GREEN.png'), \
                         (0,0,255): os.path.join('img', 'AvoCado_0_BLUE.png'), \
                         (255,255,0): os.path.join('img', 'AvoCado_0_YELLOW.png'), \
                         (255,192,203): os.path.join('img', 'AvoCado_0_PINK.png')}
        self.color = properties['color']
        self.w, self.y = properties['size']
        self.filename = self.avocados[self.color]
        self.target = target
        self.boundaries = boundaries
        self.checkObstacle = True

        # Initialize the image
        self.i = pygame.image.load(filename).convert_alpha()
        self.i = pygame.image.load(self.filename)
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
        # Checking screen boundaries
        if self.rect.right > self.screen_width or self.rect.left < 0:
            self.checkObstacle = True
            self.vx = -self.vx

        # Checking for obstacle collisions
        for obstacle in self.boundaries:
            left, top, width, height = obstacle
            right = left + width
            bottom = top + height

            if self.checkObstacle \
             and (self.rect.right < right and self.rect.left > left):
                self.checkObstacle = False
                # print(self.rect.bottom, top)
                # if self.rect.bottom > top:
                #     self.vy = -self.vy

            if self.checkObstacle \
             and ((self.rect.right > right and self.rect.left < right) \
             or (self.rect.left < left and self.rect.right > left)):
                if self.rect.bottom > top:
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
        if self.rect.top > self.screen_height:
            self.is_still_falling = False
            print('DEBUG :: splatch!')
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
