#!/usr/bin/env python3
"""
Avocados and stuff
"""

import os, random
import pygame
from pygame.locals import *

from support import colors
from interface import hud

# Move this outside
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
bg = (0,0,0)
screen.fill(bg)

def main():
    pygame.init()
    pygame.display.set_caption('Avocados')
    clock = pygame.time.Clock()
    score = 0
    time = 33

    running = True
    while running:
        # Limit to 50 fps
        time_passed = clock.tick(30)
        fps = clock.get_fps()

        my_hud = hud.draw_hud(score, time, fps)
        screen.blit(my_hud, (10,10))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()

if __name__ == '__main__':
    main()
