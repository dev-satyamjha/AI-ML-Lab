import math

import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return np.sin(x) + np.sin(10 * x / 3)


def simulated_annealing(
    start, step_size=0.5, max_iter=1000, initial_temp=10, cooling_rate=0.99
):
    x = start
    path = [x]
    temp = initial_temp

    for _ in range(max_iter):
        candidate = x + np.random.uniform(-step_size, step_size)
        candidate = np.clip(candidate, 0, 10)
        delta = f(candidate) - f(x)

        if delta > 0 or np.random.rand() < math.exp(delta / temp):
            x = candidate
            path.append(x)

        temp *= cooling_rate
        if temp < 1e-3:
            break

    return x, path


x_vals = np.linspace(0, 10, 1000)
y_vals = f(x_vals)

sa_start = np.random.uniform(0, 10)
sa_max, sa_path = simulated_annealing(sa_start)
sa_y_path = [f(x) for x in sa_path]

plt.figure(figsize=(8, 6))
plt.plot(x_vals, y_vals, label="Objective function f(x)", color="blue")
plt.scatter(sa_path, sa_y_path, color="green", label="Simulated Annealing path")
plt.scatter(
    sa_path[0],
    sa_y_path[0],
    color="orange",
    s=100,
    label="Start",
    edgecolors="black",
    linewidths=1.5,
)
plt.scatter(
    sa_path[-1],
    sa_y_path[-1],
    color="purple",
    s=100,
    label="End",
    edgecolors="black",
    linewidths=1.5,
)
plt.title(f"Simulated Annealing Search\n(start={sa_start:.2f})")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()

print(f"Simulated Annealing max at x={sa_max:.4f}, f(x)={f(sa_max):.4f}")