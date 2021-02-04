# program that asks the user to enter a lower bound number and an upper bound number.
# the program then prints out a random number between the user defined lower and upper bounds
# Author: Sam Tracey; Date: 04-FEB-2021

import random

# cnverting the str input to an integer
x = int(input("Please enter the lower boundary: "))
y = int(input("Please enter the upper boundary: "))

# using the randrange method with the user input variables as the start and stop points
number = random.randrange(x, y)

# printing out the random number and the range from which it was chosen
print ("{} is a random number between {} and {}".format(number, x, y))
