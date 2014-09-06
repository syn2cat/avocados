#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

import sys
from colors import *
from screen import *


def main():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
    pygame.display.update()

if __name__ == "__main__": main()
