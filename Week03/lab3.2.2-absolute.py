# This program asks for a number and then returns the absolute value of that number
# Author: Sam Tracey

# I used the data type float as it allows the user to enter decimal or non-decimal
realNumber = float(input("Please enter a number:-"))
absNumber = abs(realNumber)
print("The absolute value of {} is {}".format(realNumber, absNumber))