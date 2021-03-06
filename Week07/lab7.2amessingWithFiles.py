# Lab 7.2 Create a function that reads in a number from a file that already exists
# Author: Sam Tracey

filename = "count.txt"

def readNumber():
    with open(filename) as f:
        number = int(f.read())
        return number

num= readNumber()
print(num)