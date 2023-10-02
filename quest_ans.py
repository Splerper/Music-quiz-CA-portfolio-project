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
    "What does the term \"diminuendo\" mean?",
    "c",
    "a) Gradually getting louder\nb) Gradually getting quicker\nc) Gradually getting quieter\nd) Slow"
    )

q_2 = Questions(
    "What does \"da capo (D.C)\" mean?",
    "d",
    "a) Repeat from the dal sengo (D.S)\nb) The end\nc) In time\nd) Repeat from the beginning"
)

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
    "a) Very slow, solemn\nb) Gradually getting slower\n c) Smoothly\nd) Rather slow"
)

q_15 = Questions(
    "What does the term \"Stringendo\" mean?",
    "d",
    "a) Gradually getting slower\nb) Forced, accented\nc) In a singing style\nd) Gradually getting faster"
)

question_list = [q_1, q_2, q_3, q_4, q_5, q_6, q_7, q_8, q_9, q_10, q_11, q_12, q_13, q_14, q_15]