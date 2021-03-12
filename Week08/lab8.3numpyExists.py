# Lab topic week 08. Plotting. Question 3
# Author: Sam Tracey

import numpy as np
# setting the seed to ensure the random numbers generated are the same each time. Useful for debugging
np.random.seed(1)

# salaries = np.random.randint(20000, 80001, 10)

# declaring variables to be used in the randint function - more flexible
minSalary = 20000
maxSalary = 80000
numberOfEntries = 10



salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)

# creating a new array with a 5000 increases to the original salaries - highlights numpy's matrix operations
salariesPlus = salaries + 5000

salariesPercent = salaries + (salaries * 0.05)

print(salaries)
print(salariesPlus)
print(salariesPercent)