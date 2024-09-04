#2. Write a python program to implement linear regression.

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
np.random.seed(0)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)
# Create and fit the model
model = LinearRegression()
model.fit(X, y)
# Predict and evaluate
y_pred = model.predict(X)
mse = mean_squared_error(y, y_pred)
# Plot
plt.scatter(X, y, color='blue', label='Data')
plt.plot(X, y_pred, color='red', linewidth=2, label='Regression Line')
plt.xlabel('X')
plt.ylabel('y')
plt.title(f'Linear Regression (MSE = {mse:.2f})')
plt.legend()
plt.show()
