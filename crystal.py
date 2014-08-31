#!/usr/bin/env python3
"""
A class that represents a lawyer
"""

import os, pygame
from support import operations
from support.colors import *

class Crystal:

    def __init__(self, screen):
        self.screen = screen
        screen_width, screen_height = screen.get_size()
        self.rect = self.screen.get_rect()
        self.imageCenterX = self.rect.centerx
        self.imageCenterY = self.rect.centery
        self.pos = (self.imageCenterX-100,self.imageCenterY-5,200,183)

    def getBoundaries(self):
        return self.pos


    def blitme(self):
        pygame.draw.ellipse(self.screen, self.color, self.pos, 0)


    def setColor(self, color):
        self.color = color

