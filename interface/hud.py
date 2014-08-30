#!/usr/bin/env python3

import os, pygame
from pygame.locals import *
from support.colors import *
from support import operations

class Hud:

    def __init__(self, screen):
        self.screen = screen
        self.screen_width, self.screen_height = screen.get_size()
        self.font = pygame.font.Font(None, 30)
        self.hud = pygame.Surface((self.screen_width, 30))

    def draw_hud(self, score, timeleft, fps):
        self.hud.fill(BLACK)
        self.hud.blit(self.draw_score(score), (0, 0))
        self.hud.blit(self.draw_timeleft(timeleft), (self.screen_width / 2, 0))
        thefps = self.draw_fps(fps)
        fps_rect = thefps.get_rect()
        self.hud.blit(thefps, (self.screen_width - fps_rect.w, 0))
        self.blitme()

    def draw_score(self, score):
        score = self.font.render('Score: ' + str(score), 0, WHITE)
        return score

    def draw_timeleft(self, time):
        # Not sure this is clever, to recreate the surface each time ;)
        timesurface = pygame.Surface((200, 20))
        hourglass = pygame.image.load(os.path.join('img', 'hourglass.png')).convert_alpha()
        hourglass = pygame.transform.scale(hourglass, (15, 18))
        operations.color_surface(hourglass, WHITE)
        time = self.font.render(str(time), 1, WHITE)
        timesurface.blit(hourglass, (0, 0))
        timesurface.blit(time, (40, 0))
        return timesurface

    def draw_fps(self, fps):
        return self.font.render('fps: ' + str(fps), 10, RED)

    def blitme(self):
        self.screen.blit(self.hud, (10, 10))
