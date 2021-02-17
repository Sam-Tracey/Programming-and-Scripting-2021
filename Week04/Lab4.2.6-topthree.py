# Lab 4.2.6 This program creates 10 random numbers between 0 and 100
# prints them out and then prints out the 3 higest values in the list
# Author: Sam Tracey





import heapq                                    # I got the idea to use the heapq function from stack overflow. It is much neater.
from random import randrange                    # Impor the randrange function to generate random numbers

numbers = []


for iteration in range(1,11):                   # For loop which executes the statments inside 10 times.
    randomNumber = randrange(0,100)
    numbers.append(randomNumber)

print ("Ten random numbers are ", numbers)      # Output the final list and then the largest 3 numbers in the list
print(heapq.nlargest(3, numbers))





