# messing with matplotlib
# Author: Sam Tracey


import numpy as np
import matplotlib.pyplot as plt

xpoints = np.array(range(1,101))

ypoints = xpoints * xpoints

plt.plot(xpoints, ypoints, label = "x-squared", color = "red")
plt.plot(xpoints, xpoints, label = "straight", color = "green")
plt.legend()

randompoints = np.random.randint(1, 1000, 100)
plt.scatter(xpoints, randompoints, label = "random", color = "blue")
plt.show()                                      # print plot out on screen
# plt.savefig("First_graph_week08.png")           # save graph to folder


