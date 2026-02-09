import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return np.sin(x) + np.sin(10 * x / 3)


def hill_climbing(start, step_size=0.1, max_iter=1000):
    x = start
    path = [x]
    for _ in range(max_iter):
        neighbors = [x - step_size, x + step_size]
        neighbors = [n for n in neighbors if 0 <= n <= 10]
        values = [f(n) for n in neighbors]

        max_value = max(values)
        max_index = values.index(max_value)

        if max_value > f(x):
            x = neighbors[max_index]
            path.append(x)
        else:
            break
    return x, path


x_vals = np.linspace(0, 10, 1000)
y_vals = f(x_vals)

hc_start = np.random.uniform(0, 10)
hc_max, hc_path = hill_climbing(hc_start)
hc_y_path = [f(x) for x in hc_path]

plt.figure(figsize=(8, 6))
plt.plot(x_vals, y_vals, label="Objective function f(x)", color="blue")
plt.scatter(hc_path, hc_y_path, color="red", label="Hill Climbing path")
plt.scatter(
    hc_path[0],
    hc_y_path[0],
    color="green",
    s=100,
    label="Start",
    edgecolors="black",
    linewidths=1.5,
)
plt.scatter(
    hc_path[-1],
    hc_y_path[-1],
    color="purple",
    s=100,
    label="End",
    edgecolors="black",
    linewidths=1.5,
)
plt.title(f"Hill Climbing Search\n(start={hc_start:.2f})")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()

print(f"Hill Climbing max at x={hc_max:.4f}, f(x)={f(hc_max):.4f}")