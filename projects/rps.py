import random
import os

def play_again():
    while True:
        #ask to play again
        user_input = input("Do you want to play again (yes/no): ").lower()

        # logic
        if(user_input in ["yes","no"]):
            return user_input == "yes"
        else:
            print("Invalid input. Please Enter 'yes' or 'no'.")

def determine_winner(user_choice,computer_choice):
    # determine tie
    if user_choice == computer_choice:
        return "It's a tie!!!"
    #determine user win
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You Win!"
    else:
        return "Computer Wins."


def get_computer_choice():
    # have computer select rock, paper, scissors
    choices = ["rock","paper","scissors"]
    return random.choice(choices)

def get_user_choice():
    choices = {
        1:"rock",
        2:"paper",
        3:"scissors"
    }
    try:
        user_input = int(input("Enter 1 for Rock, 2 for Paper, 3 for Scissor: "))
        if user_input in choices:
            return choices[user_input]
        else:
            print("Invalid Choice. Please try again!")
            return get_user_choice()


    except ValueError:
        print("Invalid Input. Please enter a number between 1 and 3.")
        return get_user_choice()

#set up the game
def play_game():
    while True:

        # clear screen
        os.system("clear")

        # get users choice
        user_choice = get_user_choice()

        # get computer choice
        computer_choice = get_computer_choice()

        #user outputs
        print(f"You chose: {user_choice}")
        # computer output
        print(f"Computer chose: {computer_choice}")

        # determine winner
        result = determine_winner(user_choice,computer_choice)
        # print result
        print(result)

        #end the game
        if not play_again():
            print("Thanks for playing!")
            break

play_game()
