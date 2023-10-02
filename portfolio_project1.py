
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

class Questions:
    def __init__(self, question, correct_letter, choices):
        self.question = question
        self.answer = correct_letter
        self.choices = choices

print(" ##      ##  ##    ##    ######  ##    #######      #####    ##    ##  ##  #########")
print(" ###    ###  ##    ##  ##        ##   ##           ##   ##   ##    ##  ##         ##")
print(" ####  ####  ##    ##  ##        ##  ##            ##   ##   ##    ##  ##        ## ")
print(" ## #### ##  ##    ##  ##        ##  ##            ##   ##   ##    ##  ##       ##  ")
print(" ##  ##  ##  ##    ##   ######   ##  ##            ##   ##   ##    ##  ##      ##   ")
print(" ##      ##  ##    ##        ##  ##  ##            ##   ##   ##    ##  ##     ##    ")
print(" ##      ##  ##    ##        ##  ##  ##            ##   ##   ##    ##  ##    ##     ")
print(" ##      ##  ##    ##        ##  ##   ##           ##   ##   ##    ##  ##   ##      ")
print(" ##      ##  ########  #######   ##    #######      #### ### ########  ##  #########")
print("-------------------------------------------------------------------------------------")
print("This quiz will test your knowledge on music theory.                                  ")
print("-------------------------------------------------------------------------------------")

player_1 = Player(input("What will you be called?\n >>"))
