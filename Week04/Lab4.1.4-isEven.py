# Program asks the user to enter a numnber and will output whether the number is even or odd.
# Program will only continue if the user enters -1
# Author: Sam Tracey

number = int(input("Enter a number:"))

while number != -1:                                    # use of a while loop to keep prompting the user to enter a number until user enters -1
    number = int(input("Enter a number:"))

if (number % 2) == 0:
    print(number, "is an even number")
else:
    print (number, "is an odd number")