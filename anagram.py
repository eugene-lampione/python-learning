import os

os.system("clear")

# function to check if two words are anamgrams
def areAnagrams(word1,word2):
    # decide if two words are anamgrams
    '''
    python sorted
    john
    sorted(john) == hjno
    print(sorted("dog"))
    print(sorted("god"))
    print(sorted("dog") == sorted("god"))
    '''
    return sorted(word1) == sorted(word2)

# function to find all the anagrams of a word from a list of dictionary words
def findAnagrams(word,wordList):
    # convert word to lowercase
    word = word.lower()

    # return a list of words of the inputted word
    return [w for w in wordList if areAnagrams(word, w.lower()) and w.lower() != word]

# main function
def anagramSolver():
    # create a list of dictionary words
    wordList = ["listen","silent","enlist","google","elder","dog","god","evil","vile","live","tinsel"]

    # prompt user for a word
    word = input("Enter a word to find it's anagrams: ")

    # find anagrams for the word
    anagrams = findAnagrams(word,wordList)

    # output
    if anagrams:
        print(f"Anagrams of '{word}' are {','.join(anagrams)}")
    else:
        print(f"No anagrams found for '{word}'.")


anagramSolver()