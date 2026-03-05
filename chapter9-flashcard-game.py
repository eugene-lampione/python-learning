import random
from os import system

# Functions
def startGame():
	system("clear") # clear the screen
	print("Welcome to Math Flashcards!")
	choice = input(
		"Choose your flashcards (add | subtract | multiply | divide): ")
	numCards = input(
		"How many Cards do you want to play? ")

	selectCards(int(numCards),choice)

def selectCards(numCards,choice):
	if choice.lower() == "add":
		additionCards(numCards)
	elif choice.lower() == "subtract":
		subtractionCards(numCards)
	elif choice.lower() == "multiply":
		multiplicationCards(numCards)
	elif choice.lower() == "divide":
		divisionCards(numCards)
	else:
		print(f"Invalid choice: {choice}")
		input("Please hit enter to start over")
		startGame()

'''
def playAgain(cards="", correct=0, incorrect=0):
	playAgain = input("Would you like to play again? (yes|no|restart) ")

	if playAgain.lower() == "yes":
		selectCards(cards,correct,incorrect)
	elif playAgain.lower() == "no":
		print(f"Thanks for playing!")
		print(f"You got {correct} correct.")
		print(f"You got {incorrect} wrong.")
	elif playAgain.lower() == "restart":		
		print(f"Thanks for playing!")
		print(f"You got {correct} correct.")
		print(f"You got {incorrect} wrong.")
		input("Hit enter to restart")
		startGame()
	else:
		print(f"Sorry didn't recognize {playAgain}")
		playAgain()
'''

def additionCards(numCards):
	correctAns = 0
	incorrectAns = 0
	cardsPlayed = 1
	while cardsPlayed <= numCards:
		number1 = random.randint(0,10)
		number2 = random.randint(0,10)
		solution = number1 + number2
		answer = input(f"{cardsPlayed}. {number1} + {number2} = ")

		if int(answer) == int(solution):
			correctAns += 1
			print(f"CORRECT: {number1} + {number2} = {solution}")
		else:
			incorrectAns += 1
			print(f"INCORRECT: {number1} + {number2} = {solution}")

		cardsPlayed +=1

	print(f"You got {correctAns} correct and {incorrectAns} wrong")
	playAgain = input("Play Again? ")
	if(playAgain.lower() == 'yes'):
		startGame()
	else:
		print("Thanks for playing.")

def subtractionCards(numCards):
	correctAns = 0
	incorrectAns = 0
	cardsPlayed = 1
	while cardsPlayed <= numCards:
		number1 = random.randint(0,10)
		number2 = random.randint(0,10)
		solution = number1 - number2
		answer = input(f"{cardsPlayed}. {number1} - {number2} = ")

		if int(answer) == int(solution):
			correctAns += 1
			print(f"CORRECT: {number1} - {number2} = {solution}")
		else:
			incorrectAns += 1
			print(f"INCORRECT: {number1} - {number2} = {solution}")

		cardsPlayed +=1

	print(f"You got {correctAns} correct and {incorrectAns} wrong")
	playAgain = input("Play Again? ")
	if(playAgain.lower() == 'yes'):
		startGame()
	else:
		print("Thanks for playing.")

def multiplicationCards(numCards):
	correctAns = 0
	incorrectAns = 0
	cardsPlayed = 1
	while cardsPlayed <= numCards:
		number1 = random.randint(0,10)
		number2 = random.randint(0,10)
		solution = number1 * number2
		answer = input(f"{cardsPlayed}. {number1} * {number2} = ")

		if int(answer) == int(solution):
			correctAns += 1
			print(f"CORRECT: {number1} * {number2} = {solution}")
		else:
			incorrectAns += 1
			print(f"INCORRECT: {number1} * {number2} = {solution}")

		cardsPlayed +=1
	
	print(f"You got {correctAns} correct and {incorrectAns} wrong")
	playAgain = input("Play Again? ")
	if(playAgain.lower() == 'yes'):
		startGame()
	else:
		print("Thanks for playing.")

def divisionCards(numCards):
	correctAns = 0
	incorrectAns = 0
	cardsPlayed = 1
	while cardsPlayed <= numCards:
		number1 = random.randint(0,10)
		number2 = random.randint(1,10)
		solution = float(number1 / number2)
		answer = input(f"{cardsPlayed}. {number1} / {number2} = ")

		if float(answer) == solution:
			correctAns += 1
			print(f"CORRECT: {number1} / {number2} = {solution}")
		else:
			incorrectAns += 1
			print(f"INCORRECT: {number1} / {number2} = {solution}")

		cardsPlayed +=1

	print(f"You got {correctAns} correct and {incorrectAns} wrong")
	playAgain = input("Play Again? ")
	if(playAgain.lower() == 'yes'):
		startGame()
	else:
		print("Thanks for playing.")


startGame()


