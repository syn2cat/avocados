#!/usr/bin/env python3

import pygame
from pygame.locals import *
from support.colors import *

def draw_hud(score, timeleft, fps):
    hud = pygame.Surface((800, 100))
    font = pygame.font.Font(None, 30)

    # Adding items to the hud
    hud.blit(draw_score(font, score), (0, 0))
    hud.blit(draw_timeleft(font, timeleft), (100, 0))
    hud.blit(draw_fps(font, fps), (150, 0))
    return hud

def draw_score(font, score):
    score = font.render('Score: ' + str(score), 0, WHITE)
    return score

def draw_timeleft(font, time):
    # Add a clock icon here (maybe egg-clock)
    time = font.render(str(time), 1, WHITE)
    return time

def draw_fps(font, fps):
    return font.render('fps: ' + str(fps), 10, RED)
