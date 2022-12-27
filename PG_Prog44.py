import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
xx = x + 1j * x[:, np.newaxis]
out = np.exp(xx)
plt.subplot(121)
plt.imshow(np.abs(out), extent=[-2 * np.pi, 2 * np.pi, -2 * np.pi,
                                2 * np.pi])
plt.title('Magnitude	of	exp(x)')
plt.subplot(122)
plt.imshow(np.angle(out), extent=[-2 * np.pi, 2 * np.pi, -2 * np.
           pi, 2 * np.pi])
plt.title('Phase	(angle)	of	exp(x)')
plt.show()
