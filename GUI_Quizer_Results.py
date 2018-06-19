import wx

class GUI_Quizer_Results(wx.Panel):
    def __init__(self, bb_parent):
        
        wx.Panel.__init__(self, bb_parent, style=wx.BORDER_SUNKEN)
        # Input parameters
        self.round = wx.StaticText(self, label="")
        self.questions =  wx.StaticText(self, label="")
        self.correct = wx.StaticText(self, label="")
        self.incorrect = wx.StaticText(self, label="")
        self.score = wx.StaticText(self, label="")
        self.time = wx.StaticText(self, label="")
        
        # Buttons
        self.stop = wx.Button(self, label="Quit")
        self.next = wx.Button(self, label="Next")
               
        # Placing of items in frame
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(self.stop, 1, wx.EXPAND | wx.ALL)
        hbox.Add(self.next, 1, wx.EXPAND | wx.ALL)
        
        box = wx.BoxSizer(wx.VERTICAL)
        box.Add(self.round, 1, wx.EXPAND | wx.ALL)
        box.Add(self.questions, 1, wx.EXPAND | wx.ALL)
        box.Add(self.correct, 1, wx.EXPAND | wx.ALL)
        box.Add(self.incorrect, 1, wx.EXPAND | wx.ALL)
        box.Add(self.score, 1, wx.EXPAND | wx.ALL)
        box.Add(self.time, 1, wx.EXPAND | wx.ALL)
        box.Add(hbox, 1, wx.EXPAND | wx.ALL)
        self.SetSizer(box)

if __name__ == "__main__":
    class Scherm(wx.Frame):
        def __init__(self, s_parent, s_title="GUI_Quizer_Results"):
            wx.Frame.__init__(self, s_parent, title=s_title, size=(300, 300))
            panel = wx.Panel(self)
            panel1 = GUI_Quizer_Results(panel)
            box = wx.BoxSizer()
            box.Add(panel1, 1, wx.EXPAND | wx.ALL)
            panel.SetSizer(box)
            self.Centre()
            self.Show(True)
    app = wx.App(False)
    Scherm(None)
    app.MainLoop()
