import random

class Questions:
    quest_num = 0
    def __init__(self, question, correct_letter="", choices=""):
        self.question = question
        self.answer = correct_letter
        self.choices = choices
        
    def __repr__(self):
        Questions.quest_num += 1
        desc = f"{Questions.quest_num}) {self.question}\n{self.choices}"
        return desc
    
    def pq(self):
        print(self)
        
letter_count = 0
def random_choice(choices, ans, question):
    global letter_count
    
    choice = random.choice(choices)
    choices.remove(choice)
    
    letter = ["a", "b", "c", "d"]
    
    if choice == ans:
        question.answer = letter[letter_count]
        
    letter_count += 1
    if letter_count > 1:
        if "c)" not in question.choices:
            if letter_count > 1:
                letter_count = 0
        elif "d)" not in question.choices:
            if letter_count > 2:
                letter_count = 0
        elif "d)" in question.choices:
            if letter_count > 3:
                letter_count = 0
    return choice

# Questions should not have more than 4 choices.

q1a = ["Gradually getting louder", "Gradually getting quicker", "Gradually getting quieter", "Slow"] # List containing all possible choices. One must exactly match the answer variable below 
answer = "Gradually getting quieter" # Answer to the question
q_1 = Questions("What does the term \"diminuendo\" mean?") # Sets the question
q_1.choices = "a) b) c) d)" # Number of answers will go down by one letter based on num of choices ex. "a) b) c)" for 3 choices
q_1.choices = f"a) {random_choice(q1a, answer, q_1)}\nb) {random_choice(q1a, answer, q_1)}\nc) {random_choice(q1a, answer, q_1)}\nd) {random_choice(q1a, answer, q_1)}" # Sets the choices randomly to a letter

q2a = ["Repeat from the dal sengo (D.S)", "The end", "In time", "Repeat from the beginning"]
answer = "Repeat from the beginning"
q_2 = Questions("What does \"da capo (D.C)\" mean?")
q_2.choices = "a) b) c) d)"
q_2.choices = f"a) {random_choice(q2a, answer, q_2)}\nb) {random_choice(q2a, answer, q_2)}\nc) {random_choice(q2a, answer, q_2)}\nd) {random_choice(q2a, answer, q_2)}"

q3a = ["At a medium speed", "Lively, quick", "Slow", "Fairly quick"]
answer = "Lively, quick"
q_3 = Questions("What does \"vivace\" mean?")
q_3.choices = "a) b) c) d)"
q_3.choices = f"a) {random_choice(q3a, answer, q_3)}\nb) {random_choice(q3a, answer, q_3)}\nc) {random_choice(q3a, answer, q_3)}\nd) {random_choice(q3a, answer, q_3)}"

q4a = ["With movement", "Less movement; slower", "More movement; quicker", "Without movement"]
answer = "Less movement; slower"
q_4 = Questions("What does the term \"meno mosso\" mean?")
q_4.choices = "a) b) c) d)"
q_4.choices = f"a) {random_choice(q4a, answer, q_4)}\nb) {random_choice(q4a, answer, q_4)}\nc) {random_choice(q4a, answer, q_4)}\nd) {random_choice(q4a, answer, q_4)}"

q5a = ['Polyphonic', 'Homophonic', 'Sterophonic', 'Monophonic']
answer = "Monophonic"
q_5 = Questions("Which term means \"one single line of music\"?")
q_5.choices = "a) b) c) d)"
q_5.choices = f"a) {random_choice(q5a, answer, q_5)}\nb) {random_choice(q5a, answer, q_5)}\nc) {random_choice(q5a, answer, q_5)}\nd) {random_choice(q5a, answer, q_5)}"

q6a = ['Renaissance', 'Baroque', 'Classical', 'Romantic']
answer = "Renaissance"
q_6 = Questions("The period of music which followed Medieval is the:")
q_6.choices = "a) b) c) d)"
q_6.choices = f"a) {random_choice(q6a, answer, q_6)}\nb) {random_choice(q6a, answer, q_6)}\nc) {random_choice(q6a, answer, q_6)}\nd) {random_choice(q6a, answer, q_6)}"

