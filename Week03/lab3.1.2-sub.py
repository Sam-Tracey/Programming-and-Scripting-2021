# prompt the user to enter two numbers and then subtract one from the other.
# Author: Sam Tracey; Date: 04-FEB-2021

# input reads in a string so we have to use int to convert it.
# this allows us to perform mathematical operations on the variables input.

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
answer = x-y

# below is my first attempt without looking at the notes
# print(str(x) + " minus " + str(y) + " is " + str(x-y))

print ("{} minus {} is {} ".format(x, y, answer))