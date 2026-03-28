import os
import random


# function to display the intro text
def displayIntro():
    print("Welcome to the Big Time Adventure Game!")
    print("You are on a quest to rescue the princess in the castle.")
    print("Navigate carefully using directions: N (north), S (south), E (east), W (west).")
    print("Watch out for pits! They could pop up anywhere...")
    print("Good luck on your adventure!\n")

# function to check for danger
def checkForPit():
    # set random level for pit falling
    # generates a random float between 0 and 1
    num = random.random()
    #print(num)
    return num < 0.2


# adventure game function
def adventureGame():
    # clear screen
    os.system("clear")

    # call display intro
    displayIntro()

    # keep track of steps
    steps = 0

    # game loop
    while True:
        direction = input("Choose a direction (N/S/E/W): ").upper()

        # check for errors
        if direction not in ['N','S','E','W']:
           print("Invalid direction, please choose N, S, E, or W.")
           continue

        # increase step count
        steps += 1

        # check for pit
        if checkForPit():
            print(f"Oh No! You chose {direction} and fell into a pit! Game Over!")
            break

        # check for 5 steps
        if steps >= 5:
            print(f"Congrats! After {steps} steps, you reached the castle and saved the Princess!. You Win!")
            break
        else:
            print(f"You moved {direction}, keep going.")


# main function
def main():
    while True:
        # call game function
        adventureGame()

        # ask to play again
        replay = input("\nWould you like to ply again (y/n)? ").lower()

        # logic to play again
        if replay != "y":
            print("\nThanks for playing!\n")
            break

# start game
main()