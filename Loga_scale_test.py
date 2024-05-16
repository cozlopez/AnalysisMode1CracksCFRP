
"""
Created on Thu May 16 14:09:37 2024

@author: yannt
"""

import matplotlib.pyplot as plt
import numpy as np

# Generate some data
x = np.linspace(1, 10, 100)
a = 2
b=0
y = a*np.log10(x)+b

# Create a figure and an axes
fig, ax = plt.subplots()

# Plot the data
ax.plot(x, y, label='exp(x)')

# Set the scale of the x and y axes to logarithmic
ax.set_xscale('log', base=10)


# Add labels, title, and legend
ax.set_xlabel('x (log scale)')
ax.set_ylabel('y')
ax.set_title('Exponential Function on Log-Log Scale')
ax.legend()

# Show the plot
plt.show()
