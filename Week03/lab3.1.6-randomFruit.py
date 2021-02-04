# This program prints out a random fruit
# Author: Sam Tracey; Date 04-FEB-2020

import random                                       # import the random module
fruits = ('Apple', 'Orange', 'Banana', 'Pear')      # assign values to the tuple

# we want a random number between 0 and length-1

index = random.randint(0, len(fruits)-1)
fruit = fruits[index]                               # assign the value in the tuple at position index to the variable fruit
print("A Random Fruit:{}".format(fruit))
