# program that read in a string and strips any leading or trailing spaces.
# The program will also convert the string to lower case and output the length of the input and output strings.
# Author: Sam Tracey; Date: 04-FEB-2021

rawString = input("please enter a string:")
normalisedString = rawString.strip().lower()
lenghtOfRawString = len(rawString)
lenghtOfNormalised = len(normalisedString)


print("That String normalised is :{}".format(normalisedString))
print("we reduced the input string from {} to {} characters".format(
lenghtOfRawString, lenghtOfNormalised))
