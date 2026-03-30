import os

os.system("clear")

# Function to count the number of words in a sentence
def countWords(sentence):
    # split sentence into a list
    words = sentence.split()
    '''
    john elder is cool
    words = ["john","elder","is","cool"]
    '''
    # get and return the length of the list with len()
    return len(words)

# function to count number of character with spaces
def countCharacterWithSpaces(sentence):
    return len(sentence)

# function to count character without spaces
def countCharacterWithoutSpaces(sentence):
    return len(sentence.replace(" ","")) # replace("thing to replace","thing to replace with")

# main function
def wordCountProgram():
    # prompt the user
    sentence = input("Enter a sentence: ")

    if sentence:
        # get word count and character counts
        wordCount = countWords(sentence)
        charCountWithSpaces = countCharacterWithSpaces(sentence)
        charCountWithoutSpaces =  countCharacterWithoutSpaces(sentence)
    else:
        print("That's not a sentence.")

    # print results
    print(f"Word Count: {wordCount}")
    print(f"Character Count (with spaces): {charCountWithSpaces}")
    print(f"Character Count (without spaces): {charCountWithoutSpaces}")


# start programs
wordCountProgram()