#!/usr/bin/env python3

# Move a single pixel around the screen without crashing against the borders.
# (and exit the program once crashed)

import sys
from colors import *
from screen import *

def main():
    # Position of the pixel.
    x = WIDTH / 2
    y = HEIGHT / 2

    # Direction of the pixel.
    dir_x = 0
    dir_y = -1

    clock = pygame.time.Clock()
    running = True

    while running:
        x += dir_x
        y += dir_y

        if x <= 0 or x >= WIDTH or y <= 0 or y >= HEIGHT:
            print("Crash!")
            running = False

        screen.fill(BLACK)
        screen.set_at((int(x), int(y)), WHITE)

        for event in pygame.event.get():
           if event.type == pygame.QUIT:
                running = False
           elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    dir_x = 0
                    dir_y = -1
                elif event.key == pygame.K_DOWN:
                    dir_x = 0
                    dir_y = 1
                elif event.key == pygame.K_LEFT:
                    dir_x = -1
                    dir_y = 0
                elif event.key == pygame.K_RIGHT:
                    dir_x = 1
                    dir_y = 0

        pygame.display.flip()
        clock.tick(120)

if __name__ == "__main__": main()
