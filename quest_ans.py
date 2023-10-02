class Questions:
    def __init__(self, question, correct_letter, choices):
        self.question = question
        self.answer = correct_letter
        self.choices = choices
        
    def __repr__(self):
        desc = f"{self.question}\n{self.choices}"
        return desc
    
    def pq(self):
        print(self)

q_1 = Questions(
    "",
    "",
    ""
    )

question_list = [q_1]