# messing with histograms
# Author: Sam Tracey


import numpy as np
import matplotlib.pyplot as plt

'''
# np.random.seed(1)   # this line ensures your random data is the same each time - handy for debugging
normData = np.random.normal(10, 1.5, size=10000)


plt.hist(normData)
plt.show()

'''

fruit = np.array(["Apples", "Oranges", "Bananas", "Coconut"])
numbers = np.array([22, 77, 18, 41])

plt.pie(numbers, labels = fruit, shadow = True)
plt.show()
