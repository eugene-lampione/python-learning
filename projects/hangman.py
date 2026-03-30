import os
import random

# cleat the screen
os.system("clear")

# creating a list of words
wordList = ['python','javascript','ruby','perl','hangman','developer','variable','syntax','function']

# select random wor from out list
def getRandomWord():
    return random.choice(wordList)

# display the current state of the guessed word
def displayWord(word,guessedLetters):
    return ' '.join([letter if letter in guessedLetters else '_' for letter in word])

# main game logice
def playHangman():
    # get the random word
    word = getRandomWord()
    
    # get length of word
    wordLength = len(word)

    # keep track of guessed letters and incorrect guesses
    # set rules: https://docs.python.org/3/tutorial/datastructures.html#sets
    # sets can;t have duplicates, so same letter cant be guessed multiple times
    guessedLetters = set() # letters players guessed correctly
    incorrectGuesses = set() # incorrect letters guessed by player
    lives = 6 # number of incorrect guessed allowed

    # prompt user
    print("Welcome to Hangman")
    print(f"The word has {wordLength} letters")

    # main game loop
    while lives > 0:
        # display the current word status
        print("\n" + displayWord(word,guessedLetters))
        print(f"\nIncorrect guesses: {', '.join(incorrectGuesses)}")
        print(f'Lives Remaining: {lives}')

        # prompt the user for a guess
        guess = input("Guess a letter: ").lower()

        # validate the guesses
        if len(guess) != 1 or not guess.isalpha():
            os.system("clear")
            print("Invalid input. Please enter a single letter.")
            continue
        
        # check if letter was already guessed
        if guess in guessedLetters or guess in incorrectGuesses:
            os.system("clear")
            print(f"You already guessed {guess}. Try a different letter.")
            continue
        
        # check if the guess is correct.
        if guess in word:
            os.system("clear")
            guessedLetters.add(guess)
            print(f"Good guess. '{guess}' is in the word.")
        else:
            os.system("clear")
            incorrectGuesses.add(guess)
            # remove a live
            lives -= 1
            print(f"Wrong guess. '{guess}' is not in the word.")

        # guess if the player has guessed the entire word
        if all(letter in guessedLetters for letter in word):
            print(f"\nCongrats your guessed the word: {word}\n")
            break
        
    # if the player runs out of lives
    if lives == 0:
        print("\nYou ran out of lives! The word was: ", word,"\n")

playHangman()

