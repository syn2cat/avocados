#!/usr/bin/env python3

import pygame
from pygame.locals import *
from support.colors import *

def draw_hud(score):
    hud = pygame.Surface((800, 100))

    # Adding items to the hud
    hud.blit(draw_score(score), (0, 0))
    #hud.blit(get_timeleft, (200, 0))
    return hud

def draw_score(score):
    font = pygame.font.Font(None, 30)
    score = font.render('Score: ' + str(score), 0, WHITE)
    return score
