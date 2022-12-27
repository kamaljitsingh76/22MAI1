import matplotlib.pyplot as plt
import numpy as np

X = np.linspace(-np.pi, np.pi, 15)
C = np.cos(X)
S = np.sin(X)

# [left, bottom, width, height]
ax = plt.axes([0.1, 0.1, 0.8, 0.8])

# 'bs:' mentions blue color, square
# marker with dotted line.
ax1 = ax.plot(X, C, 'bs:')

# 'ro-' mentions red color, circle
# marker with solid line.
ax2 = ax.plot(X, S, 'ro-')

ax.legend(labels=('Cosine Function', 'Sine Function'), loc='upper left')

ax.set_title("Trigonometric Functions")

plt.show()
