# Lab topic week 08. Plotting. Question 7
# Author: Sam Tracey

import matplotlib.pyplot as plt
import numpy as np

# salaries = np.random.randint(20000, 80001, 10)

minSalary = 20000
maxSalary = 80000
numberOfEntries = 10

minAge = 21
maxAge = 65



salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
ages = np.random.randint(minAge, maxAge, numberOfEntries)

plt.scatter(ages, salaries)


plt.show()
