# Programming and Scripting Module 2021.

# 

# Problem Set Solutions

# 

# Name: Sam Tracey

# 

# Student ID: G00398245

This repository contains solutions to the Problem Sets for the programming and
scripting module.

**Weekly Task 1**

Write a program that calculates somebody's Body Mass Index (BMI). Call the file
bmi.py

The inputs are the person's height in centimetres and weight in kilograms.

The output is their weight divided by their height in metres squared.

\$ python bmi.py

Enter weight: 65

Enter height: 180

BMI is 20.06.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# bmi.py
# this code calculates a person's BMI or Body Mass Index
# Author: Sam Tracey.

weight = int(input ("Please enter your weight in Kgs: "))
height = int(input ("Please enter your height in Cm: "))

# calculation used for BMI = weight divided by their height squared

bmi = weight / ((height/100)**2)

# rounding the output to the required number of decimal places and outputting the answer on screen
# Reference for round() function: https://www.w3schools.com/python/ref_func_round.asp
print("BMI is " + str(round((bmi),2)))
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Reference: <https://www.w3schools.com/python/ref_func_round.asp>

**Weekly Task 2**

Write a program that takes asks a user to input a string and outputs every
second letter in reverse order.

\$ python secondstring.py

Please enter a sentence: The quick brown fox jumps over the lazy dog.

.o zletrv pu o wr cu h

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This program asks for the user to enter a string.
# The string is then reversed and every second letter printed out on screen
# Author: Sam Tracey

userString = input("Please enter a string: ")       # Ask user to enter a string value.
reverseString = userString[::-1]                    # reverse using slice backwards and store in reverseString variable
print(reverseString[::2])                           # print out every other letter

# References:
# https://www.w3schools.com/python/python_howto_reverse_string.asp (reversing a string)
# https://www.w3schools.com/python/gloss_python_string_slice.asp (Indexing and slicing strings)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Weekly Task 3**

Write a program that asks the user to input any positive integer and outputs the
successive values of the following calculation.

At each step calculate the next value by taking the current value and, if it is
even, divide it by two, but if it is odd, multiply it by three and add one.

Have the program end if the current value is one.

\$ python collatz.py

Please enter a positive integer: 10

10 5 16 8 4 2 1

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Weekly task 4
# Program asks the user to input a positive number.
# if the value entered is positive it is divided by 2.
# if the value is negative it is multiplied by 3 and one is added.
# the result from each calculation is appended to a list and once the calculation returs 1, the list is printed out.
# Author: Sam Tracey

list = []                                                       # define an empty list called list

userInput = int(input("Please enter a positive number "))       # ask the user to enter a positive number

while userInput != 1:                                           # counter controlled loop which will repeat until the value of userInput = 1
    list.append(userInput)                                      # append the value of userInput to the list
    if (userInput % 2 == 0):                                    # for loop to check whether the value of userInput is positive or negative
        userInput = int(userInput / 2)                          # if positive userInput is declared as userInput divided by 2
    else:
        userInput = int(userInput * 3 + 1)                      # if negative, userInput is declared as userInput * 3 + 1
        

print(*list, sep=" ")                                           # found this on stack overflow, handy way to print the contents of a list without the brackets.

# References:
# http://introtopython.org/while_input.html (appending list with user input)
# https://stackoverflow.com/questions/11178061/print-list-without-brackets-in-a-single-row
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Weekly Task 5**

Weekly Task 05

Write a program that outputs whether or not today is a weekday.

(You will need to search the web to find how you work out what day it is)

An example of running this program on a Thursday is given below.

\$ python weekday.py

Yes, unfortunately today is a weekday.

An example of running it on a Saturday is as follows:

\$ python weekday.py

It is the weekend, yay!

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




 datetime  date                                               

today = date.today()                                                    
weekDay = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")      

 today in weekDay:                                                    
    print("Yes, unfortunately today is a weekday")                      
:
    print("It is the weekend, yay!")                                    
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Weekly Task 6**

Write a program that takes a positive floating-point number as input and outputs
an approximation of its square root.

You should create a function called \<tt\>sqrt\</tt\> that does this.

I am asking you to create your own sqrt function and not to use the built in
functions x \*\* .5 or math.sqrt(x).

This is to demonstrate that you can research and code a process (If you really
needed the square root you would use one of the above methods).

I suggest that you look at the newton method at estimating square roots.

This is a more difficult task than some of the others, but will be marked
equally, so only do as much work on this as you feel comfortable.

\$ python squareroot.py

Please enter a positive number: 14.5

