# Generates a list of 10 random numbers then extract the numbers from the list one at a time and print the remaining numbers
# Author: Sam Tracey

import random
randomList = random.sample(range(0,101), 10)                                                # define the list randomList as a list of 10 random numbers between 0 and 101
print ("Queue is ", randomList)
while len(randomList) != 0:                                                                 # loop while the list randomList is not empty.
    removedValue = randomList.pop()                                                         # extract first element from list and assign to variable removedValue
    print ("current number is: ", removedValue, " and the queue is ", randomList)

print ("The queue is now empty")