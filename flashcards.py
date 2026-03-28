import random
import os

# function to generate a math problem
def generateFlashcard(operation):
    # generate two random numbers
    number1 = random.randint(1,10)
    number2 = random.randint(1,10)

    # logic to create questions
    if operation == "addition":
        correctAnswer = number1 + number2
        question = f"{number1} + {number2} = ?"
    elif operation == "substraction":
        correctAnswer = number1 - number2
        question = f"{number1} - {number2} = ?"
    elif operation == "multiplication":
        correctAnswer = number1 * number2
        question = f"{number1} * {number2} = ?"
    elif operation == "division":
        # // cast into an integer
        # ensure second number is not 0 and num 1 is divisible by num2
        while number2 == 0 or number1 % number2 != 0:
            # get new numbers
            number1 = random.randint(1,10)
            number2 = random.randint(1,10)

        correctAnswer = number1 // number2
        question = f"{number1} / {number2} = ?"

    return question, correctAnswer

# main menu function
def mainMenu():
    # clear the screen
    os.system("clear")

    # create menu
    print("\n--- Math Flashcard App ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")

    # get the user selection
    choice = input("\nChoose and option (1 - 5): ")
    return choice

# function to create a flashcard session
def flashcardSession(operation):
    while True:
        # clear the screen
        os.system("clear")

        question, correctAnswer = generateFlashcard(operation)

        # print question
        print(f"\nFlashcard: {question}")

        # prompt use for answer
        userAnswer = input("Your answer: ")

        # error handling 
        try:
            userAnswer = int(userAnswer)
        except ValueError:
            print("Invalid Input. Please enter a valid number.")

        # answer solution
        if userAnswer == correctAnswer:
            print("Correct!")
        else:
            print(f"The correct answer is {correctAnswer}")

        # ask to play again
        nextStep = input("\nWould you like another flashcard (y/n?)").lower()

        if nextStep == 'n':
            break


# main function
def flashcardApp():
    while True:
        # call main menu functions
        choice = mainMenu()

        # logic to determine choice
        if choice == "1":
            flashcardSession("addition")
        elif choice == "2":
            flashcardSession("subtraction")
        elif choice == "3":
            flashcardSession("multiplication")
        elif choice == "4":
            flashcardSession("division")
        elif choice == "5":
            print("\nGoodbye!\n")
            break
        else:
            print("Invalid Choice. Please try again.")



# start the app
flashcardApp()