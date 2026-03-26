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


# print out password rules
def showPasswordRules():
    print("Password Rules:")
    print("1. Must be at least 8 characters long.")
    print("2. Must contain at least one digit (0-9).")
    print("3. Must contain at least one lowercase letter (a-z).")
    print("4. Must contain at least one uppercase letter (A-Z).")
    print("5. Must contain at least one special character (!, @, #, $, etc.)")
    print()

def passwordValidator():
    # show password rules
    showPasswordRules()

    # prompt the user
    password = input("Please enter your password: ")

    # validate the password
    is_valid, message = validatePassword(password)

    # return the result
    if is_valid:
        print("Success: ", message)
    else:
        print("Validation Failed: ", message)

# run the program
passwordValidator()