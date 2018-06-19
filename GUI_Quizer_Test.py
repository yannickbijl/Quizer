import wx

class GUI_Quizer_Test(wx.Panel):
    def __init__(self, bb_parent):
        
        wx.Panel.__init__(self, bb_parent, style=wx.BORDER_SUNKEN)
        # Input parameters
        self.round = wx.StaticText(self, label="")
        self.questionnr = wx.StaticText(self, label="")
        self.question =  wx.TextCtrl(self, value="", style=wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL)
        self.options = ["A", "B", "C", "D"]
        self.choices = wx.RadioBox(self, choices=self.options,
                                   style=wx.RA_SPECIFY_ROWS)
    
        # Buttons
        self.stop = wx.Button(self, label="Quit")
        self.next = wx.Button(self, label="Next")

        # Placing of items in frame
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox1.Add(self.round, 1, wx.EXPAND | wx.ALL)
        hbox1.Add(self.questionnr, 9, wx.EXPAND | wx.ALL)
        
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2.Add(self.stop, 1, wx.EXPAND | wx.ALL)
        hbox2.Add(self.next, 1, wx.EXPAND | wx.ALL)
        
        box = wx.BoxSizer(wx.VERTICAL)
        box.Add(hbox1, 1, wx.EXPAND | wx.ALL)
        box.Add(self.question, 3, wx.EXPAND | wx.ALL)
        box.Add(self.choices, 3, wx.EXPAND | wx.ALL)
        box.Add(hbox2, 1, wx.EXPAND | wx.ALL)
        self.SetSizer(box)

if __name__ == "__main__":
    class Scherm(wx.Frame):
        def __init__(self, s_parent, s_title="GUI_Quizer_Test"):
            wx.Frame.__init__(self, s_parent, title=s_title, size=(300, 300))
            panel = wx.Panel(self)
            panel1 = GUI_Quizer_Test(panel)
            box = wx.BoxSizer()
            box.Add(panel1, 1, wx.EXPAND | wx.ALL)
            panel.SetSizer(box)
            self.Centre()
            self.Show(True)
    app = wx.App(False)
    Scherm(None)
    app.MainLoop()
