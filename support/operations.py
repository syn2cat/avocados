#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

import pygame

def color_surface(surface, color):
    red, green, blue = color
    arr = pygame.surfarray.pixels3d(surface)
    arr[:,:,0] = red
    arr[:,:,1] = green
    arr[:,:,2] = blue
