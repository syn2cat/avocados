#!/usr/bin/env python3
"""
Avocados and stuff
"""

import os, random, sys
import pygame
import avocado, crystal, pingenerator
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
        self.bg.set_colorkey((255,255,255))
        self.bg.set_alpha(75)

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
        # Never set below 4, else we have a high
        # probability of losing the game due to a missing color
        # Alternatively, you could edit chooseRandomColor()
        # to only work on the first multiplier colors
        multiplier = 4
        time = timeleft = 30
        level = 1
        levelChange = 0
        score = 0
        targetScore = 400

        # We could use this list for redrawing only this part
        # of the screen install of all of it
        pinnedAvocados = []
        movingAvocados = []
        thrownPins = []

        # initialize the HUD class and the lawyer
        the_hud = hud.Hud(self.screen)
        crystalBall = crystal.Crystal(self.screen)

        # Initial color indication
        color = self.chooseRandomColor()
        crystalBall.setColor(color)

        running = True
        while running:
            time_passed = clock.tick(desired_fps)
            fps = clock.get_fps()
            screen_width, screen_height = self.size

            # Redraw the background and put our lawyer back on top
            self.drawBackground()
            crystalBall.blitme()

            # Next level?
            if score >= (targetScore * level):
                level += 1
                levelChange = 70
                timeleft = time
                print('DEBUG :: Score: ' + str(score))
                print('DEBUG :: Level ' + str(level))
                self.playLevel(level)
                pinnedAvocados = []
                movingAvocados = []
                thrownPins = []

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

            # If we're not currently in between levels…
            if levelChange == 0:
                # Initialize a number of avocados, depending on the level
                avocadosInGame = len(movingAvocados)
                avocadosWanted = level * multiplier
                if avocadosInGame < avocadosWanted:
                    probability = int(1.0/(avocadosWanted - avocadosInGame) * 100)
                    if random.randint(0, probability) < 3:
                        avocolor = self.chooseRandomColor()
                        avosize = (50, 50)   # should we randomize this?
                        a = avocado.Avocado(self.screen, avocolor, avosize, color, level)
                        movingAvocados.append(a)

                # Remove avocados from the list of moving avocados if they no longer move
                # Or add them to the list of pinned avocados if they're been hit
                pinnedAvocados += [avo for avo in movingAvocados if avo.isPinned() ]
                movingAvocados[:] = [ avo for avo in movingAvocados if avo.isFalling() ]

                ##############################
                #
                # Late-Night-Comments:
                #
                # Can we maybe handle the pinned avocados the same way I handle "stuck"
                # pins? It seems to be easier.. well, the pins don't fall out of the screen
                # though…
                #
                ##############################

                # Now redraw our avocados
                for a in movingAvocados:
                    a.setTargetColor(color)
                    a.move()
                    a.blitme()

                for a in pinnedAvocados:
                    a.blitme()

                # And finally check if we need to redraw any pins
                for activePin in thrownPins:
                    activePin.blitme()
                    if not activePin.isStuck():
                        activePin.moveTowardsTarget()

            # Catch events
            for event in pygame.event.get():
                # Collision detection
                if event.type == MOUSEBUTTONDOWN:
                    mousepos = pygame.mouse.get_pos()

                    # Throw a pin here
                    newPin = pingenerator.Generate(self.screen)
                    newPin.throwAt(mousepos)
                    thrownPins.append(newPin)

                    # Check if any avocados have been hit
                    for avo in movingAvocados:
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
                elif event.type == pygame.KEYDOWN:
                    if pygame.key.get_pressed()[pygame.K_f] != 0:
                        print("Toggling full screen, in the Future")
                elif (pygame.key.get_pressed()[pygame.K_q] != 0) or (pygame.key.get_pressed()[pygame.K_ESCAPE] != 0):
                    running = False
                    game.gameOver()
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()


if __name__ == '__main__':
    game = TheGame()
    game.playLevel()
    game.main()
