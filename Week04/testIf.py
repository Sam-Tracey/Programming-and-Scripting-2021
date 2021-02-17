# program to show the format of an if statement
# Author: Sam Tracey


if False:
    # statements
    print("condition is true")
b = 3
if b == 2:
    print("b is equal to 2")
else:
    print("b is not equal to 2")


a = 2
if a != 2:
    print("I hope this is not displayed")
else:
    print("2 is not equal to 2 is false")

aNumber = 5
if(aNumber % 2) == 0:
    print (aNumber, " is even")
elif (aNumber % 3) == 0:
    print (aNumber, " is divisable by 3")
else:
    print (aNumber, " is not even or divisable by 3")

print ("This will always be output")
