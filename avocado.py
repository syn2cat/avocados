#!/usr/bin/env python3

import pygame, random
from support import operations

class Avocado:

    def __init__(self, screen, color, size, target, sound=True, filename='img/AvoCado_0.png'):

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
        self.vx = 10
        self.vy = 10
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


    def mute(self,mute=False):
        if not sound:
            return
        if mute:
            pygame.mixer.music.set_volume(0.0)
        else:
            pygame.mixer.music.set_volume(0.5)


    def playLevel(self,lvl=1):
        if not sound:
            return
        if lvl == 1:
            pygame.mixer.music.load("""audio/level1.wav""")
        elif lvl == 2:
            pygame.mixer.music.load("""audio/level2.wav""")
        elif lvl == 3:
            pygame.mixer.music.load("""audio/level3.wav""")
        pygame.mixer.music.play()


    def fade(self):
        if not sound:
            return
        pygame.mixer.music.fadeout(3000)


    def loadClick(self):
        if not sound:
            return
        self.click = pygame.mixer.Sound("audio/click.wav")
        return self.click

    def destroy(self):
        del(self)
