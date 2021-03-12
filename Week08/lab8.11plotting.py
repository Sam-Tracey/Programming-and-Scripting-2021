# Lab topic week 08. Plotting. Question 11
# Author: Sam Tracey


import numpy as np
import matplotlib.pyplot as plt

possibleCounties = ['Cavan', 'Monaghan', 'Fermanagh', 'Tyrone','Donegal']

counties = np.random.choice(possibleCounties ,p=[0.1, 0.3, 0.2, 0.12, 0.28 ],size=(100))

unique, counts = np.unique(counties, return_counts=True)

plt.pie(counts, labels= unique)
plt.show()

