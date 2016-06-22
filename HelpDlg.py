from GridDlg import GridDlg
from tkinter import *
import tkinter.font

class HelpDlg(GridDlg):
    
    def __init__(self,title):
        super(HelpDlg,self).__init__(title)

        row = 0
        l = self.label("Basic help",row,0,font="Helvetica 16 bold italic")
        
        row += 1
        self.label("C",row,0,0)
        self.label("Configuration dlg",row,1)

        row += 1
        self.label("P or space",row,0,0)
        self.label("Plot points",row,1)

        row += 1
        self.label("R",row,0,0)
        self.label("Reset",row,1)

        row += 1
        self.label("H",row,0,0)
        self.label("Toggle histogram",row,1)
        
        row += 1
        self.label("W",row,0,0)
        self.label("Wipe background",row,1)
        
        row += 1
        self.label("Esc",row,0,0)
        self.label("Exit",row,1)
        
        row += 1
        self.label("F1",row,0,0)
        self.label("This help",row,1)
        
    @staticmethod
    def Show():
        
        HelpDlg("Rangame Help").DoModal()



if __name__ == "__main__":

    HelpDlg.Show()
