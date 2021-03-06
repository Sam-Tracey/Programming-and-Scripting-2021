# Lab 7.2b write a funtion that takes in a number and overwrites a files with that number
# Author: Sam Tracey

filename = "count.txt"

def writeNumber(number):
    with open(filename, "wt") as f:
        # write only takes in string data types so we must convert it with str
        f.write(str(number))

writeNumber(3)
