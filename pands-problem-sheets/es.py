# A program that reads in a text file based on an argument on the command line and counts the number of "e's" in it.
# When running this script the user must add the filename moby.txt in the command lines
# python es.py moby.txt
# Author: Sam Tracey


import sys

# This function takes as arguments the filename specified by the user and the letter which is to be counted

def letterCount (fileName, letter):
    # opening the file as read only, assign the file as a variable text and then convert all the letters to lower case
    # This allows us to count all the e's whether they are upper or lower case.
    # Code for converting all letters to lower case found at https://stackoverflow.com/questions/14067267/lower-case-from-a-text-file/37497605
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

# References: 
# https://www.knowledgehut.com/blog/programming/sys-argv-python-examples
# https://stackoverflow.com/questions/14067267/lower-case-from-a-text-file/37497605