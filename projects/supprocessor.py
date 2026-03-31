import subprocess
import os

# function to run a selected pythong file
def runFile(filename):
    try:
        # run the file
        subprocess.run(["python3",filename], check=True)

    except subprocess.CalledProcessError:
        print(f"Error: Could not run {filename}")

# main Function
def mainMenu():
    while True:
        # clear screen
        os.system("clear")
        # print main menu
        print("\n---Main Menu---")
        print("1. Anagram Solver")
        print("2. Use Arrows")
        print("3. Use Arrows with TKinter")
        print("4. Choose Your Own Adventure")
        print("5. Clocks")
        print("6. File Manager")
        print("7. Flashcard Game")
        print("8. Number Guessing Game")
        print("9. Number Guessing Game GUI")
        print("10. Hangman Game")
        print("12. Image Resizer")
        print("12. Palindrome Checker")
        print("13. Password Generator")
        print("14. Password Validator")
        print("15. Rock Paper Scissors")
        print("16. Tic-Tac-Toe")
        print("17. To-Do List")
        print("18. Draw Turtles")
        print("19. Typing Speed Test")
        print("20. Word Counter")
        print("21. Quit")

        # get choice
        choice = input("Choose an option (1-21): ")

        if choice == "1":
            runFile('anagram.py')
        elif choice == "2":
            runFile('arrows.py')
        elif choice == "3":
            runFile('arrows-tkinter.py')
        elif choice == "4":
            runFile('choose-your-adventure.py')
        elif choice == "5":
            runFile('clocks.py')
        elif choice == "6":
            runFile('file-manager.py')
        elif choice == "7":
            runFile('flashcards.py')
        elif choice == "8":
            runFile('guessing_game.py')
        elif choice == "9":
            runFile('guessing_game_gui.py')
        elif choice == "10":
            runFile('hangman.py')
        elif choice == "11":
            runFile('image-resizer.py')
        elif choice == "12":
            runFile('palindrome.py')
        elif choice == "13":
            runFile('password-generator.py')
        elif choice == "14":
            runFile('password-validator.py')
        elif choice == "15":
            runFile('rock-paper-scissors.py')
        elif choice == "16":
            runFile('tic-tac-toe.py')
        elif choice == "17":
            runFile('to-do-list.py')
        elif choice == "18":
            runFile('turtle-draw.py')
        elif choice == "19":
            runFile('typing-speedtest.py')
        elif choice == "20":
            runFile('wordcount.py')
        elif choice == "21":
            print("Exiting Program...")
            break
        else:
            print("Invalid Choice. Please pick an option from 1 to 21.")
        

# run program
mainMenu()