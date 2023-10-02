from quest_ans import question_list

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


print(question_list[0].pq())