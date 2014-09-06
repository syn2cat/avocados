#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

import pygame
from support.colors import *

class Text:

    def __init__(self, container, text, pos, duration):
        """ Foo """
        self.clock = container['clock']
        self.duration = duration
        self.totalTime = 0
        self.text = container['font'].render(text, 0, WHITE)
        self.screen = container['screen']
        self.pos = pos


    def blitme(self):
        """ sd """
        self.screen.blit(self.text, self.pos)


    def hasExpired(self):
        self.totalTime += self.clock.get_time()
        if self.totalTime > self.duration:
            del(self)
            return True
        return False
