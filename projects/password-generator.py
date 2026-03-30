import random
import string
import os

# clear screen
os.system("clear")

# validate the password
def validatePassword(password):
    # check our password rules
    if len(password) < 8:
        return False, "Password must be at least character long."
    # check for digits
    if not any(char.isdigit() for char in password):
        return False, "Password must contain at least one digit."
    #check for lowercase
    if not any(char.islower() for char in password):
        return False, "Password must contain at least one lowercase letter."
    #check for uppercase
    if not any(char.isupper() for char in password):
        return False, "Password must contain at least one uppercase letter."
    # check for special characters
    if not any(char in string.punctuation for char in password):
        return False, "Password must contain at least one special character."
    # return true 
    return True, "Password is strong!"

# generate password
def generatePassword(length):
    while True:
        # Ensure we meet the basic criteria (the four things) at least once
        # https://docs.python.org/3/library/string.html
        password = [
            random.choice(string.ascii_lowercase), # at least one lowercase
            random.choice(string.ascii_uppercase), # at least one uppercase
            random.choice(string.digits), # at least one digit
            random.choice(string.punctuation), # at least one special character
        ]

        # fill in the rest of the password character from all character sets
        # get remaining character count
        remainingLength = length - 4
        # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
        password += random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation,k=remainingLength)
        # password = ["s","G","6","%","9","$","H","1"]
        
        # shuffle the list
        random.shuffle(password)

        #convert list to a string using join()
        password = ''.join(password)

        # validate the password
        is_valid, message = validatePassword(password)
        if is_valid:
            return password



# prompt the user
def passwordGenerator():
    while True:
        try:
            # get the password length
            length = int(input("Enter the desired password length (minimum 8): "))
            if length < 8:
                print("Password length must be at least 8 characters.")
                continue
            break

        except ValueError:
            print("Invalid input. Please enter a number.")

    # generate the password
    password = generatePassword(length)
    print(f"Generated Password: {password}")
    print("This password is strong!!")

# run the program
passwordGenerator()