#import os module/library
import os
import random

# create play_again function
def play_again():
    # prompt user
    again = input("Would you like to play again? y/n: ")
    # logic to figure out what to do
    if again == "y" or again == "Y" or again == "yes" or again == "YES" or again == "Yes":
        game()
    else:
        print("Thanks for playing")
        return


# create main game function
def game():

    # create vairiable to keep track of guesses and correct
    number_of_guesses = 0
    correct = False

    #clear screen
    os.system("clear")

    #generate random number and assign to variable
    number_to_guess = random.randint(1,10)

    # get user input
    print("Guess a number between 1 and 10 ")

    # create guessing loop
    while correct == False:

        # try/except block
        try:
            guess = int(input("Enter your guess: "))
        except Exception as e:
            print("Something went wrong. Game Over")
            return
        
        # check the guess
        if guess < number_to_guess:
            print("Too Low - Try again!")
            # increment number of guesses
            number_of_guesses += 1
        
        elif guess > number_to_guess:
            print("Too High - Try Again!")
            # increment number of guesses
            number_of_guesses += 1
        
        elif guess == number_to_guess:
            # increment number of guesses
            number_of_guesses +=1
            print(f"Correct! The number was {number_to_guess} and you guessed it in {number_of_guesses} guesses!")
            
            # set correct to true
            correct = True

            # play again function
            play_again()


# call our game function
game()


