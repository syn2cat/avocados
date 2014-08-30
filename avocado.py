#!/usr/bin/env python3

import pygame, random

class Avocado:

    def __init__(self, screensize):
        screen_width, screen_height = screensize
        self.x = random.randint(0,screen_width)
        self.y = 0 # change this to start somewhere above the screen
        self.w = 100
        self.y = 100

    def collides(self, click):
        """
        Checks whether this object collides with the given position
        in click
        """
        return True
        #if collision then self.destroy()

    def destroy(self):
        """destroys this object"""

