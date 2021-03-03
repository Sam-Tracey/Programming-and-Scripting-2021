# This program asks for the user to enter a string.
# The string is then reversed and every second letter printed out on screen
# Author: Sam Tracey

userString = input("Please enter a string: ")       # Ask user to enter a string value.
reverseString = userString[::-1]                    # reverse using slice backwards and store in reverseString variable
print(reverseString[::2])                           # print out every other letter