q7a = ['Palestrina', 'Bach', 'Beethoven', 'Mozart']
answer = "Bach"
q_7 = Questions("The Baroque era began in about 1600 and ended at the time of the death of which composer?")
q_7.choices = "a) b) c) d)"
q_7.choices = f"a) {random_choice(q7a, answer, q_7)}\nb) {random_choice(q7a, answer, q_7)}\nc) {random_choice(q7a, answer, q_7)}\nd) {random_choice(q7a, answer, q_7)}"

q8a = ['Viola', 'Violin', 'Viol', 'Violoncello']
answer = 'Viol'
q_8 = Questions("Which instrument was invented during the Renaissance period?")
q_8.choices = "a) b) c) d)"
q_8.choices = f"a) {random_choice(q8a, answer, q_8)}\nb) {random_choice(q8a, answer, q_8)}\nc) {random_choice(q8a, answer, q_8)}\nd) {random_choice(q8a, answer, q_8)}"

q9a = ['The Symphony', 'The Mazurka', 'The Sonata', 'Plainsong']
answer = "The Sonata"
q_9 = Questions("Which of these musical forms was popular in the Baroque era?")
q_9.choices = "a) b) c) d)"
q_9.choices = f"a) {random_choice(q9a, answer, q_9)}\nb) {random_choice(q9a, answer, q_9)}\nc) {random_choice(q9a, answer, q_9)}\nd) {random_choice(q9a, answer, q_9)}"

q10a = ['Bach to Beethoven', 'Bach to Mozart', 'Palestrina to Liszt', 'Mozart to Beethoven']
answer = "Bach to Beethoven"
q_10 = Questions("The Classical music period spans from the death of which composer to the death of which other composers?")
q_10.choices = "a) b) c) d)"
q_10.choices = f"a) {random_choice(q10a, answer, q_10)}\nb) {random_choice(q10a, answer, q_10)}\nc) {random_choice(q10a, answer, q_10)}\nd) {random_choice(q10a, answer, q_10)}"

q11a = ['Flute', 'Guitar', 'Piano', 'Viola']
answer = "Piano"
q_11 = Questions("Which instrument became hugely popular in the Classical era?")
q_11.choices = "a) b) c) d)"
q_11.choices = f"a) {random_choice(q11a, answer, q_11)}\nb) {random_choice(q11a, answer, q_11)}\nc) {random_choice(q11a, answer, q_11)}\nd) {random_choice(q11a, answer, q_11)}"

q12a = ['Mostly form', 'Mostly emotion', 'Form and emotion in equal measures']
answer = "Mostly emotion"
q_12 = Questions("In the romantic era, the focus was on:")
q_12.choices = "a) b) c)"
q_12.choices = f"a) {random_choice(q12a, answer, q_12)}\nb) {random_choice(q12a, answer, q_12)}\nc) {random_choice(q12a, answer, q_12)}"

q13a = ['It has a flat third and sixth', 'It has an extra note', 'It can be used in any song', 'It has a raised 7th degree']
answer = "It has a flat third and sixth"
q_13 = Questions("The harmonic minor scale is different from the major scale because:")
q_13.choices = "a) b) c) d)"
q_13.choices = f"a) {random_choice(q13a, answer, q_13)}\nb) {random_choice(q13a, answer, q_13)}\nc) {random_choice(q13a, answer, q_13)}\nd) {random_choice(q13a, answer, q_13)}"

q14a = ['Very slow, solemn', 'Gradually getting slower', 'Smoothly', 'Rather slow']
answer = "Rather slow"
q_14 = Questions("What does the term \"larghetto\" mean?")
q_14.choices = "a) b) c) d)"
q_14.choices = f"a) {random_choice(q14a, answer, q_14)}\nb) {random_choice(q14a, answer, q_14)}\nc) {random_choice(q14a, answer, q_14)}\nd) {random_choice(q14a, answer, q_14)}"

q15a = ['Gradually getting slower', 'Forced, accented', 'In a singing style', 'Gradually getting faster']
answer = "Gradually getting faster"
q_15 = Questions("What does the term \"Stringendo\" mean?")
q_15.choices = "a) b) c) d)"
q_15.choices = f"a) {random_choice(q15a, answer, q_15)}\nb) {random_choice(q15a, answer, q_15)}\nc) {random_choice(q15a, answer, q_15)}\nd) {random_choice(q15a, answer, q_15)}"

question_list = [q_1, q_2, q_3, q_4, q_5, q_6, q_7, q_8, q_9, q_10, q_11, q_12, q_13, q_14, q_15]