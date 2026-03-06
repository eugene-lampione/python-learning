import random
from os import system

# Functions
def startGame():
	system("clear") # clear the screen
	print("Welcome to Math Flashcards!")
	choices = ["+", "-", "*", "/"]
	#choice = input(
	#	"Choose your flashcards (add | subtract | multiply | divide): ")
	numCards = input(
		"How many Cards do you want to play? ")
	showCards(int(numCards),choices)

def showCards(numCards,choices):
	correctAns = 0
	incorrectAns = 0
	cardsPlayed = 1
	while cardsPlayed <= numCards:
		choiceIndex = random.randint(0,3)
		operation = choices[choiceIndex]
		number1 = random.randint(0,10)
		number2 = random.randint(1,10)
		if operation == "+":
			solution = int(number1 + number2)
		elif operation == "-":
			solution = int(number1 - number2)
		elif operation == "*":
			solution = int(number1 * number2)
		elif operation == "/":
			solution = float(number1 / number2)
			divmodSolution = divmod(number1, number2)
			print(divmodSolution)

		answer = input(f"{cardsPlayed}. {number1} {operation} {number2} = ")
		if operation == "/":
			answer = float(answer)
		else:
			answer = int(answer)

		if answer == solution:
			correctAns += 1
			print(f"CORRECT: {number1} {operation} {number2} = {solution}")
		else:
			incorrectAns += 1
			print(f"INCORRECT: {number1} {operation} {number2} = {solution}")

		cardsPlayed +=1

	print(f"You got {correctAns} correct and {incorrectAns} wrong")
	playAgain = input("Play Again? ")
	if(playAgain.lower() == 'yes'):
		startGame()
	else:
		print("Thanks for playing.")

startGame()


