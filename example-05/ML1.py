import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
rng = np.random

x = rng.rand(50)*10
y = 2 * x + rng.randn(50)

model = LinearRegression()

x_new = x.reshape(-1, 1)

model.fit(x_new, y)
print(model.score(x_new, y))
