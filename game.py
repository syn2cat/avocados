#!/usr/bin/env python3
"""
Avocados and stuff
"""

import os, random
import pygame
from pygame.locals import *

from support.colors import *
from interface import hud

def main():
    pygame.init()
    pygame.display.set_caption('Avocados')
    clock = pygame.time.Clock()

    # Move this outside the main code?
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width,screen_height))
    bg = BLACK
    desired_fps = 60

    font = pygame.font.Font(None, 40)
    game_over = font.render('GAME OVER', 0, RED)
    my_hud = hud.Hud((screen_width, screen_height))

    score = 0
    time = 15

    running = True
    timeleft = time
    while running:
        time_passed = clock.tick(desired_fps)
        fps = clock.get_fps()

        screen.fill(bg)

        timeleft -= time_passed / 1000
        timeleft = round(timeleft,2)

        if timeleft <= 0:
            screen.blit(game_over, (screen_width/3, screen_height/2))

        chud = my_hud.draw_hud(score, timeleft, round(fps,2))
        screen.blit(chud, (10,10))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()


if __name__ == '__main__':
    main()
