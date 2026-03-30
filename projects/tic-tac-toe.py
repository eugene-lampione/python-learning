import os

# clear the screen
def clearScreen():
    os.system("clear")

'''
1 | 2 | 3
--+---+--
4 | 5 | 6
--+---+--
7 | 8 | 9
'''

# print board
def printBoard(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

# check for winner
def checkWinner(board, currentPlayer):
    # define winning combos
    winCombinations = [
        # rows
        [0,1,2],[3,4,5],[6,7,8],
        # columns
        [0,3,6],[1,4,7],[2,5,8],
        # diagonals
        [0,4,8],[2,4,6],
    ]

    # check if any winning combo is met
    for combination in winCombinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] == currentPlayer:
            return True
        
    return False

# check for a draw
def checkForDraw(board):
    # ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    return all(spot in ["X","O"] for spot in board)    

# main function
def playTicTacToe():
    # initialize the board (empty spots represented by numbers)
    # ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    board = [str(i) for i in range(1,10)]
    print(board)

    # define our players
    currentPlayer = "X"

    # main game loop
    while True:
        clearScreen()
        printBoard(board)

        # get player move
        move = input(f"Player {currentPlayer}, enter your move (1-9): ")

        # validate the move
        if not move.isdigit() or int(move) < 1 or int(move) > 9:
            print("Invalid Input. Please enter a number between 1 and 9.\n")
            input("Press Enter to Continue....")
            continue

        # convert move number to index number
        move = int(move) - 1

        # check if spot in already taken
        if board[move] in ["X","O"]:
            print("That spot is already taken, try again.\n")
            input("Press Enter to Continue....")
            continue

        # update the board
        board[move] = currentPlayer

        # check if the current player won
        if checkWinner(board, currentPlayer):
            clearScreen()
            #redraw updated board
            printBoard(board)
            print(f"Player {currentPlayer} wins!")
            break

        # check for draw
        if checkForDraw(board):
            clearScreen()
            printBoard(board)
            print("It's a Draw!")
            break


        # switch players
        currentPlayer = "O" if currentPlayer == "X" else "X"


# play the game
playTicTacToe()