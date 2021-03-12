# messing ith Numpy
# Author: Sam Tracey

import numpy as np

# show the difference in regular list and numpy array
listOfNumbers = [1,2,4,5]
numbers = np.array([1,2,4,5])

# listOfNumbers = listOfNumbers + 3 - doesn't work

numbers = numbers * np.array([1,4,7,8])
print (numbers)
print(listOfNumbers)


randomNumbers = np.random.normal(5, 1.5, 200)
print (randomNumbers)