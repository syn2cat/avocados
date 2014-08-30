#!/usr/bin/env python3
"""
Avocados and stuff
"""

import os, random
import pygame
import avocado, lawyer
from pygame.locals import *
from support.colors import *
from interface import hud

def initialize_screen():
    displayInfo = pygame.display.Info()
    zoom = 1.3

    WIDTH = int(displayInfo.current_w / zoom)
    HEIGHT = int(displayInfo.current_h / zoom)
    return (WIDTH, HEIGHT)


def main():
    pygame.init()
    pygame.display.set_caption('Pin the Avocados!')
    clock = pygame.time.Clock()

    # initialize_screen() won't work for dualscreen
    #size = initialize_screen()
    size = (800, 600)
    bg = BLACK
    desired_fps = 60
    font = pygame.font.Font(None, 40)

    # I don't know, should we move this text out of the way?
    game_over = font.render('GAME OVER', 0, RED)

    # initialize the game canvas
    screen = pygame.display.set_mode(size)

    # initialize the HUD class
    my_hud = hud.Hud(size)

    # initialize our lawyer
    fullegast = lawyer.Lawyer(screen)

    score = 0
    time = 15
    level = 5

    running = True
    timeleft = time
    avocados = []
    while running:
        time_passed = clock.tick(desired_fps)
        fps = clock.get_fps()
        screen.fill(bg)

        # Let's add the lawyer
        fullegast.blitme()

        timeleft -= time_passed / 1000
        timeleft = round(timeleft, 2)

        if timeleft <= 0:
            screen_width, screen_height = size
            screen.blit(game_over, (screen_width/3, screen_height/2))
            displaytime = 'Timed out!'
        else:
            displaytime = timeleft

        # Redraw the HUD
        chud = my_hud.draw_hud(score, displaytime, round(fps, 2))
        screen.blit(chud, (10, 10))

        # Initialize a number of avocados, depending on the level
        if len(avocados) != level:
            avocados = []
            for i in range(0, level):
                a = avocado.Avocado(size)
                avocados.append(a)

        for a in avocados:
            if not a.move():
                a.reset()
            screen.blit(a.image, a.pycard)

        # Catch events
        for event in pygame.event.get():
            # Collision detection
            if event.type == MOUSEBUTTONDOWN:
                for avo in avocados:
                    if avo.collides(pygame.mouse.get_pos()):
                        score += 100

            # Had enough of this?
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()


if __name__ == '__main__':
    main()
