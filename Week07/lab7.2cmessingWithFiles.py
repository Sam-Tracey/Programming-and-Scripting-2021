# Lab 7.2c Combine previous functions to count how many times a program has been run
# Author: Sam Tracey

import os


def readNumber():
    try:   
        with open(filename) as f:
            number = int(f.read())
            return number
    except IOError:
        # This file is created when we write back
        # no file assumes first time running
        # ie zero previous runs
        return 0

def writeNumber(number):
    with open(filename, "wt") as f:
        # write only takes in string data types so we must convert it with str
        f.write(str(number))


def createFile(obj):
    f = open(filename, "x")



# main program
# rather than a fixed filename prompt user to enter the name of the file
filename = input("Enter file name: ")
# if the filename does not exist in the directory, warn the user, create the file and initialise it to 0.
if not os.path.isfile(filename):
    print ("File does not exist")
    createFile(filename)
    # initialising file to 0
    writeNumber(0)
num = readNumber()
num +=1
print ("We have run this program {} times".format(num))
writeNumber(num)