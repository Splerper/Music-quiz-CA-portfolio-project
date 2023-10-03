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
        
flag = []
letter_count = 0
def random_choice(choices, ans, question):
    global letter_count
    
    if len(flag) >= 4:
        flag.clear()
        
    choice = random.choice(choices)
    if choice in flag:
        return random_choice(choices, ans, question)
    flag.append(choice)
    
    letter = ["a", "b", "c", "d"]
    
    if choice == ans:
        q_2.answer = letter[letter_count]
    letter_count += 1
    
    if letter_count > 1:
        if "b)" in question.choices and "c)" not in question.choices:
            if letter_count >= 1:
                letter_count = 0
        elif "c)" in  question.choices and "d)" not in question.choices:
            if letter_count >= 2:
                letter_count = 0
        elif "d)" in question.choices:
            if letter_count > 3:
                letter_count = 0
    return choice

# Questions should not have more than 4 choices.

q_1 = Questions(
    "What does the term \"diminuendo\" mean?",
    "c",
    "a) Gradually getting louder\nb) Gradually getting quicker\nc) Gradually getting quieter\nd) Slow"
    )

q2a = ["Repeat from the dal sengo (D.S)", "The end", "In time", "Repeat from the beginning"]
answer = "Repeat from the beginning"
q_2 = Questions(
    "What does \"da capo (D.C)\" mean?",
)
q_2.choices = "a) b) c) d)"
q_2.choices = f"a) {random_choice(q2a, answer, q_2)}\nb) {random_choice(q2a, answer, q_2)}\nc) {random_choice(q2a, answer, q_2)}\nd) {random_choice(q2a, answer, q_2)}"

q_3 = Questions(
    "What does \"vivace\" mean?",
    "b",
    "a) At a medium speed\nb) Lively, quick\nc) Slow\nd) Fairly quick"
)

q_4 = Questions(
    "What does the term \"meno mosso\" mean?",
    "b",
    "a) With movement\nb) Less movement; slower\nc) More movement; quicker\nd) Without movement"
)

q_5 = Questions(
    "Which term means \"one single line of music\"?",
    "d",
    "a) Polyphonic\nb) Homophonic\nc) Sterophonic\nd) Monophonic"
)

q_6 = Questions(
    "The period of music which followed Medieval is the:",
    "a",
    "a) Renaissance\nb) Baroque\nc) Classical\nd) Romantic"
)

q_7 = Questions(
    "The Baroque era began in about 1600 and ended at the time of the death of which composer?",
    "b",
    "a) Palestrina\nb) Bach\nc) Beethoven\nd) Mozart"
)

q_8 = Questions(
    "Which instrument was invented during the Renaissance period?",
    "c",
    "a) Viola\nb) Violin\nc) Viol\nd) Violoncello"
)

q_9 = Questions(
    "Which of these musical forms was popular in the Baroque era?",
    "c",
    "a) The Symphony\nb) The Mazurka\nc) The Sonata\nd) Plainsong"
)

q_10 = Questions(
    "The Classical music period spans from the death of which composer to the death of which other composers?",
    "a",
    "a) Bach to Beethoven\nb) Bach to Mozart\nc) Palestrina to Liszt\nd) Mozart to Beethoven"
)

q_11 = Questions(
    "Which instrument became hugely popular in the Classical era?",
    "c",
    "a) Flute\nb) Guitar\nc) Piano\nd) Viola"
)

q_12 = Questions(
    "In the romantic era, the focus was on:",
    "b",
    "a) Mostly form\nb) Mostly emotion\nc) Form and emotion in equal measures"
)

q_13 = Questions(
    "The harmonic minor scale is different from the major scale because:",
    "a",
    "a) It has a flat third and sixth\nb) It has an extra note\nc) It can be used in any song\nd) It has a raised 7th degree"
)

q_14 = Questions(
    "What does the term \"larghetto\" mean?",
    "d",
    "a) Very slow, solemn\nb) Gradually getting slower\nc) Smoothly\nd) Rather slow"
)

q_15 = Questions(
    "What does the term \"Stringendo\" mean?",
    "d",
    "a) Gradually getting slower\nb) Forced, accented\nc) In a singing style\nd) Gradually getting faster"
)

question_list = [q_1, q_2, q_3, q_4, q_5, q_6, q_7, q_8, q_9, q_10, q_11, q_12, q_13, q_14, q_15]