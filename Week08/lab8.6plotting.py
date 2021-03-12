# Lab topic week 08. Plotting. Question 6
# Author: Sam Tracey

import matplotlib.pyplot as plt
import numpy as np

# salaries = np.random.randint(20000, 80001, 10)

minSalary = 20000
maxSalary = 80000
numberOfEntries = 10

salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
print(salaries)

plt.hist(salaries)
plt.show()