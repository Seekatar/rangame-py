from Tkinter import *
import tkFileDialog
import tkColorChooser

class GridDlg(object):

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

    def __init__(self, master):

        self.frame = Frame(master, padx=10, pady=10)
        self.numberValidator = self.numberCommand = (self.frame.register(self.numbersOnly), '%S', '%s', '%i') # change, before, index
        self.signedNumberValidator = (self.frame.register(self.signedNumbersOnly), '%S', '%s', '%i') # change, before, index
        self.decimalValidator = (self.frame.register(self.decimalOnly), '%S', '%s', '%i') # change, before, index

        self.frame.pack()

        self.frame.bind_all('<KeyPress-Escape>',self.close)

        self.okClicked = False

    def close(self,event=None):
        self.frame.quit()

    def DoModal(self,settings,root,title):
        import Tkinter

        root = Tkinter.Tk()
        root.title( title)

        root.mainloop()

        root.destroy() #Unload Tkinter

        return app.okClicked

