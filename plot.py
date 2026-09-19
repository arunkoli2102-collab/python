import matplotlib.pyplot as plt
import numpy as np

X = np.linspace(0, 2 * np.pi, 100)
Y = np.sin(X)

plt.plot(X, Y, label="sin(x)", color="blue", marker="o")

plt.title("Line Plot - Sine Function")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()

plt.show()