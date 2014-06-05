from GridDlg import GridDlg

class HelpDlg(GridDlg):
    
    def __init__(self,master):
        super(HelpDlg,self).__init__(master)

        row = 0
        self.Label("Basic help",row,0)
        row += 1
        self.Label("C",row,0)
        self.Label("Configuration dlg",row,1)


    @staticmethod
    def DoModal(settings):
        import Tkinter

        root = Tkinter.Tk()
        root.title( "RangamePy Settings" )
        app = SettingsDlg(root,settings)

        root.mainloop()

        root.destroy() #Unload Tkinter

        return app.okClicked


