from Tkinter import *
import tkFileDialog
import tkColorChooser

class Settings(object):

    def __init__(self):
        self.SetDefaults()

    @staticmethod
    def ColorAsTuple(color):
        if (len(color) == 10 ):
            return ( int(color[1:4],16), int(color[4:7],16), int(color[7:10],16) )
        elif (len(color) == 7 ):
            return ( int(color[1:3],16), int(color[3:5],16), int(color[5:7],16) )
        elif (len(color) == 4 ):
            return ( int(color[1:2],16), int(color[2:3],16), int(color[3:4],16) )

    def SetDefaults(self):
        self.Sides = 3
        self.PointsK = 1
        self.Divisor = 2
        self.UseMarkers = True
        self.UseRegular = True
        self.Radius = 100
        self.ShowHisto = False
        self.Background = '#000000'
        self.Foreground = '#0000FF'

    def LoadValues(self):
        import xml.dom.minidom
        import os

        self.SetDefaults()
        
        if ( os.path.exists("RangamePy.xml") ):

            dom = xml.dom.minidom.parse("RangamePy.xml")

            if len(dom.getElementsByTagName('Sides')) > 0 :
                self.Sides = (int(dom.getElementsByTagName('Sides')[0].firstChild.data))
            if len(dom.getElementsByTagName('PointsK')) > 0 :
                self.PointsK = (int(dom.getElementsByTagName('PointsK')[0].firstChild.data))
            if len(dom.getElementsByTagName('Radius')) > 0 :
                self.Radius = (int(dom.getElementsByTagName('Radius')[0].firstChild.data))
            if len(dom.getElementsByTagName('Divisor')) > 0 :
                self.Divisor = (float(dom.getElementsByTagName('Divisor')[0].firstChild.data))
            if len(dom.getElementsByTagName('UseMarkers')) > 0 :
                self.UseMarkers = (int(dom.getElementsByTagName('UseMarkers')[0].firstChild.data) != 0)
            if len(dom.getElementsByTagName('UseRegular')) > 0 :
                self.UseRegular = (int(dom.getElementsByTagName('UseRegular')[0].firstChild.data) != 0)
            if len(dom.getElementsByTagName('ShowHisto')) > 0 :
                self.ShowHisto = (int(dom.getElementsByTagName('ShowHisto')[0].firstChild.data) != 0)
            if len(dom.getElementsByTagName('Foreground')) > 0 :
                self.Foreground = (dom.getElementsByTagName('Foreground')[0].firstChild.data)
            if len(dom.getElementsByTagName('Background')) > 0 :
                self.Background= (dom.getElementsByTagName('Background')[0].firstChild.data)

    def SaveValues(self):
        xml = """<RangamePy>
            <Sides>%d</Sides>
            <PointsK>%d</PointsK>
            <Divisor>%f</Divisor>
            <Radius>%d</Radius>
            <UseMarkers>%d</UseMarkers>
            <UseRegular>%d</UseRegular>
            <Foreground>%s</Foreground>
            <Background>%s</Background>
            <ShowHisto>%d</ShowHisto>
        </RangamePy>
        """ % (self.Sides,self.PointsK,self.Divisor,self.Radius,1 if self.UseMarkers else 0, 1 if self.UseRegular else 0,self.Foreground,self.Background, 1 if self.ShowHisto else 0)

        f = open('RangamePy.xml', 'w')
        f.write(xml)
        f.close()

