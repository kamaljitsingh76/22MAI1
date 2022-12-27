# Python Program to illustrate Linear Plotting

import matplotlib.pyplot as plt

year = [1972, 1982, 1992, 2002, 2012]
e_india = [100.6, 158.61, 305.54,
           394.96, 724.79]

e_bangladesh = [10.5, 25.21, 58.65,
                119.27, 274.87]

# formatting of line style and
# plotting of co-ordinates
plt.plot(year, e_india, color='orange',
         marker='o', markersize=10,
         label='India')

plt.plot(year, e_bangladesh, color='g',
         linestyle='dashed', linewidth=2,
         label='Bangladesh')

plt.xlabel('Years')
plt.ylabel('Power consumption in kWh')

plt.title('Electricity consumption per \
capita of India and Bangladesh')

plt.legend()
plt.show()
