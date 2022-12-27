import matplotlib.pyplot as plt

fig = plt.figure()

# [left, bottom, width, height]
ax = plt.axes([0.1, 0.1, 0.8, 0.8])

#[left, bottom, width, height]
# ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax.legend(labels = ('label1', 'label2'), loc = 'upper left')


plt.show()