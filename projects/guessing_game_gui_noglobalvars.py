# import tkinter
from tkinter import *

#import os module/library
import os
import random


# create play_again function
def reset_game(guess_entry,result_label,submit_button,playAgain_button, state):
    
    #generate random number and assign to variable
    state['number_to_guess'] = random.randint(1,10)
    #set number of guesses 
    state['number_of_guesses'] = 0

    # delete result label
    result_label.config(text="")

    # clear entry box
    guess_entry.delete(0, END)

    #set submit button back to normal
    submit_button.config(state=NORMAL)

    #hide play again button
    playAgain_button.pack_forget()



# create main game function
def check_guess(guess_entry,result_label,submit_button,playAgain_button, state):

    # try/except block
    try:
        guess = int(guess_entry.get())
        state['number_of_guesses'] += 1

        # check the guess
        if guess < state['number_to_guess']:
            result_label.config(text="Too Low - Try again!")
            # clear entry box
            guess_entry.delete(0, END)
            guess_entry.focus_set()
        
        elif guess > state['number_to_guess']:
            result_label.config(text="Too High - Try Again!")
            # clear entry box
            guess_entry.delete(0, END)
            guess_entry.focus_set()
        
        else:
            result_label.config(text=f"Correct! The number was {state['number_to_guess']} and you guessed it in {state['number_of_guesses']} guesses!")
            #disable guess button
            submit_button.config(state=DISABLED)
            # enable play again button
            playAgain_button.pack()

    except ValueError:
        result_label.config(text="Invalid Input! Please enter a number.")
    
    


def setup_gui():
    # create window
    root = Tk()
    # add title
    root.title("Guessing Game")
    # set the size of the app
    root.geometry("500x350")

    #set the game state
    state = {'number_to_guess':None, 'number_of_guesses':0}

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

    guess_entry.bind('<Return>', lambda event=None: submit_button.invoke())

    # create another label
    result_label = Label(root,text="")
    result_label.pack(pady=20)

    # create buttons
    submit_button = Button(root,text="Submit Guess", command=lambda: check_guess(guess_entry,result_label,submit_button,playAgain_button, state))
    submit_button.pack(pady=20)


    playAgain_button = Button(root,text="Play Again", command=lambda:reset_game(guess_entry,result_label,submit_button,playAgain_button, state))
    playAgain_button.pack()
    #hide this button
    playAgain_button.pack_forget()

    # On start, reset the game
    reset_game(guess_entry,result_label,submit_button,playAgain_button, state)

    # start the app
    root.mainloop()

# call our main function
setup_gui()
