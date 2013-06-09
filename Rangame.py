import pygame, sys, math, random
import time
from pygame.locals import *
from SettingsDlg import SettingsDlg, Settings
from HelpDlg import HelpDlg

from Histogram import Histogram

PINK = (255,0,255)

class Plotter:

    def __init__(self,surface):
        self.surface = surface
        self.plotview = None

    def PlotPoint(self,x,y,color):
        pygame.draw.line(self.surface,color,(x,y),(x,y))

    def DrawX(self,x,y):
        pygame.draw.line(self.surface,PINK,(x-3,y-3),(x+3,y+3))
        pygame.draw.line(self.surface,PINK,(x+3,y-3),(x-3,y+3))

    def DrawStar(self,x,y):
        self.DrawX(x,y)
        pygame.draw.line(self.surface,PINK,(x-3,y),(x+3,y))
        #pygame.draw.line(self.surface,PINK,(x,y-3),(x,y+3))

    def SaveCurrent(self):
        self.plotview = self.surface.convert()

    def ResetLast(self,background,wiping):
        self.surface.fill( Settings.ColorAsTuple( background ))
        if wiping and self.plotview != None:
           self.plotview.fill( Settings.ColorAsTuple( background))

    def ShowLast(self):
        if self.plotview != None:
            self.surface.blit(self.plotview,(0,0))
        

class PlotPoint:

    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

class Rangame:

    def __init__(self,width,height,plotter,settings):
        self.plotter = plotter
        self.width = width
        self.height = height
        self._counts = [0]
        self._counts *= 31
        self.points = []
        self.totalPoints = 0
        self.histo = Histogram(plotter.surface,2)
        self.showingHisto = False

        for i in range(21):
            self.points.append(PlotPoint())

        self.settings = settings

    def PlotAgain(self):
        self.totalPoints = 0

    def AddPoint(self,x,y):
        self.points.append(PlotPoint(x,y))
        if self.settings.UseMarkers:
            self.plotter.DrawX(x,y)
        if len(self.points) >= self.settings.Sides:
            pygame.mouse.set_cursor(*pygame.cursors.arrow)
            self.PlotAgain()

    def InitPoints(self):

        self.points = []

        if not self.settings.UseRegular:
            pygame.mouse.set_cursor(*pygame.cursors.broken_x)
            self.totalPoints = sys.maxint
            return

        for i in range(self.settings.Sides):
            self.points.append(PlotPoint())


        origin = PlotPoint( self.width/2, self.height/2 )

        aspect = 1.0

        # top point
        dg = 0.0
        incdg = 0.0        # degree, increment
        i = 0
        j = 0
        k = 0
        l = 0

        # clear memory for histogram
        for i in range(self.settings.Sides):
            self._counts[i] = 0

        incdg = (math.pi/self.settings.Sides*2.0)
        dg = -.5*math.pi + incdg

        # set first point
        self.points[0].y = origin.y - (int)(self.settings.Radius*aspect)

        # does this put that corner off screen?
        if self.points[0].y < 0:
        
            # reset origin
            origin.y = origin.y - self.points[0].y

            # set point on screen
            self.points[0].x = 5
        
        self.points[0].x = origin.x

        j = 1
        while (dg <= 0.5*math.pi+0.001):
        
            if (dg < math.pi/2):
            
                k = self.settings.Radius*math.cos(dg)*aspect+0.5
                l = self.settings.Radius*math.sin(dg)+0.5
                self.points[j].x = origin.x + k
                self.points[j].y = origin.y + l

                # symetrical point, too
                self.points[self.settings.Sides-j].x = origin.x - k
                self.points[self.settings.Sides-j].y = origin.y + l
            
            else:
            
                # even numbered figure, this is point opposite first
                self.points[j].x = origin.x
                self.points[j].y = origin.y + (int)(self.settings.Radius*aspect)
            
            j += 1
            dg += incdg

        if self.settings.UseMarkers and self.totalPoints == 0:
            for i in range(self.settings.Sides):
                self.plotter.DrawX(self.points[i].x,self.points[i].y)

    def Plot(self,points):
        
        if self.totalPoints > self.settings.PointsK*1000:
            if self.totalPoints != sys.maxint:
                self.totalPoints = sys.maxint
                self.plotter.SaveCurrent()
                if self.settings.ShowHisto:
                    self.histo.show(self._counts,self.settings.Sides)        
                self.showingHisto = self.settings.ShowHisto
            return 

        if self.totalPoints == 0:
            self.plotter.ShowLast()
            if self.settings.UseRegular:
                self.InitPoints()

        self._canceled = False

        random.seed(time.clock())
        x = random.randrange(self.width)
        y = random.randrange(self.height)

        for j in range(self.settings.Sides):
            self._counts[j] = 0

        if self.settings.UseMarkers and self.totalPoints == 0:
            self.plotter.DrawStar( x, y ) # starting point

        # rest of them
        color = Settings.ColorAsTuple(self.settings.Foreground)

        for self._plotCount in range(points): #self.settings.PointsK*1000:
            if self._canceled:
                break

            nextPt = random.randrange(self.settings.Sides)
            x += (int)((self.points[nextPt].x-x)/self.settings.Divisor)
            y += (int)((self.points[nextPt].y-y)/self.settings.Divisor)
            self.plotter.PlotPoint(x,y,color)
            self._counts[nextPt]+=1

        self.totalPoints += points

    def Wipe(self):
        self.plotter.ResetLast(self.settings.Background, True )

    def ToggleHisto(self):
        if self.showingHisto:
            self.plotter.ResetLast(self.settings.Background, False )
            self.plotter.ShowLast()
            self.showingHisto = False
        else:
            self.histo.show(self._counts,self.settings.Sides)
            self.showingHisto = True

def main():
    pygame.init()
    WIDTH = 800
    HEIGHT = 800
    surface = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("RangamePy")

    settings = Settings()
    settings.LoadValues()
    surface.fill( Settings.ColorAsTuple( settings.Background ))
   
    plotter = Plotter( surface )
    rg = Rangame(WIDTH,HEIGHT,plotter,settings)
    rg.InitPoints()

    FPS = 30
    fpsClock = pygame.time.Clock()

    Histogram(surface,1)
    while True:
        mousex = None

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONUP:
                mousex,mousey = event.pos
                rg.AddPoint(mousex,mousey)
            elif event.type == KEYUP:
                if event.key == K_c:
                    if SettingsDlg.DoModal(settings):
                        settings.SaveValues()
                elif event.key == K_p or event.key == K_SPACE:
                    rg.PlotAgain()
                elif event.key == K_r:
                    rg.InitPoints()
                elif event.key == K_h:
                    rg.ToggleHisto()
                elif event.key == K_w:
                    rg.Wipe()
                    print "Forground is ", settings.Foreground
                elif event.key == K_F1:
                    # TODO HelpDlg().DoModal()
                    pass

        rg.Plot(100)

        pygame.display.update()

        fpsClock.tick(FPS)

if __name__ == "__main__":
    main()