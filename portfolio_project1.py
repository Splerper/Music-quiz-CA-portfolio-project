import random
from quest_ans import question_list
import re

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.incorrect = 0
    
    def scoring(self, correct):
        if correct:
            print("That's correct!")
            self.score += 1
        else:
            print("Sorry, wrong answer")
            self.incorrect += 1

def check_ans(answer, quest):
    if answer.lower() == quest.answer:
        print("corrent")
    elif answer + ")" in quest.choices and answer.lower() != quest.answer:
        print("incorrent")
    else:
        print("Invalid answer")
        return check_ans(input(">> "), quest)

print(""" ##      ##  ##    ##    ######  ##    #######      #####    ##    ##  ##  #########
 ###    ###  ##    ##  ##        ##   ##           ##   ##   ##    ##  ##         ##
 ####  ####  ##    ##  ##        ##  ##            ##   ##   ##    ##  ##        ## 
 ## #### ##  ##    ##  ##        ##  ##            ##   ##   ##    ##  ##       ##  
 ##  ##  ##  ##    ##   ######   ##  ##            ##   ##   ##    ##  ##      ##   
 ##      ##  ##    ##        ##  ##  ##            ##   ##   ##    ##  ##     ##    
 ##      ##  ##    ##        ##  ##  ##            ##   ##   ##    ##  ##    ##     
 ##      ##  ##    ##        ##  ##   ##           ##   ##   ##    ##  ##   ##      
 ##      ##  ########  #######   ##    #######      #### ### ########  ##  #########
-------------------------------------------------------------------------------------
This quiz will test your knowledge on music theory and history.
-------------------------------------------------------------------------------------""")

player_1 = Player(
    input("What will you be called?\n >>")
    )
print(f"""
Good Luck, {player_1.name}
      """)

question = question_list[random.randint(0, 14)]
question.pq()
check_ans(input(">> "), question)