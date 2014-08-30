#!/usr/bin/env python3
import sys, time
from colors import *
from screen import *

def main():
    ck = (127, 33, 33)
    size = 25
    while True:
        time.sleep(0.5)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEMOTION:
                s = pygame.Surface((50,50))
                # first, "erase" the surface by filling it with a color and
                # setting this color as colorkey, so the surface is empty
                s.fill(ck)
                s.set_colorkey(ck)

                pygame.draw.circle(s, (RED), (size, size), size, 4)
                # after drawing the circle, we can set the
                # alpha value (transparency) of the surface
                s.set_alpha(75)

                x, y = pygame.mouse.get_pos()
                screen.blit(s, (x-size, y-size))
            pygame.event.poll()
            pygame.display.flip()
    pygame.display.update()

if __name__ == "__main__": main()
