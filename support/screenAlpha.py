#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

import pygame
from pygame.locals import *

pygame.init()

displayInfo = pygame.display.Info()
zoom = 1.3

WIDTH = int(displayInfo.current_w / zoom)
HEIGHT = int(displayInfo.current_h / zoom)

# this will be the Surface you work on (in the docs referenced as Surface)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screenAlpha = screen.convert_alpha()

pygame.display.set_caption("Pink Unicorns are waiting but what is the HOTkey?!?!?!1111")
