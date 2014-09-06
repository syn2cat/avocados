#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

import urllib.request, sys, shutil, os
from colors import *
from screenAlpha import *

file_name = 'mlp.png'

def main():
    try:
        os.path.isfile(file_name)
        print("Howdy you already got the file! Good.")
    except:
        MLP = "http://localhost.lu/MLP.png"
        with urllib.request.urlopen(MLP) as response, open(file_name, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)

    MLPcolor = (255,192,192,128)

    image = pygame.image.load(file_name)
    image = pygame.transform.scale(image, (200, 200))
    image.set_colorkey((255,255,255))
    alpha = 75
    image.set_alpha(alpha)
    screen.fill(MLPcolor)
    screen.blit(image, (0,0))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
           if event.type == QUIT:
                pygame.quit()
                sys.exit()
           elif event.type == KEYDOWN:
                if event.key == K_UP:
                    alpha += 1
                    image.set_alpha(alpha)
                    print("Alpha wants to be: {}".format(alpha))
                elif event.key == K_DOWN:
                    alpha -= 1
                    image.set_alpha(alpha)
                    print("Alpha wants to be: {}".format(alpha))
                elif event.key == K_LEFT:
                    dir_x = -1
                    dir_y = 0
                elif event.key == K_RIGHT:
                    dir_x = 1
                    dir_y = 0
                elif event.key == K_q:
                    pygame.quit()
                    sys.exit()
    pygame.display.update()

if __name__ == "__main__": main()

