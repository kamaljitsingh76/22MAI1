import matplotlib.pyplot as plt

# Data labels, sizes, and colors are defined:
labels = 'Broccoli', 'Chocolate Cake', 'Blueberries', 'Raspberries'
sizes = [30, 330, 245, 210]
colors = ['green', 'brown', 'blue', 'red']

# Data is plotted:
plt.pie(sizes, labels=labels, colors=colors)

plt.axis('equal')
plt.title("Pie Plot")
plt.show()