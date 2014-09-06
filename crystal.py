#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

"""
A class that represents a lawyer
"""

import os, pygame, random
from support import operations
from support.colors import *

class Crystal:

    def __init__(self, screen, level, font, psychomode):
        self.psychomode = psychomode
        self.screen = screen
        screen_width, screen_height = screen.get_size()
        screen_rect = self.screen.get_rect()
        self.imageCenterX = screen_rect.centerx
        self.imageCenterY = screen_rect.centery
        self.pos = (self.imageCenterX-100,self.imageCenterY-5,200,183)
        self.level = level
        self.font = font
        self.colorTexts = {
            RED: 'RED',
            GREEN: 'GREEN',
            BLUE: 'BLUE',
            YELLOW: 'YELLOW',
            PINK: 'PINK'
        }


    def getBoundaries(self):
        return self.pos


    def blitme(self):
        myrect = pygame.draw.ellipse(self.screen, self.thecolor, self.pos, 0)
        if self.level >= self.psychomode:
            self.text = self.font.render(self.colorTexts[self.color], 0, WHITE)
            self.screen.blit(self.text, myrect)


    def setColor(self, color):
        self.color = color
        self.thecolor = self.color
        if self.level >= self.psychomode:
            colors = [RED, GREEN, BLUE, YELLOW, PINK]
            self.thecolor = colors[random.randint(0,len(colors) - 1)]