The square root of 14.5 is approx. 3.8.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This program takes in a positive floating-point number and outputs an approximation of its square root.
# The object is to define our own fucntion for calculating the square root and not to use one of the built-in functions.
# Author: Sam Tracey

def sqrt(num, error= 0.0000001):
    estimate = num
    # arbritary large value for the variable diff (difference) this will get much smaller as we iterate through the loop
    # keep looping while the variable diff is greater than the error value stipulated in arg 2 of the function
    diff = 9999999999                                                      
    while diff > error:                                                     .
        
        # Based on Newton's method formula (found at https://pages.mtu.edu/~shene/COURSES/cs201/NOTES/chap06/sqrt-1.html )
        newEstimate = estimate - ((estimate**2 - num) / (2*estimate))

        # There is a potential for a negative value here so use ABS to ensure diff remains positive
        diff = abs(newEstimate - estimate)
        estimate = newEstimate
    return estimate

# Assign value entered by user as variable userNumber
# Error checking - ensure number entered is positive.
userNumber = float(input("Please enter a positive number: "))             
while userNumber < 0:                                                       
    userNumber = float(input("Please enter a positive number: "))

# Call the function passing in userNumber which was input by the user as an argument
rootNumber = sqrt(userNumber)
print("The sqaure root of {} is approximately {}".format(userNumber, rootNumber))

# References:
# https://pages.mtu.edu/~shene/COURSES/cs201/NOTES/chap06/sqrt-1.html
# https://www.youtube.com/watch?v=tUFzOLDuvaE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Weekly Task 7**

Write a program that reads in a text file and outputs the number of e's it
contains.

The program should take the filename from an argument on the command line.

\$ python es.py moby-dick.txt

116960

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# A program that reads in a text file based on an argument on the command line and counts the number of "e's" in it.
# When running this script the user must add the filename moby.txt in the command lines
# python es.py moby.txt
# Author: Sam Tracey

import sys

# This function takes as arguments the filename specified by the user and the letter which is to be counted

def letterCount (fileName, letter):
    # opening the file as read only, assign the file as a variable text and then convert all the letters to lower case
    # This allows us to count all the e's whether they are upper or lower case.
    # Code for converting all letters to lower case found at https://stackoverflow.com/questions/14067267/lower-case-from-a-text-file/37497605
    file = open(fileName, "r")
    text = file.read()
    textLowerCase = text.lower()
    return textLowerCase.count(letter)



# Ensure that the user enters an argument to specify the text file at the command prompt
if len(sys.argv) != 2:
    print ("Please provide filename in command line prompt")
else:
    fileName = sys.argv[1]
    # Testing to make sure that the correct argument is assigned to the variable
    # print("Book title is: ", fileName)

    print (letterCount(fileName, 'e'))

# References: 
# https://www.knowledgehut.com/blog/programming/sys-argv-python-examples
# https://stackoverflow.com/questions/14067267/lower-case-from-a-text-file/37497605
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Weekly Task 8**

Write a program called plottask.py that displays a plot of the functions f(x)=x,
g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.

Some marks will be given for making the plot look nice.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Week 08 Task. Write a program that displays a plot of the functions f(x) = x, g(x)=x^2, h(x)=x^3
# Author: Sam Tracey

import matplotlib.pyplot as plt
import numpy as np

# define x points as a numpy array containing the values (0, 1, 2, 3)
xpoints = np.array(range(0,4))

# Use numpy's operational array capabilities to calculate x squared and x cubed.
ypoints = xpoints **2
zpoints = xpoints **3

# define characteristics of the graph (line styles, line colours, axis titles, legend etc.)

plt.plot(xpoints, '*-r', label = 'f(x)=x') 
# code for adding superscript labels found at https://stackoverflow.com/questions/21226868/superscript-in-python-plots            
plt.plot(ypoints, '+--b', label = 'g(x)=$x^2$' )        
plt.plot(zpoints, 'D-.g', label = 'h(x)=$x^3$')
plt.title('Week 08 Weekly Task', fontname = 'Calibri', fontweight = 'bold', fontsize = '20')
plt.ylabel("Transformed x value")
plt.xlabel("x Value")
# I decided to only use y axis grid as the graph was too noisy with both x & y axis grids added.
plt.grid(axis = 'y')
plt.legend()

# Displaying the plot on screen and saving a copy to the current directory.
plt.savefig('Week08Plot.png')
plt.show()

# References:
# https://realpython.com/python-matplotlib-guide/
# https://matplotlib.org/2.0.2/users/pyplot_tutorial.html
# https://www.w3schools.com/python/matplotlib_plotting.asp
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

![Chart, line chart Description automatically
generated](media/19ecfbb551460b240e3da369e20cd1b9.png)
