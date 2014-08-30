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
        self.imageCenterX = self.screen.get_rect().centerx
        self.imageCenterY = self.screen.get_rect().centery

    def setColor(self, color):
        """ Announces the color to pin by drawing a rectangle
        and filling it with a color """
        pygame.draw.ellipse(self.screen, (color), (self.imageCenterX-158,self.imageCenterY-5,277,217), 0)
        print("Drawing {} ellipse".format(color))
