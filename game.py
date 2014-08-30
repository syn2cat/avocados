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
    try:
        pygame.mixer.init()
        pygame.mixer.music.set_volume(0.5)
        noSound = False
    except:
        print("Setting no sound :(")
        noSound = True

    pygame.display.set_caption('Pin Avo, the Cado!')
    clock = pygame.time.Clock()

    # initialize_screen() won't work for dualscreen
    #size = initialize_screen()
    size = (800, 600)
    bg = pygame.image.load("img/background.png")
    desired_fps = 10
    font = pygame.font.Font(None, 40)

    # I don't know, should we move this text out of the way?
    game_over = font.render('GAME OVER', 0, RED)

    # initialize the game canvas
    screen = pygame.display.set_mode(size)

    # initialize the HUD class and the lawyer
    the_hud = hud.Hud(screen)
    fullegast = lawyer.Lawyer(screen)

    # Well, we want this to select between several colors, so we need a list
    # of colors, right?
    colors = [BLUE, GREEN, RED, YELLOW]
    selected = random.randint(0, 3)
    color = colors[selected]

    score = 0
    time = 15
    level = 5

    running = True
    timeleft = time
    avocados = []
    while running:
        time_passed = clock.tick(desired_fps)
        fps = clock.get_fps()
        if type(bg) is tuple:
            screen.fill(bg)
        else:
            screen.blit(pygame.transform.scale(bg,(800,600)),(0,0))


        # Let's add the lawyer and have him announce a color
        fullegast.setColor(color)
        fullegast.blitme()

        timeleft -= time_passed / 1000
        timeleft = round(timeleft, 2)


        if timeleft <= 0:
            screen_width, screen_height = size
            screen.blit(game_over, (screen_width/3, screen_height/2))
            displaytime = 'Timed out!'
            pygame.display.flip()
            continue
        else:
            displaytime = timeleft

        # Redraw the HUD
        the_hud.draw_hud(score, displaytime, round(fps, 2))

        # Initialize a number of avocados, depending on the level
        avocados_in_game = len(avocados)
        print(avocados_in_game)
        if avocados_in_game != level:
            for i in range(avocados_in_game, level):
                avocolor = colors[random.randint(0, 3)]
                avosize = (50, 50)   # should we randomize this?
                a = avocado.Avocado(screen, avocolor, avosize, color, noSound)
                avocados.append(a)

        avocados[:] = [ x for x in avocados if x.exists() ]
        for a in avocados:
            a.move()
            a.blitme()

        # Catch events
        for event in pygame.event.get():
            # Collision detection
            if event.type == MOUSEBUTTONDOWN:
                for avo in avocados:
                    if avo.collides(pygame.mouse.get_pos()):
                        score += 100
                        avo.init_pos()
            # Had enough of this?
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()


if __name__ == '__main__':
    main()
