# Program asks the user to enter a numnber and will output whether the number is even or odd.
# Author: Sam Tracey

number = int(input("Enter a number:"))

if (number % 2) == 0:
    print(number, "is an even number")
else:
    print (number, "is an odd number")