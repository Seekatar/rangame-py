import pygame, sys, math, random
import time
from pygame.locals import *


class HistogramCounts:

    def __init__(self):
        self.reset()

    def reset(self):
        self.counts = []
        
    def set_value(self,i,value):
        self.ensure(i)
        self.counts[i] = value

    def inc_value(self,i,inc=1):
        self.ensure(i)
        self.counts[i] += inc

    def ensure(self,i):
        while (len(self.counts) < i ):
            self.counts.append(0)


COLORS = [( 255,   0,   0,  128 ),
          (   0, 255,   0,  128 ),
          (   0,   0, 255,  128 ),
          ( 255,   0, 255,  128 ),
          (   0, 255, 255,  128 ),
          ( 255, 255, 255,  128 ),
          ( 255, 255,   0,  128 )
          ]

class Histogram:

    def __init__(self,parent):
        self.parent = parent
        self.surface = parent.convert_alpha()
        pygame.draw.rect(self.surface, (255,0,0,128), (0,10,100,30))
        self.parent.blit(self.surface,(0,0))

    def show(self,counts,count):

        width = self.surface.get_width()*.90 # width of histo 90%
        maxValue = 0
        for i in counts:
            if i > maxValue:
                maxValue = i
        
        colorIndex = 0
        row = 0
        for i in counts:
            r = pygame.draw.rect(self.surface, COLORS[colorIndex], (0, 20+(row*25), (width*i)/maxValue, 20))

            row += 1
            if row >= count:
                break

            colorIndex += 1
            if colorIndex >= len(COLORS):
                colorIndex = 0
                

        self.parent.blit(self.surface,(0,0))
