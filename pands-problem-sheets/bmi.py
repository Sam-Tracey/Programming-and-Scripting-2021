# bmi.py
# this code calculates a person's BMI or Body Mass Index
# Author: Sam Tracey.

weight = int(input ("Please enter your weight in Kgs: "))
height = int(input ("Please enter your height in Cm: "))

# calculation used for BMI = weight divided by their height squared

bmi = weight / ((height/100)**2)


# rounding the output to the required number of decimal places and outputting the answer on screen
print("BMI is " + str(round((bmi),2)))