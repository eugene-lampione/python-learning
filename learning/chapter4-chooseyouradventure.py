from os import system
system("clear")

print("Welcome to Choose Your Own Adventure")
print("The goal is to find the Python Princess")

name = input("Enter your Name: ")
name = name.lower()

system("clear")

print("You're standing in front of two doors....")
print("Do you want to enter the door on the left or right?")

question = input().lower()
if question == "left":
	system("clear")
	print("You fell into a pit and died! GAME OVER!")
elif question == "right":
	system("clear")
	print(f"Congratulation {name.capitalize()} you found")
	print("the Python Princess! YOU WIN!")
else:
	system("clear")
	print("Sorry, I don't recognize your response GAME OVER!")