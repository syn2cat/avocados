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

        self.WIDTH, self.HEIGHT = 800, 600

        # initialize the game canvas
        self.size = (self.WIDTH, self.HEIGHT)
        self.screen = pygame.display.set_mode(self.size)
        self.colors = [BLUE, GREEN, RED, YELLOW]
        self.bg = pygame.image.load(os.path.join('img', 'lawyerCrystalBall.png'))

        # fonts
        self.bigFont = pygame.font.Font(None, 90)

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


    def fadeSound(self, sound=True):
        if not sound:
            return
        pygame.mixer.music.fadeout(3000)

    def chooseRandomColor(self):
        selected = random.randint(0, 3)
        return self.colors[selected]


    def gameOver(self):
        screen_width, screen_height = self.size
        gameOverImage = pygame.image.load("img/gameOver.png")
        gameOverText = self.bigFont.render('GAME OVER', 0, YELLOW)
        gameOverImage.blit(gameOverText, (screen_width/8, screen_height/7))
        self.screen.blit(pygame.transform.scale(gameOverImage, self.size), (0, 0))
        pygame.display.flip()
        self.fadeSound()
        pygame.time.wait(3000)
        pygame.quit()
        sys.exit()


    def keepPinned(self, avocado):
        self.pinned.append(avocado)


    def drawBackground(self):
        if type(self.bg) is tuple:
            self.screen.fill(self.bg)
        else:
            self.screen.blit(pygame.transform.scale(self.bg, self.size), (0, 0))


    def main(self):
        clock = pygame.time.Clock()
        desired_fps = 60
        multiplier = 3
        time = timeleft = 30
        level = 1
        levelChange = 0
        score = 0
        targetScore = 400

        # initialize the HUD class and the lawyer
        the_hud = hud.Hud(self.screen)
        crystalBall = crystal.Crystal(self.screen)

        # Initial color indication
        color = self.chooseRandomColor()

        # We could use this list for redrawing only this part
        # of the screen install of all of it
        avocados = []
        running = True

        while running:
            time_passed = clock.tick(desired_fps)
            fps = clock.get_fps()
            screen_width, screen_height = self.size

            # Redraw the background and put our lawyer back on top
            self.drawBackground()

            # Next level?
            if score >= targetScore:
                self.score = 0
                level += 1
                levelChange = 35
                timeleft = time
                avocados = []
                print('DEBUG :: Level ' + str(level))
                self.playLevel(level)

            if levelChange > 0:
                levelText = self.bigFont.render('Level ' + str(level), 0, WHITE)
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

            # If we're not currently in between levels…
            if levelChange == 0:
                # Initialize a number of avocados, depending on the level
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
                avocados[:] = [ x for x in avocados if x.exists() ]
                for a in avocados:
                    a.setTargetColor(color)
                    if not a.isPinned():
                        a.move()
                    a.blitme()

            # Catch events
            for event in pygame.event.get():
                # Collision detection
                if event.type == MOUSEBUTTONDOWN:
                    mousepos = pygame.mouse.get_pos()
                    # Throw a pin here
                    # pin.throwAt(mousepos)
                    # Yep, above here
                    for avo in avocados:
                        hit = avo.isHit(mousepos)
                        if hit:
                            score += 100
                            color = self.chooseRandomColor()
                            crystalBall.setColor(color)
                        elif hit == False:
                            score -= 50

                # Had enough of this?
                if event.type == pygame.QUIT:
                    running = False
                    game.gameOver()
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()


if __name__ == '__main__':
    game = TheGame()
    game.playLevel()
    game.main()
