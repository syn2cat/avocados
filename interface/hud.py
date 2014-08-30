#!/usr/bin/env python3

import pygame
from pygame.locals import *
from support.colors import *

class Hud:

    def __init__(self, screensize):
        self.screen_width, self.screen_height = screensize
        self.font = pygame.font.Font(None, 30)
        self.screen = pygame.Surface((self.screen_width, self.screen_height / 6))

    def draw_hud(self, score, timeleft, fps):
        self.screen.fill(BLACK)
        self.screen.blit(self.draw_score(score), (0, 0))
        self.screen.blit(self.draw_timeleft(timeleft), (100, 0))
        self.screen.blit(self.draw_fps(fps), (650, 0))
        return self.screen

    def draw_score(self, score):
        score = self.font.render('Score: ' + str(score), 0, WHITE)
        return score

    def draw_timeleft(self, time):
        # Add a clock icon here (maybe egg-clock)
        time = self.font.render(str(time), 1, WHITE)
        return time

    def draw_fps(self, fps):
        return self.font.render('fps: ' + str(fps), 10, RED)
