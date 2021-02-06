# This program asks for a float number and then returns an integer value rounded down
# Author: Sam Tracey

# The math module is required for this program
import math

floatNumber = float(input("Enter a Float number:-"))
print("{} floored is {}".format(floatNumber, math.floor(floatNumber)))