# import tkinter
from tkinter import *

#import os module/library
import os
import random

# initial game state variables
number_to_guess = None
number_of_guesses = 0

# create play_again function
def reset_game():
    # set our global variable
    global number_to_guess, number_of_guesses

    #generate random number and assign to variable
    number_to_guess = random.randint(1,10)
    #set number of guesses 
    number_of_guesses = 0

    # delete result label
    result_label.config(text="")

    # clear entry box
    guess_entry.delete(0, END)

    #set submit button back to normal
    submit_button.config(state=NORMAL)

    #hide play again button
    playAgain_button.pack_forget()



# create main game function
def check_guess():
    global number_of_guesses

    # try/except block
    try:
        guess = int(guess_entry.get())
        number_of_guesses += 1

        # check the guess
        if guess < number_to_guess:
            result_label.config(text="Too Low - Try again!")
        
        elif guess > number_to_guess:
            result_label.config(text="Too High - Try Again!")
        
        else:
            result_label.config(text=f"Correct! The number was {number_to_guess} and you guessed it in {number_of_guesses} guesses!")
            #disable guess button
            submit_button.config(state=DISABLED)
            # enable play again button
            playAgain_button.pack()

    except ValueError:
        result_label.config(text="Invalid Input! Please enter a number.")
    
    


def setup_gui():
    #make our widgets global
    global result_label, guess_entry, submit_button, playAgain_button
    # create window
    root = Tk()
    # add title
    root.title("Guessing Game")
    # set the size of the app
    root.geometry("500x350")

    '''
    with Tkinter you need to pack or grid your elements into the app
    Griding allows you to put things side by side
    Packing just plops things one after the other
    '''

    # create label
    instruction_label = Label(root,text="Guess a number between 1 and 10", font=("Helvetica", 18))
    instruction_label.pack(pady=20)

    # create entry box
    guess_entry = Entry(root, font=("Helvetica",18))
    guess_entry.pack(pady=10)

    # create another label
    result_label = Label(root,text="")
    result_label.pack(pady=20)

    # create buttons
    submit_button = Button(root,text="Submit Guess", command=check_guess)
    submit_button.pack(pady=20)

    playAgain_button = Button(root,text="Play Again", command=reset_game)
    playAgain_button.pack()
    #hide this button
    playAgain_button.pack_forget()

    # On start, reset the game
    reset_game()

    # start the app
    root.mainloop()

# call our main function
setup_gui()
