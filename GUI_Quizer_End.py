import wx

class GUI_Quizer_End(wx.Panel):
    def __init__(self, bb_parent):
        def ending():
            txt = ("Thank you for using Quizer. I developed this to help me "
                   "studying. Hopefully this will help you too. Good luck " 
                   "with your exams.\n\nBest,\nDeveloper: Yannick Bijl\n\n" 
                   "Github: www.github.com/yannickbijl/\nWebsite: "
                   "yannickbijl.github.io")
            return txt
        
        wx.Panel.__init__(self, bb_parent, style=wx.BORDER_SUNKEN)
        # Input parameters
        self.ending = (wx.StaticText(self, label=ending()))
        
        # Buttons
        self.stop = wx.Button(self, label="Quit")
        self.restart = wx.Button(self, label="Restart")
               
        # Placing of items in frame
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(self.stop, 1, wx.EXPAND | wx.ALL)
        hbox.Add(self.restart, 1, wx.EXPAND | wx.ALL)
        
        box = wx.BoxSizer(wx.VERTICAL)
        box.Add(self.ending, 5, wx.EXPAND | wx.ALL)
        box.Add(hbox, 1, wx.EXPAND | wx.ALL)
        self.SetSizer(box)

if __name__ == "__main__":
    class Scherm(wx.Frame):
        def __init__(self, s_parent, s_title="GUI_Quizer_End"):
            wx.Frame.__init__(self, s_parent, title=s_title, size=(300, 300))
            panel = wx.Panel(self)
            panel1 = GUI_Quizer_End(panel)
            box = wx.BoxSizer()
            box.Add(panel1, 1, wx.EXPAND | wx.ALL)
            panel.SetSizer(box)
            self.Centre()
            self.Show(True)
    app = wx.App(False)
    Scherm(None)
    app.MainLoop()
