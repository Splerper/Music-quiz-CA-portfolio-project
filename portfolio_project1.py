import random
import re
import time
from quest_ans import question_list, kill_questions, Questions

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
    elif re.search("\s+", answer) and answer.strip() == "":
        print("Invalid answer")
        return check_ans(input(">> "), quest)
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
def run_game():
    count = 0
    while count < 15:
        while True:
            question = question_list[random.randint(0, 14)]
            if question in used_q:
                continue
            used_q.append(question)
            break
        if player_1.score == 10:
            for i in range(0, 20):
                print("")
            print(f"You cannot beat me {player_1.name}.") 
            time.sleep(1)
            for i in range(0, 100):
                print("")
            break
        question.pq()
        count += 1
        check_ans(input(">> "), question)
    while count < 15:
        while True:
            question = kill_questions[random.randint(0, 7)]
            if question in used_q:
                continue
            used_q.append(question)
            break
        question.pq()
        count += 1
        check_ans(input(">> "), question)
run_game()
if player_1.score <= 0:
    for i in range(0, 20):
        print("")
    print("How could this happen")
    time.sleep(2)
    for i in range(0,20):
        print("")
    print("Did we not teach you well?")
    time.sleep(2)
    out = ["What is wrong with you", "You are are not welcome here", "Don't come back here", "How could you", "There will be consequences", "Death is calling for you", "Never show your face here again"]
    for i in range(0,70):
        print(random.choice(out))
    time.sleep(1)
    for i in range(0, 100):
        print("")
    print("Try again")
    used_q.clear()
    player_1.score = 0
    player_1.incorrect = 0
    Questions.quest_num = 0
    run_game()
    if player_1.score <=0:
        for i in range(0, 20):
            print("""
                
                """)
        print("I hate you")
        time.sleep(1)
        for i in range(0, 100):
            print("""
                
                
                """)
print(f"You got {player_1.score}/15 correct!")

if player_1.score >= 15:
    print("huh, I guess I lost.. cheater")
elif player_1.score < 10 and player_1.score > 0:
    print("Better luck next time")
elif player_1.score > 10 and player_1.score < 15:
    print("Getting a little closer now ;)")