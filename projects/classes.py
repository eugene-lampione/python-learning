# Clear Screen
import os
os.system("clear")

# Define a class
# Python ignores the self parameter, it is just a convention
class Square:
    def __init__(self, side_length):
        # define square side length
        self.side_length = side_length

    # Get the Area
    def area(self):
        return(self.side_length * self.side_length)

    # get perimeter
    def perimeter(self):
        return(self.side_length * 4)

    def report(self):
        print(f'Side Length: {self.side_length}\n')
        print(f'Area: {self.area()}\n')
        print(f'Perimeter: {self.perimeter()}\n')

# Instantiate the class
my_square = Square(10)

# print stuff
#print(my_square.area())
#print(my_square.perimeter())
my_square.report()