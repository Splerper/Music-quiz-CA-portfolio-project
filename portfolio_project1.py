import random
import re
import time
from quest_ans import question_list

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.incorrect = 0
    
    def scoring(self, correct):
        if correct:
            print("That's correct!\n")
            self.score += 1
        else:
            print("Sorry, wrong answer\n")
            self.incorrect += 1

def check_ans(answer, quest):
    if answer.lower().strip() == quest.answer and re.search("\s*", answer):
        player_1.scoring(True)
    elif answer.strip() + ")" in quest.choices and answer.lower().strip() != quest.answer:
        player_1.scoring(False)
    else:
        print("Invalid answer")
        return check_ans(input(">> "), quest)

with open("title.txt") as intro:
    title = intro.read()
    print(title)

player_1 = Player(
    input("What will you be called?\n >>")
    )
print(f"""
Good Luck, {player_1.name}
      """)
used_q = []
for i in range(0, 15):
    while True:
        question = question_list[random.randint(0, 14)]
        if question in used_q:
            continue
        used_q.append(question)
        break
    if player_1.score == 10:
        for i in range(0, 20):
            print("")
        print("You cannot beat me.")
        time.sleep(1)
        for i in range(0, 100):
            print("")
    question.pq()
    check_ans(input(">> "), question)
