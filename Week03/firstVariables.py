# messing around with variable types
# Author: Sam Tracey; Date: 04-FEB-2021

ageOfPatient = {}
age = "3"

# we need to convert the type to str so we can concatenate it to the message
print("Type of ageOfPatient is: " + str(type(ageOfPatient)))
print("Type of age is: " + str(type(age)))

# show how you convert str to int and int to str
print ("You are " + str(age))
nextYear = int(age) + 1
print ("Next year you will be " + str (nextYear))