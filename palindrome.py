import os
os.system("clear")

def is_palidrome(string):
    '''
    #remove spaces and convert to lower case and strip notation
    cleaned_string = ''
    # loop through user input
    for char in string:
        # check if character is character
        if char.isalnum():
            cleaned_string += char.lower()
    '''
    # short hand for the above code
    cleaned_string = "".join(char.lower() for char in string if char.isalnum())

    # check if string is the same forward and backward
    return cleaned_string == cleaned_string[::-1]


# ask the user for input
userinput = input("Enter a word or phrase to see if it's a palindrome: ")

# slice = [start:stop:step]
# end goes to but not including
# step tell you how many to go (-1 goes in reverse)
#userinput = userinput[::-1]



# Check if true or false
if is_palidrome(userinput):
    print(f"{userinput} is a palindrome!")
else:
    print(f"{userinput} is NOT a palindrome.")
