# This program asks for an amount to be entered and will return the amount in cent
# Author: Sam Tracey

dollarAmount = float(input("Please enter an amount:- "))    # using a float data type to express decimals which can be +ve or -ve
centAmount = int(abs(dollarAmount*100))                     # calculate the amount in cent, convert it to a +ve value and return an int

print("The amount in cent is: {}".format(centAmount))       # print out the value in cent