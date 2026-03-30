# Rock (1), Paper (2), Scissors (3)
# Rock  (1) beats Scissors (3)
# Scissors (3) beats Paper (2)
# Paper (2) beast Rock (1)
import random
from os import system

def start_game(playagain=False):
    if playagain == True:
	    system("clear") # clear the screen

    winner = False

    while winner == False:

        userguess = int(input("Enter 1 for Rock, 2 for Paper, 3 for Scissors: "))
        computerguess = random.randint(1,3)
        guesses = {
            1:"Rock",
            2:"Paper",
            3:"Scissors"
        }

        if userguess != 1 and userguess != 2 and userguess != 3:
            print("Invalid guess please try again!")
            start_game()
        else:
            if (userguess == 1 and computerguess == 3) or (userguess == 2 and computerguess == 1) or (userguess == 3 and computerguess == 2):
                print(f"You Win! {guesses[userguess]} beats {guesses[computerguess]}")
                winner = True
            elif (computerguess == 1 and userguess == 3) or (computerguess == 2 and userguess == 1) or (computerguess == 3 and userguess == 2):
                print(f"Computer Wins! {guesses[computerguess]} beats {guesses[userguess]}")
                winner = True
            else:
                print("Draw! Try Again!")

    playAgain = input("Play Again? (y/n)")
    if playAgain.lower() == "y":
        start_game(True)
    else:
        print("Thanks for Playing!")

start_game()




