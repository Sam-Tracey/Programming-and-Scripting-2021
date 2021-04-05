# Weekly task 4
# Program asks the user to input a positive number.
# if the value entered is positive it is divided by 2.
# if the value is negative it is multiplied by 3 and one is added.
# the result from each calculation is appended to a list and once the calculation returs 1, the list is printed out.
# Author: Sam Tracey


list = []                                                       # define an empty list called list

userInput = int(input("Please enter a positive number "))       # ask the user to enter a positive number

while userInput != 1:                                           # counter controlled loop which will repeat until the value of userInput = 1
    list.append(userInput)                                      # append the value of userInput to the list
    if (userInput % 2 == 0):                                    # for loop to check whether the value of userInput is positive or negative
        userInput = int(userInput / 2)                          # if positive userInput is declared as userInput divided by 2
    else:
        userInput = int(userInput * 3 + 1)                      # if negative, userInput is declared as userInput * 3 + 1
        


print(*list, sep=" ")                                           # found this on stack overflow, handy way to print the contents of a list without the brackets.


# References:
# http://introtopython.org/while_input.html (appending list with user input)
# https://stackoverflow.com/questions/11178061/print-list-without-brackets-in-a-single-row