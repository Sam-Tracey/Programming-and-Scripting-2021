# messing with Ands and Ors
# Author: Sam Tracey

number = 120
if (number >=0) and (number <= 100):
    print("ok")


if (number <= 0) or (number >=100):
    isBad = True
    print("Stop")
else:
    isBad = False
    print ("Go")