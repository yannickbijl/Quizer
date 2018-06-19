import random

class ESC_Quizer():
    def __init__(self, filename):
        
        def read_quiz(filename):
            with open(filename) as f: 
                for line in f:
                    segments = line.split("\t")
                    self.questions.append(segments[0])
                    self.options.append(segments[1].split("`"))
                    self.answers.append(segments[2].strip())
                    
        self.questions = []
        self.options = []
        self.answers = []
        self.round_q = []
        self.round_o = []
        self.round_a = []
        read_quiz(filename)
        
    def generate_round(self, nr):
        for number in range(nr):
            randomnr = random.randint(0, len(self.questions) - 1)
            self.round_q.append(self.questions[randomnr])
            self.round_o.append(self.options[randomnr])
            self.round_a.append(self.answers[randomnr])
    
    def get_round_q(self):
        return self.round_q

    def get_round_o(self):
        return self.round_o

    def get_round_a(self):
        return self.round_a
    
    def reset_round(self):
        self.round_q = []
        self.round_o = []
        self.round_a = []