# import required modules
import matplotlib.pyplot as plt
import matplotlib.tri as mtri
import numpy as np

# assign data
x = np.asarray([0, 1, 2, 3, 0.5,
                1.5, 2.5, 1, 2,
                1.5])

y = np.asarray([0, 0, 0, 0, 1.0,
                1.0, 1.0, 2, 2,
                3.0])

triangles = [[0, 1, 4], [1, 5, 4],
             [2, 6, 5], [4, 5, 7],
             [5, 6, 8], [5, 8, 7],
             [7, 8, 9], [1, 2, 5],
             [2, 3, 6]]

# depict illustration
triang = mtri.Triangulation(x, y, triangles)
z = np.cos(1.5 * x) * np.cos(1.5 * y)

fig, axs = plt.subplots()
axs.tricontourf(triang, z)
axs.triplot(triang, 'b-', color='white')

# turn off the axes
#axs.set_axis_off()

# assign title
axs.set_title('Triangle illustration')

plt.show()
