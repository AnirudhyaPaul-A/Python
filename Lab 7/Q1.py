 #1. Write a Python program that computes the value of the Gaussian distribution at a given vector X. Hence, plot the effect of varying mean and variance to the normal distribution.

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
def plot_gaussian(mean, variance):
    x = np.linspace(mean - 4*np.sqrt(variance), mean + 4*np.sqrt(variance),1000)
    y = norm.pdf(x, mean, np.sqrt(variance))
    plt.plot(x, y, label=f'Mean = {mean}, Variance = {variance}')
    plt.xlabel('X')
    plt.ylabel('Probability Density')
    plt.title('Gaussian Distribution')
    plt.legend()
    plt.grid(True)
    plt.show()
plot_gaussian(mean=3, variance=5)