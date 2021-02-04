# prompt the user to enter two numbers and then divides the first one by the second one
# the output result should be the integer and the remainder
# Author: Sam Tracey; Date: 04-FEB-2021

# input reads in a string so we have to use int to convert it.
# this allows us to perform mathematical operations on the variables input.

x = int(input("Enter first number: "))
y = int(input("Enter the number you want to divide by: "))

# we use the floor operator (//) to get the integer part and the modulus operator (%) to get the remainder part.
floor = (x // y)
remainder = (x % y)

print("{} divided by {} is {} with remainder {}".format( x, y, floor, remainder))
