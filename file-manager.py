# file path: /Users/eugene.lampione/Documents/repos/pythoncode/files

import os

# clear the screen
os.system("clear")

# function to create and save a file
def createFile():
    # prompt for file details
    text = input("Enter the text you want to save in the file: ")
    fileName = input("Enter the filename (e.g. myfile.txt): ")
    fileLocation = input("Enter the file location: ")

    # Ensure the directorty exists
    if not os.path.exists(fileLocation):
        os.makedirs(fileLocation)

    # full file path
    filePath = os.path.join(fileLocation,fileName)

    # create and save file
    with open(filePath, 'w') as file:
        file.write(text)
    
    print(f"File '{fileName}' saved successfully as {fileLocation}")




# function to open and read a file
def openFile():
    # prompt the user for file details
    fileName = input("Enter the file name to open: ")
    fileLocation = input("Enter the file location: ")

    # get the full path
    filePath = os.path.join(fileLocation,fileName)

    if os.path.exists(filePath):
        # open the file and read
        with open(filePath,'r') as file:
            # print contents
            print("\nFile contents:")
            print(file.read())
    else:
        print(f"File {fileName} not found at {fileLocation}")


# main functions
def fileManager():
    while True:
        print("\n--- File Manager ---")
        print("1. Creat and save a file")
        print("2. Open and read a file")
        print("3. Quit")

        # chose an option
        choice = input("Choose an option (1 | 2 | 3): ")

        if choice == "1":
            createFile()
        elif choice == "2":
            openFile()
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid Selection. Please choose 1, 2, or 3.")

# start the program
fileManager()
