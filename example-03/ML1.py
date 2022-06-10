import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 10)
y = 2 * x + 1

plt.plot(x, y, '-r', label='y=2x+1')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc="upper left")
plt.title("Display y=2+1")
plt.grid()
plt.show()
