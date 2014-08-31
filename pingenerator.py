#!/usr/bin/env python3

import os, pygame

class Generate:

    def __init__(self, screen):
        self.inFlight = False
        self.vx = 40
        self.vy = 40

        self.screen = screen
        screen_width, screen_height = screen.get_size()
        self.pos = (screen_width / 2, screen_height)
        self.image = pygame.image.load(os.path.join('img','pin.png')).convert_alpha()


    def throwAt(self, target):
        self.inFlight = True
        self.target = target


    def isStuck(self):
        if self.pos == self.target:
            print('Pin stuck!')
            return True


    def blitme(self):
        self.screen.blit(self.image, self.pos)


    def moveTowardsTarget(self):
        # OK, this works, but honestly,
        # it would probably be much more effective
        # to just be more lenient on isStuck
        # e.g. accept approximate positions.
        x, y = self.pos
        tx, ty = self.target
        xToCover = tx - x;
        yToCover = ty - y;

        # Please someone turn this into python  ;)
        if abs(xToCover) < self.vx:
            self.vx = self.vx/2

        if abs(yToCover) < self.vy:
            self.vy = self.vy/2

        if xToCover < 0:
            xstep = -1 * self.vx
        elif xToCover == 0:
            xstep = 0
        else:
            xstep = 1* self.vx

        newx = x + xstep

        if yToCover < 0:
            ystep = -1 * self.vy # = d * v (direction * speed)
        elif yToCover == 0:
            ystep = 0
        else:
            ystep = 1 * self.vy

        newy = y + ystep

        print('DEBUG :: pin target: ' + str(tx) + ',' + str(ty))
        print('DEBUG :: pin position: ' + str(newx) + ',' + str(newy))
        print('DEBUG :: pin distance: ' + str(xToCover) + ',' + str(yToCover))
        print('DEBUG :: pin speed: ' + str(self.vx) + ',' + str(self.vy))
        print('')
        self.pos = (newx, newy)
