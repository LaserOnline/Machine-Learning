from random import random
import numpy as np
import matplotlib.pyplot as plt

rng = np.random
x = rng.rand(50)*10
y = 2 * x + rng.randn(50)

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.show()

# * y=ax+c
