import time
import random
import os

# clear the screen
os.system("clear")

# list of sentences
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is an easy to learn programming language.",
    "Artificial Intelligence will shape the future of technology.",
    "Typing speed tests are quite stupid and a waste of time!",
    "Consistent practice is key to mastering any skill."
]

# function to calculate words per minute
def calculateWPM(startTime,endTime,typedSentence):
    # calcute time in seconds that it took to finish
    timeTaken = endTime - startTime # in seconds
    # get number of words
    numberOfWords = len(typedSentence.split())
    # calculate WPM
    wpm = (numberOfWords / timeTaken) * 60

    # return results
    return(round(wpm,2))



# function to run the typing speed test
def typingSpeedTest():
    # chose a random sentence from list
    sentence = random.choice(sentences)

    print("\n--- Typing Speed Test ---")
    print("Type the following sentence as fast as you can: ")
    print(f"\n{sentence}\n")

    # tell the user to hit enter to start
    input("Press Enter when you are ready to start...")

    # start the timer
    startTime = time.time()
    #print(startTime)

    # prompt the user to start typing
    typedSentence = input("\nStart Typing Here (hit enter when finished):\n")

    # get the end time
    endTime = time.time()

    # calculate WPM (word per minute)
    wpm = calculateWPM(startTime,endTime,typedSentence)

    # output the results / check for errors
    if typedSentence == sentence:
        print(f"Great Job! Your typing speed is {wpm} words per minute!")
    else:
        print(f"Your typing speed is {wpm} wordd per minutes, but there we some mistakes")


# main function
def startTest():
    while True:
        # clear the screen
        os.system("clear")

        # start the test
        typingSpeedTest()

        # ask the user to try again
        retry = input("\nWould yo like to try again? (y/n)? ").lower()

        # logic to determine y/n
        if retry != "y":
            print("\nThanks for using the Typing Speed test. Bye!\n")
            break



# run the app
startTest()

