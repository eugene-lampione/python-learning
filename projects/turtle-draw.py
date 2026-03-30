import os
import turtle
# https://docs.python.org/3/library/turtle.html

# clear screen
os.system("clear")

# create a turtle object
t = turtle.Turtle()
# create screen
#screen = turtle.Screen()

# reset turtle
def resetTurtle():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

# draw square
def drawSquare(size):
    #resetTurtle()
    # for loop for 4 lines
    for _ in range(4):
        t.forward(size)
        t.right(90)


# draw triangle
def drawTriangle(size):
    #resetTurtle()
    for _ in range(3):
        t.forward(size)
        t.left(120)

# draw circle
def drawCircle(radius):
    #resetTurtle()
    t.circle(radius)



# main function
def drawShape():
    # prompt the user
    while True:
        # clear screen
        os.system("clear")
        print("\nSelect a shape to Draw:")
        print("1. Square")
        print("2. Circle")
        print("3. Triangle")
        print("4. Exit")

        # prompt the user
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            size = int(input("Enter the Size of the Square: "))
            drawSquare(size)
        elif choice == "2":
            size = int(input("Enter the Radius of the Circle: "))
            drawCircle(size)
        elif choice == "3":
            size = int(input("Enter the Size of the Triangle: "))
            drawTriangle(size)
        elif choice == "4":
            print("Exiting the program. Later!")
            # close the turtle screen
            turtle.bye()
            break

        # catch errors
        else:
            print("Invalid choice, please try again...")


# run the app
drawShape()

# complete drawing
#turtle.done()