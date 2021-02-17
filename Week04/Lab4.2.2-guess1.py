# Lab 4.2.2 prompts the user to enter a number and keep prompting theuser until the correct number is entered
# Author: Sam Tracey

correctNumber = 30
val = int(input ("Please guess the number: "))
while val != correctNumber:
    if val < correctNumber:
         print("too low")
    elif val > correctNumber:
         print("Too high")
    val = int(input("Please guess again: "))
print ("Well done! Yes the number was", correctNumber)