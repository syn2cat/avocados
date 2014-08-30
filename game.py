#!/usr/bin/env python3
"""
Avocados and stuff
"""

import os, random, sys
import pygame
import avocado, crystal
from pygame.locals import *
from support.colors import *
from interface import hud


class TheGame:

    def __init__(self):
        """ Initialize the game """
        pygame.init()
        pygame.display.set_caption('Pin Avo, the Cado!')

        displayInfo = pygame.display.Info()
        self.resize = 1.3

        self.WIDTH = int(displayInfo.current_w / self.resize)
        self.HEIGHT = int(displayInfo.current_h / self.resize)

        # initialize the game canvas
        self.size = (self.WIDTH, self.HEIGHT)
        self.screen = pygame.display.set_mode(self.size)
        self.colors = [BLUE, GREEN, RED, YELLOW]

        # fonts
        self.big = pygame.font.Font(None, 90)

        self.pinned = []

        # Set splashscreen
        splashScreen = pygame.image.load("img/splashScreen.png")
        self.screen.blit(pygame.transform.scale(splashScreen, self.size), (0, 0))
        pygame.display.flip()
        pygame.time.wait(3000)

        try:
            pygame.mixer.init()
            pygame.mixer.music.set_volume(0.5)
            sound = True
        except:
            print("Y U NO sound? :(")
            sound = False


    def mute(self,mute=False, sound=True):
        if not sound:
            return
        if mute:
            pygame.mixer.music.set_volume(0.0)
        else:
            pygame.mixer.music.set_volume(0.5)


    def playLevel(self,lvl=1,sound=True):
        if not sound:
            return
        if lvl == 1:
            pygame.mixer.music.load("""audio/level1.wav""")
        elif lvl == 2:
            pygame.mixer.music.load("""audio/level2.wav""")
        elif lvl >= 3:
            pygame.mixer.music.load("""audio/level3.wav""")
        pygame.mixer.music.play()


    def fade(self, sound=True):
        if not sound:
            return
        pygame.mixer.music.fadeout(3000)


    def loadClick(self, sound=True):
        if not sound:
            return
        self.click = pygame.mixer.Sound("audio/click.wav")
        return self.click


    def gameOver(self):
        screen_width, screen_height = self.size
        gameOverImage = pygame.image.load("img/gameOver.png")
        gameOverText = self.big.render('GAME OVER', 0, YELLOW)
        gameOverImage.blit(gameOverText, (screen_width/8, screen_height/6))
        self.screen.blit(pygame.transform.scale(gameOverImage, self.size), (0, 0))
        pygame.display.flip()
        self.fade()
        pygame.time.wait(3000)
        pygame.quit()
        sys.exit()


    def keepPinned(self, avocado):
        self.pinned.append(avocado)


    def main(self):
        clock = pygame.time.Clock()
        bg = pygame.image.load("img/lawyerCrystalBall.png")
        desired_fps = 60
        multiplier = 3
        score = 0
        time = timeleft = 30
        level = 1
        levelChange = 0
        reachScore = 200
        avoClick = self.loadClick()

        # initialize the HUD class and the lawyers crystal ball
        the_hud = hud.Hud(self.screen)
        crystalBall = crystal.Crystal(self.screen)

        # Initial color indication
        color = self.chooseRandomColor()

        avocados = []   # We could use this for redrawing only this part
        running = True

        while running:
            time_passed = clock.tick(desired_fps)
            fps = clock.get_fps()
            screen_width, screen_height = self.size

            if type(bg) is tuple:
                self.screen.fill(bg)
            else:
                self.screen.blit(pygame.transform.scale(bg, self.size), (0, 0))

            # Next level?
            if score >= reachScore:
                score = 0
                level += 1
                levelChange = 35
                timeleft = time
                avocados = []
                self.pinned = []
                print('DEBUG :: Level ' + str(level))
                game.playLevel(level)

            if levelChange > 0:
                levelText = self.big.render('Level ' + str(level), 0, WHITE)
                self.screen.blit(levelText, (screen_width / 3, screen_height / 2))
                levelChange -= 1

            timeleft -= time_passed / 1000
            timeleft = round(timeleft, 2)
            if timeleft <= 0:
                self.gameOver()
            else:
                displaytime = timeleft

            # Redraw the HUD
            the_hud.draw_hud(score, displaytime, round(fps, 2))
            crystalBall.setColor(color)

            # Initialize a number of avocados, depending on the level
            if levelChange == 0:
                avocados_in_game = len(avocados)
                avocadosWanted = level * multiplier
                if avocados_in_game < avocadosWanted:
                    for i in range(avocados_in_game, avocadosWanted):
                        avocolor = self.chooseRandomColor()
                        avosize = (50, 50)   # should we randomize this?
                        a = avocado.Avocado(self.screen, avocolor, avosize, color)
                        avocados.append(a)

                # Remove avocados from the list if they no longer exist
                # E.g. have been pinned or fallen down
                self.pinned += [avo for avo in avocados if avo.has_been_pinned]
                avocados[:] = [ x for x in avocados if x.exists() ]
                for a in avocados:
                    a.setTargetColor(color)
                    a.move()
                    a.blitme()
                for a in self.pinned:
                    a.blitme()

            # Catch events
            for event in pygame.event.get():
                # Collision detection
                if event.type == MOUSEBUTTONDOWN:
                    avoClick.play()
                    for avo in avocados:
                        hit = avo.isHit(pygame.mouse.get_pos())
                        if hit:
                            score += 100
                            color = self.chooseRandomColor()
                            crystalBall.setColor(color)
                        elif hit == False:
                            score -= 50

                # Had enough of this?
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()


    def chooseRandomColor(self):
        selected = random.randint(0, 3)
        return self.colors[selected]


if __name__ == '__main__':
    game = TheGame()
    game.playLevel()
    game.main()
