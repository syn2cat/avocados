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
        screen_rect = self.screen.get_rect()
        self.imageCenterX = screen_rect.centerx
        self.imageCenterY = screen_rect.centery
        self.pos = (self.imageCenterX-100,self.imageCenterY-5,200,183)


    def getBoundaries(self):
        return self.pos


    def blitme(self):
        pygame.draw.ellipse(self.screen, self.color, self.pos, 0)
        pygame.draw.rect(self.screen, WHITE, self.pos, 2)


    def setColor(self, color):
        self.color = color

