from random import randint

#Create a list of play options
c = ["Rock", "Paper", "Scissors"]

opponent = c[randint(0,2)]

#Set player to False
player = False

while player == False:
#sets player to True
    player = input(["Rock", "Paper", "Scissors"])
    if player == opponent:
        print("Tie! Go Again!!")
    elif player == "Rock":
        if opponent == "Paper":
            print("You lose! ", opponent, "covers ", player) 
        else: 
            print("You win!", player, "beats ", opponent)
    elif player == "Paper":
        if opponent == "Scissors":
            print("You lose! ", opponent, "cuts ", player)
        else: 
            print("You win! ", player, "covers ", opponent)
    elif player == "Scissors":
        if opponent == "Rock":
            print("You lose...", opponent, "slams ", player)
        else:
            print("You win!", player, "slashes ", opponent)
    else:
        print("That/'s not a valid play. Please check your spelling!")
#player was to True, but it is needed to be False so that the loop continues         
player = False
opponent = c[randint(0,2)]                                               