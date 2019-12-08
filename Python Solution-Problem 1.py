# Import libraries
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 100).tolist()
y = np.array([])

for i in range(0, 10):
    result = x[i] ** 2 - 7
    y = np.append(y, result)

y = np.append(y, np.zeros(90))

for i in range(10, 100):
    y[i] = y[i-10]

plt.stem(x, y)
plt.xlabel('n')
plt.ylabel('f(n)')
plt.title('Stem plot of the function')
plt.show()