class SettingsDlg(object):

    def label(self,text,r,c):
        l = Label( self.frame, text= text,underline=0)
        l.grid(row=r,column=c,sticky=W)
        return l

    def numberEntry(self,var,r,c,min=None,max=None):
        #e = Entry(self.frame,textvariable=var,validate="key",validatecommand=self.numberValidator)
        e = Spinbox(self.frame,from_=min,to=max,textvariable=var,validate="key",validatecommand=self.numberValidator)
        e.grid(row=r,column=c,sticky=W)
        return e
        
    def decimalEntry(self,var,r,c,min,max):
        e = Entry(self.frame,textvariable=var,validate="key",validatecommand=self.decimalValidator)
        e.grid(row=r,column=c,sticky=W)
        return e
        
    def checkBox(self,var,text,r,c):
        e = Checkbutton(self.frame, text=text, variable=var,underline=0)
        e.grid(row=r,column=c,sticky=W)
        return e

    def button(self,text,command,r,c):
        e = Button(self.frame, text=text, command=command, underline=0)
        e.grid(row=r,column=c)
        return e

    def color(self,color,command,r,c):
        e = Button(self.frame, background=color,width=5,command=command)
        e.grid(row=r,column=c,pady=4,sticky=W)
        return e

    def getColor(self,color,button):
        (c1,c2) =  tkColorChooser.askcolor(color)
        if c2 != None:
            color = c2
            button["bg"] = c2
        
    def getFgColor(self):
        self.getColor(self.settings.Foreground,self.fgButton )

    def getBgColor(self):
        self.getColor(self.settings.Background,self.bgButton )

    def numbersOnly(self,S,s,i):
        if len(S) > 0:
            return (S >= '0' and S <= '9') 
        else:
            return True

    def numberSlider(self,sides,start,stop,r,c):
        e = Scale(self.frame, variable=sides,from_=start,to=stop,orient=HORIZONTAL,showvalue=0)
        e.grid(row=r,column=c)
        return e

    def signedNumbersOnly(self,S,s,i):
        return self.numbersOnly(S,s,i)  or (S == '-' and i == '0')

    def decimalOnly(self,S,s,i):
        return self.numbersOnly(S,s,i) or (S == '.' and s.find('.') == -1)

    @property
    def Sides(self):
        return self._sides.get()

    @property
    def PointsK(self):
        return self._pointsK.get()

    @property
    def Divisor(self):
        return self._divisor.get()

    @property
    def UseMarkers(self):
        return self._useMarkers.get()

    @property
    def UseRegular(self):
        return self._useRegular.get()

    @property
    def Radius(self):
        return self._radius.get()

    def __init__(self, master,settings):

        self.settings = settings

        self.frame = Frame(master, padx=10, pady=10)
        self.numberValidator = self.numberCommand = (self.frame.register(self.numbersOnly), '%S', '%s', '%i') # change, before, index
        self.signedNumberValidator = (self.frame.register(self.signedNumbersOnly), '%S', '%s', '%i') # change, before, index
        self.decimalValidator = (self.frame.register(self.decimalOnly), '%S', '%s', '%i') # change, before, index

        self.frame.pack()

        self._sides = IntVar()
        self._pointsK = IntVar()
        self._divisor = DoubleVar()
        self._useMarkers = IntVar()
        self._useRegular = IntVar()
        self._showHisto = IntVar()
        self._radius = IntVar()
        
        self._sides.set(settings.Sides)
        self._pointsK.set(settings.PointsK)
        self._divisor.set(settings.Divisor)
        self._radius.set(settings.Radius)
        self._useRegular.set(settings.UseRegular)
        self._useMarkers.set(settings.UseMarkers)
        self._showHisto.set(settings.ShowHisto)

        row = 0
        self.label("Sides",row,0)
        self.frame.ss = self.numberEntry(self._sides,row,1,2,20).focus_set()

        row += 1
        self.label("Points to plot (x1000)",row,0)
        self.numberEntry(self._pointsK,row,1,1,1000000)
        
        row += 1
        self.label("Divisor",row,0)
        self.decimalEntry(self._divisor,row,1,.01,100)
       
        row += 1
        self.label("Radius",row,0)
        self.numberEntry(self._radius,row,1,1,3000)
       
        row += 1
        self.checkBox(self._useMarkers, "Use markers to show points",row,0)
        
        row += 1
        self.checkBox(self._useRegular, "Create Regular shape",row,0)

        row += 1
        self.checkBox(self._showHisto, "Show Histogram after plot",row,0)

        row += 1
        self.label("Foreground",row,0)
        self.fgButton = self.color(settings.Foreground,self.getFgColor,row,1)

        row += 1
        self.label("Background",row,0)
        self.bgButton = self.color(settings.Background,self.getBgColor,row,1)

        row += 1
        self.button("OK", self.ok, row, 0)
        self.button("Cancel", self.close, row, 1)

        self.frame.bind_all('<KeyPress-Escape>',self.close)

        self.okClicked = False

    def ok(self):
        self.settings.Sides = self._sides.get()
        self.settings.PointsK = self._pointsK.get()
        self.settings.Divisor = self._divisor.get()
        self.settings.Radius = self._radius.get()
        self.settings.UseRegular = self._useRegular.get()
        self.settings.UseMarkers = self._useMarkers.get()
        self.settings.Foreground = self.fgButton["bg"]
        self.settings.Background = self.bgButton["bg"]
        self.settings.ShowHisto = self._showHisto.get()

        self.okClicked = True

        self.close()

    def close(self,event=None):
        self.frame.quit()

    @staticmethod
    def DoModal(settings):
        import Tkinter

        root = Tkinter.Tk()
        root.title( "RangamePy Settings" )
        app = SettingsDlg(root,settings)

        root.mainloop()

        root.destroy() #Unload Tkinter

        return app.okClicked


if __name__ == "__main__":
        
        s = Settings()
        s.LoadValues()
        if SettingsDlg.DoModal(s):
            s.SaveValues()

