import wx

class GUI_Quizer_Settings(wx.Panel):
    def __init__(self, bb_parent):
        
        def explain():
            text = ("Give how many rounds you want to play and the number of "
                    "questions per round. If you want to track the time you "
                    "spend per round, you can turn 'Keep time' on. Your file "
                    "containing tour test/exam should be in the format:\n"
                    "Question <tab> A`B`C`D <tab> Answer\nExample:\n"
                    "In which language is Quizer programmed?\tPython`Java`R`"
                    "Matlab\tPython")
            return text
        
        wx.Panel.__init__(self, bb_parent, style=wx.BORDER_SUNKEN)
        # Input parameters
        self.rounds = wx.SpinCtrl(self, min=1, max=10, initial=1)
        self.questions = wx.SpinCtrl(self, min=1, max=25, initial=10)
        self.timing = wx.ToggleButton(self, label="Off")
        self.filename = wx.FilePickerCtrl(self, path="")
    
        # Buttons
        self.stop = wx.Button(self, label="Quit")
        self.next = wx.Button(self, label="Next")
        
        # Text
        self.explain = wx.StaticText(self, label=explain())
        
        # Placing of items in frame
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox1.Add(wx.StaticText(self, label="Rounds:"), 1, wx.EXPAND | wx.ALL)
        hbox1.Add(self.rounds, 2, wx.EXPAND | wx.ALL)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2.Add(wx.StaticText(self, label="Questions:"), 1, wx.EXPAND | wx.ALL)
        hbox2.Add(self.questions, 2, wx.EXPAND | wx.ALL)
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3.Add(wx.StaticText(self, label="Keep time:"), 1, wx.EXPAND | wx.ALL)
        hbox3.Add(self.timing, 2, wx.EXPAND | wx.ALL)
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        hbox4.Add(wx.StaticText(self, label="File:"), 1, wx.EXPAND | wx.ALL)
        hbox4.Add(self.filename, 2, wx.EXPAND | wx.ALL)
        
        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        hbox5.Add(self.stop, 1, wx.EXPAND | wx.ALL)
        hbox5.Add(self.next, 1, wx.EXPAND | wx.ALL)
        
        box = wx.BoxSizer(wx.VERTICAL)
        box.Add(self.explain, 6, wx.EXPAND | wx.ALL)
        box.Add(hbox1, 1, wx.EXPAND | wx.ALL)
        box.Add(hbox2, 1, wx.EXPAND | wx.ALL)
        box.Add(hbox3, 1, wx.EXPAND | wx.ALL)
        box.Add(hbox4, 1, wx.EXPAND | wx.ALL)
        box.Add(hbox5, 1, wx.EXPAND | wx.ALL)
        self.SetSizer(box)

if __name__ == "__main__":
    class Scherm(wx.Frame):
        def __init__(self, s_parent, s_title="GUI_Quizer_Settings"):
            wx.Frame.__init__(self, s_parent, title=s_title, size=(300, 300))
            panel = wx.Panel(self)
            panel1 = GUI_Quizer_Settings(panel)
            box = wx.BoxSizer()
            box.Add(panel1, 1, wx.EXPAND | wx.ALL)
            panel.SetSizer(box)
            self.Centre()
            self.Show(True)
    app = wx.App(False)
    Scherm(None)
    app.MainLoop()
