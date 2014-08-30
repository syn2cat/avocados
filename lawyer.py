#!/usr/bin/env python3
"""
A class that represents a lawyer
"""

import os, pygame
from support import operations
from support.colors import *

class Lawyer:

    def __init__(self, screen):
        self.screen = screen
        screen_width, screen_height = screen.get_size()
        temp_image = pygame.image.load(os.path.join('img', 'lawyer.png'))
        # WARNING!! FIXME Absolute sizes FIXME
        self.image = pygame.transform.scale(temp_image, (220, 400))
        self.rect = self.image.get_rect()
        operations.color_surface(self.image, WHITE)
        self.pos = (screen_width - self.rect.w, screen_height - self.rect.h)

    def blitme(self):
        """ Blit this object to the screen """
        self.image.blit(self.pane, (self.rect.left, self.rect.bottom / 2))
        self.screen.blit(self.image, self.pos)

    def setColor(self, color):
        """ Announces the color to pin by drawing a rectangle
        and filling it with a color """
        self.pane = pygame.Surface((200, 100))
        self.pane.fill(color)
