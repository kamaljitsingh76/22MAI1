# importing library
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
x = np.arange(0.0, 2.0, 0.01)
y = 1 + np.sin(2 * np.pi * x)

# Creating 6 subplots and unpacking the output array immediately
fig, (ax1,ax2,ax3, ax4,ax5) = plt.subplots(5)
ax1.plot(x, y, color="orange")
'''ax2.plot(x, y, color="green")
ax3.plot(x, y, color="blue")
ax4.plot(x, y, color="magenta")
ax5.plot(x, y, color="black")
ax6.plot(x, y, color="red")'''
plt.show()