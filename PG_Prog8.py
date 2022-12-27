# importing library
import matplotlib.pyplot as plt

# Some data to display
x = [1, 2, 3]
y = [0, 1, 0]
z = [1, 0, 1]

# Creating 2 subplots
fig, ax = plt.subplots(2)

# Accessing each axes object to plot the data through returned array
ax[0].plot(x, y)
ax[1].plot(x, z)
plt.show()