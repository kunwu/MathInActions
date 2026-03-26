import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.sans-serif"] = ["PingFang SC", "Arial Unicode MS", "STHeiti"]
plt.rcParams["axes.unicode_minus"] = False


# Define the function
def parabola(x):
    return x**2 - 4 * x + 3


# Generate x values from -1 to 5
x = np.linspace(-1, 5, 400)
y = parabola(x)

# Plot the parabola
plt.figure(figsize=(8, 6))
plt.plot(x, y, "b-", linewidth=2, label="y = x² - 4x + 3")
plt.axhline(y=0, color="k", linestyle="-", linewidth=0.5)
plt.axvline(x=0, color="k", linestyle="-", linewidth=0.5)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Parabola: y = x² - 4x + 3")
plt.grid(True, alpha=0.3)
plt.legend()

# Find and mark the vertex
x_vertex = 2  # For ax² + bx + c, vertex at x = -b/(2a) = -(-4)/(2*1) = 2
y_vertex = parabola(x_vertex)
plt.plot(
    x_vertex, y_vertex, "ro", markersize=8, label=f"Vertex: ({x_vertex}, {y_vertex})"
)

# Find and mark the roots (where y = 0)
# x² - 4x + 3 = 0
# (x-1)(x-3) = 0
# x = 1 or x = 3
roots = [1, 3]
plt.plot(roots, [0, 0], "go", markersize=8, label=f"Roots: {roots}")

plt.legend()
plt.tight_layout()
plt.savefig("parabola_plot.png", dpi=150, bbox_inches="tight")
print("Plot saved as 'parabola_plot.png'")
print(f"Vertex: ({x_vertex}, {y_vertex})")
print(f"Roots: x = {roots[0]}, x = {roots[1]}")
