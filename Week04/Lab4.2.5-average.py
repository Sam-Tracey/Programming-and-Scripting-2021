# Lab 4.2.5 Keeps reading numbers until the user enters a 0.
# The program will append each number entered to a list and then print out each number and the average of the list when a 0 is entered
# Author: Sam Tracey


numbers = []

number = int(input("Enter a number (0 to quit): "))                     # Get first number

while number !=0:                                                       # check to see if value entered is not a 0
    numbers.append(number)                                              # append value entered to numbers list
    number = int(input("Enter another (0 to quit): "))                  # ask user for another input before returning to conditional while statement to check

for val in numbers:                                                     # loop though the list to print each element
    print (val)

average = float(sum(numbers)) / len (numbers)                           # caluclate average of all elements in numbers list and print out
print ("The average is ", average)