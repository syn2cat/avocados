#!/usr/bin/env python3

import os, pygame
from support import operations
from support.colors import *

class Lawyer:

    def __init__(self, screen):
        self.screen = screen
        screen_width, screen_height = screen.get_size()
        temp_image = pygame.image.load(os.path.join('img', 'lawyer.png'))
        # WARNING!! Absolute sizes
        self.image = pygame.transform.scale(temp_image, (200, 400))
        rect = self.image.get_rect()
        self.pos = (screen_width - rect.w, screen_height - rect.h)

    def blitme(self):
        operations.color_surface(self.image, WHITE)
        self.screen.blit(self.image, self.pos)
