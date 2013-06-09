import pygame, sys, math, random
import time
from pygame.locals import *

RED = ( 255,   0,   0,  128 )
COLORS = [( 255,   0,   0,  128 ),
          (   0, 255,   0,  128 ),
          (   0,   0, 255,  128 ),
          ( 255,   0, 255,  128 ),
          (   0, 255, 255,  128 ),
          ( 255, 255, 255,  128 ),
          ( 255, 255,   0,  128 )
          ]

class Histogram:

    def __init__(self,parent,num):
        self.parent = parent
        self.surface = None

    def show(self,counts,count):

        maxValue = 0
        for i in counts:
            if i > maxValue:
                maxValue = i
        
        colorIndex = 0
        row = 0
        
        if ( self.surface != None ):
            self.surface.fill((0,0,0,0))
        
        self.surface = self.parent.convert_alpha()

        width = self.surface.get_width()*.90 # width of histo 90%

        for i in counts:
            r = pygame.draw.rect(self.surface, COLORS[colorIndex], (0, 20+(row*25), (width*i)/maxValue, 20))

            row += 1
            if row >= count:
                break

            colorIndex += 1
            if colorIndex >= len(COLORS):
                colorIndex = 0
                

        self.parent.blit(self.surface,(0,0))
    