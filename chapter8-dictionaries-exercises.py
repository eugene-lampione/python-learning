# Exercises
friends = {
	"Laura":"516-263-7467",
	"Abhi":"516-123-4567",
	"Amanda":"516-890-1234",
	"Kevin":"516-567-8901",
	"Lori":"516-234-5678"
}

def getphone(name):
	print(friends[name])
	print("-----")

def addremovefriend():
	action = input("Would you like to add or remove a friend from the dictionary? ")

	if action == 'add':
		name = input("Friend's Name: ")
		phone = input("Friend's Phone: ")
		friends[name] = phone
	elif action == 'remove':
		name = input("Friend's name to remove: ")
		friends.pop(name)
	else:
		print("Please enter add or remove")
		addremovefriend();

	print(friends)
	print("-----")


friendsName = input("Whose number would you like to retrieve? ")
getphone(friendsName)

addremovefriend()

for x,y in friends.items():
	print(f"My friend {x}'s phone number is: {y}")