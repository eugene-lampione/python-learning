from os import system
system("clear")

print("Welcome to the Math Flashcard game")
print("Question: 5 + 23")

answer = input()

if answer == "28":
	print("You are CORRECT")
else:
	print("You are INCORRECT")

print("-----")

fname = input("What is your first name?")
lname = input("What is your last name?")

fullname = fname + " " + lname
print(fullname.title())
print("-----")

name = input("What is your name?")
print(f"Hi {name.title()}, your name has {len(name)} characters.")