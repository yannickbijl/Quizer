import datetime
import random
import sys

import wx

from ESC_Quizer import ESC_Quizer
from GUI_Quizer_Settings import GUI_Quizer_Settings
from GUI_Quizer_Test import GUI_Quizer_Test
from GUI_Quizer_Results import GUI_Quizer_Results
from GUI_Quizer_End import GUI_Quizer_End

class Quizer(wx.Frame):
    def __init__(self, s_parent, s_title="Quizer"):
        wx.Frame.__init__(self, s_parent, title=s_title, style=wx.DEFAULT_FRAME_STYLE ^ wx.MAXIMIZE_BOX ^ wx.RESIZE_BORDER)
        self.panel = wx.Panel(self)
        
        self.frames()
        self.hiding()
        self.binder()
                
        self.panel.SetSizer(self.box2)
        self.dic['A'].Show()
        self.Show(True)
        self.Centre()
        self.SetSize((300, 300))
        
        box = wx.BoxSizer()
        box.Add(self.panel, 1, wx.ALL | wx.EXPAND)
        self.SetSizer(box)

    def frames(self):
        def dic_make():
            self.dic = {}
            self.dic['A'] = self.quiz_settings
            self.dic['B'] = self.quiz_test
            self.dic['C'] = self.quiz_results
            self.dic['D'] = self.quiz_end

        self.quiz_settings = GUI_Quizer_Settings(self.panel)
        self.quiz_test = GUI_Quizer_Test(self.panel)
        self.quiz_results = GUI_Quizer_Results(self.panel)
        self.quiz_end = GUI_Quizer_End(self.panel)

        dic_make()
        self.box2 = wx.BoxSizer()
        for x in self.dic:
            self.box2.Add(self.dic[x], 1, wx.ALL | wx.EXPAND)

    def hiding(self):
        for x in self.dic:
            self.dic[x].Hide()

    def binder(self):
        def stop_buttons():
            for x in self.dic:
                self.dic[x].stop.Bind(wx.EVT_BUTTON, self.quitting)

        def other_buttons():
            self.quiz_settings.timing.Bind(wx.EVT_TOGGLEBUTTON, self.tog_time)
            self.quiz_settings.next.Bind(wx.EVT_BUTTON, self.next_frame1)
            self.quiz_test.next.Bind(wx.EVT_BUTTON, self.next_frame2)
            self.quiz_results.next.Bind(wx.EVT_BUTTON, self.next_frame3)
            self.quiz_end.restart.Bind(wx.EVT_BUTTON, self.restart_quiz)

        stop_buttons()
        other_buttons()

    def tog_time(self, event):
        if event.GetEventObject().GetValue():
            event.GetEventObject().SetLabel("On")
        else:
            event.GetEventObject().SetLabel("Off")

    def quitting(self, event):
        sys.exit()

    def next_frame1(self, event):
        def get_vars():
            self.rounds = self.quiz_settings.rounds.GetValue()
            self.questionnr = self.quiz_settings.questions.GetValue()
            self.timing = self.quiz_settings.timing.GetValue()
            if self.timing:
                self.total_time = 0
                self.start_time = datetime.datetime.now()
            
            self.rounds_done = 0
            self.questions_done = 0
            self.correct = 0
            self.incorrect = 0
            
            self.quiz = ESC_Quizer(self.quiz_settings.filename.GetPath())

            
        get_vars()
        self.get_quiz_round()
        self.set_question()
        self.hiding()
        self.dic['B'].Show()
        self.Layout()
        self.Centre()
        self.Refresh()

    def next_frame2(self, event):        
        def check_question():
            if self.opt[self.quiz_test.choices.GetSelection()] == self.answer:
                self.correct += 1
            else:
                self.incorrect += 1
        
        def set_text():
            self.quiz_results.round.SetLabel(f"Round:\t{self.rounds_done}")
            self.quiz_results.questions.SetLabel(f"Questions:\t{self.questions_done * self.rounds_done}")
            self.quiz_results.correct.SetLabel(f"Correct:\t{self.correct}")
            self.quiz_results.incorrect.SetLabel(f"Correct:\t{self.incorrect}")
            self.quiz_results.score.SetLabel(f"Score:\t{self.correct - self.incorrect/3}")
            if self.timing:
                self.quiz_results.time.SetLabel(f"Total time:\t{self.total_time}")
            

        check_question()
        self.questions_done += 1
        if self.questions_done == self.questionnr:
            if self.timing:
                self.total_time = datetime.datetime.now() - self.start_time
            self.quiz.reset_round()
            self.rounds_done += 1
            set_text()
            self.hiding()
            self.dic['C'].Show()
            self.Layout()
            self.Centre()
        else:
            self.set_question()
            self.Refresh()

    def next_frame3(self, event):               
        if self.rounds_done == self.rounds:
            self.hiding()
            self.dic['D'].Show()
            self.Layout()
            self.Centre()
        else:
            if self.timing:
                self.start_time = datetime.datetime.now()
            self.questions_done = 0
            self.get_quiz_round()
            self.set_question()
            self.hiding()
            self.dic['B'].Show()
            self.Layout()
            self.Centre()

    def restart_quiz(self, event):
        def set_values():
            self.quiz_settings.rounds.SetValue(1)
            self.quiz_settings.questions.SetValue(10)
            self.quiz_settings.timing.SetLabel("Off")
            self.quiz_settings.timing.SetValue(False)
            self.quiz_settings.filename.SetPath("")
        
        set_values()
        self.hiding()
        self.dic['A'].Show()
        self.Layout()
        self.Centre()

    def get_quiz_round(self):
        self.quiz.generate_round(self.questionnr)
        self.r_q = self.quiz.get_round_q()
        self.r_a = self.quiz.get_round_a()
        self.r_o = self.quiz.get_round_o()
    
    def set_question(self):
        random_nr = random.randint(0, len(self.r_q) - 1)
        
        self.quiz_test.round.SetLabel("Round: " + str(self.rounds_done + 1) + "\t")
        self.quiz_test.questionnr.SetLabel("Question: " + str(self.questions_done + 1))
        self.quiz_test.question.SetLabel(self.r_q.pop(random_nr))
        self.answer = self.r_a.pop(random_nr)
        self.opt = self.r_o.pop(random_nr)
        for option in range(4):
            try:
                self.quiz_test.choices.SetItemLabel(option, self.opt[option])
            except IndexError:
                self.quiz_test.choices.SetItemLabel(option, "")


# Is called when this script is used as the MAIN.
if __name__ == "__main__":
    class MyApp(wx.App):
        def OnInit(self):
            frame = Quizer(None)
            frame.Show(True)
            frame.Centre()
            self.SetTopWindow(frame)
            return True

    # The application-loop
    app = MyApp(0)
    app.MainLoop()