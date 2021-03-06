# Week 08 Task. Write a program that displays a plot of the functions f(x) = x, g(x)=x^2, h(x)=x^3
# Author: Sam Tracey


import matplotlib.pyplot as plt
import numpy as np


# define x points as a numpy array containing the values (0, 1, 2, 3)
xpoints = np.array(range(0,4))

# Use numpy's operational array capabilities to calculate x squared and x cubed.
ypoints = xpoints **2
zpoints = xpoints **3

# define characteristics of the graph (line styles, line colours, axis titles, legend etc.)

plt.plot(xpoints, '*-r', label = 'f(x)=x') 
# code for adding superscript labels found at https://stackoverflow.com/questions/21226868/superscript-in-python-plots            
plt.plot(ypoints, '+--b', label = 'g(x)=$x^2$' )        
plt.plot(zpoints, 'D-.g', label = 'h(x)=$x^3$')
plt.title('Week 08 Weekly Task', fontname = 'Calibri', fontweight = 'bold', fontsize = '20')
plt.ylabel("Transformed x value")
plt.xlabel("x Value")
# I decided to only use y axis grid as the graph was too noisy with both x & y axis grids added.
plt.grid(axis = 'y')
plt.legend()

# Displaying the plot on screen and saving a copy to the current directory.
plt.savefig('Week08Plot.png')
plt.show()

# References:
# https://realpython.com/python-matplotlib-guide/
# https://matplotlib.org/2.0.2/users/pyplot_tutorial.html
# https://www.w3schools.com/python/matplotlib_plotting.asp
