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


class TheGame:

    def __init__(self):
        """ foo """
        self.colors = [BLUE, GREEN, RED, YELLOW]


    def initialize_screen(self):
        displayInfo = pygame.display.Info()
        zoom = 1.3
        WIDTH = int(displayInfo.current_w / zoom)
        HEIGHT = int(displayInfo.current_h / zoom)
        return (WIDTH, HEIGHT)


    def main(self):
        pygame.init()
        try:
            pygame.mixer.init()
            pygame.mixer.music.set_volume(0.5)
            noSound = False
        except:
            print("Y U NO sound? :(")
            noSound = True

        pygame.display.set_caption('Pin Avo, the Cado!')
        clock = pygame.time.Clock()

        # initialize_screen() won't work for dualscreen
        #size = initialize_screen()
        size = (800, 600)
        bg = pygame.image.load("img/background.png")
        desired_fps = 15
        multiplier = 6
        score = 0
        time = timeleft = 30
        level = 1
        font = pygame.font.Font(None, 40)

        # I don't know, should we move this text out of the way?
        game_over = font.render('GAME OVER', 0, RED)

        # initialize the game canvas
        screen = pygame.display.set_mode(size)

        # initialize the HUD class and the lawyer
        the_hud = hud.Hud(screen)
        fullegast = lawyer.Lawyer(screen)

        # Initial color
        color = self.chooseRandomColor()
        fullegast.setColor(color)

        avocados = []
        running = True
        while running:

            time_passed = clock.tick(desired_fps)
            fps = clock.get_fps()

            if type(bg) is tuple:
                screen.fill(bg)
            else:
                screen.blit(pygame.transform.scale(bg, (800, 600)), (0, 0))

            # Next level?
            if score >= 500:
                score = 0
                level += 1
                print('DEBUG :: Level ' + string(level))

            # Let's add the lawyer
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
            avocadosWanted = level * multiplier
            if avocados_in_game < avocadosWanted:
                for i in range(avocados_in_game, avocadosWanted):
                    avocolor = self.chooseRandomColor()
                    avosize = (50, 50)   # should we randomize this?
                    a = avocado.Avocado(screen, avocolor, avosize, color, noSound)
                    avocados.append(a)

            # Remove avocados from the list if they no longer exist
            # E.g. have been pinned or fallen down
            avocados[:] = [ x for x in avocados if x.exists() ]
            for a in avocados:
                a.updateTargetColor(color)
                a.move()
                a.blitme()

            # Catch events
            for event in pygame.event.get():
                # Collision detection
                if event.type == MOUSEBUTTONDOWN:
                    for avo in avocados:
                        hit = avo.isHit(pygame.mouse.get_pos())
                        if hit:
                            score += 100
                            color = self.chooseRandomColor()
                            fullegast.setColor(color)
                        elif hit == False:
                            score -= 50

                # Had enough of this?
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.flip()


    def chooseRandomColor(self):
        selected = random.randint(0, 3)
        return self.colors[selected]


if __name__ == '__main__':
    game = TheGame()
    game.main()
