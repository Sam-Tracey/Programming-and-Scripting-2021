# This program reads ina string, strips any leading and trailing spaces, converts the string to lower case
# and also outputs the length of the input and output strings.
# Author: Sam Tracey


userInput = input("Please enter a string:")
userStringCount = len(userInput)
spaceRemoved = userInput.strip()
lowerCase = spaceRemoved.lower()
strippedLen = len(lowerCase)

print("That string normalised is: {}".format(lowerCase))
print("We reduced the input string from {} to {} characters".format(userStringCount, strippedLen))