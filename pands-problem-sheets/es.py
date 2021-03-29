# A program that reads in a text file based on an argument on the command line and counts the number of "e's" in it.
# Author: Sam Tracey


import sys

# This function takes as arguments the filename specified by the user and the letter which is to be counted

def letterCount (fileName, letter):
    # opening the file as read only, assign the file as a variable text and then convert all the letters to lower case
    # This allows us to count all the e's whether they are upper or lower case.
    file = open(fileName, "r")
    text = file.read()
    textLowerCase = text.lower()
    return textLowerCase.count(letter)




# Ensure that the user enters an argument to specify the text file at the command prompt
if len(sys.argv) != 2:
    print ("Please provide filename in command line prompt")
else:
    fileName = sys.argv[1]
    # Testing to make sure that the correct argument is assigned to the variable
    # print("Book title is: ", fileName)

    print (letterCount(fileName, 'e'))