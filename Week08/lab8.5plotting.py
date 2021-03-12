# Lab topic week 08. Plotting. Question 5
# Author: Sam Tracey

import matplotlib.pyplot as plt
import numpy as np

# define xpoints as a numpy array with values of 1 to 100
# define ypoints as xpoint squared
xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints

plt.plot(xpoints, ypoints)
plt.show()
