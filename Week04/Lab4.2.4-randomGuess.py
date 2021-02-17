# Lab 4.2.4 prompts the user to enter a number and keep prompting the user until the correct number is entered
# This program uses the randrange function to generate a random number between 1 and 100
# Author: Sam Tracey

from random import randrange                                    # import the randrange function from random module

correctNumber = randrange(1,100)                                # define correctNumber as a random integer between 1 and 100
val = int(input ("Please guess the number: "))                  # ask the user to enter a value
while val != correctNumber:                                     # while loop start
    if val < correctNumber:                                     # check to see if the entered number is lower than the random number and prompt the user accordingly
         print("too low")
    elif val > correctNumber:                                   # check to see if the entered number is higher than the random number and prompt the user accordingly
         print("Too high")
    val = int(input("Please guess again: "))                    # prompt the user to guess again
print ("Well done! Yes the number was", correctNumber)          # only printed out when the user's input matches the random variable.