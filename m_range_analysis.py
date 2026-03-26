import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.sans-serif"] = ["PingFang SC", "Arial Unicode MS", "STHeiti"]
plt.rcParams["axes.unicode_minus"] = False


# Original parabola
def parabola(x):
    return x**2 - 4 * x + 3


# Generate points
x = np.linspace(-2, 6, 800)
y = parabola(x)

# Create figure with two subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

# ===== Plot 1: Parabola showing forbidden and allowed regions =====
ax1.plot(x, y, "b-", linewidth=2, label="y = x² - 4x + 3")
ax1.axhline(y=0, color="k", linestyle="-", linewidth=0.5, alpha=0.5)
ax1.axvline(x=0, color="k", linestyle="-", linewidth=0.5, alpha=0.5)

# Mark the region x1 ∈ (-1, 1)
x1_vals = np.linspace(-1, 1, 100)
ax1.axvline(x=-1, color="g", linestyle="--", linewidth=2, alpha=0.7)
ax1.axvline(x=1, color="g", linestyle="--", linewidth=2, alpha=0.7)
ax1.fill_between(
    [min(x1_vals), max(x1_vals)],
    min(y),
    max(y),
    alpha=0.1,
    color="green",
    label="x1 ∈ (-1, 1)",
)

# Mark the corresponding x2 = 4 - x1 region (3, 5)
ax1.axvline(x=3, color="r", linestyle="--", linewidth=2, alpha=0.7)
ax1.axvline(x=5, color="r", linestyle="--", linewidth=2, alpha=0.7)
ax1.fill_between(
    [3, 5],
    min(y),
    max(y),
    alpha=0.1,
    color="red",
    label="x2 = 4 - x1, forbidden region",
)

# Mark vertex
ax1.plot(2, -1, "ko", markersize=8, label="Vertex (2, -1)")

# Mark roots
ax1.plot([1, 3], [0, 0], "go", markersize=8, label="Roots (1, 0), (3, 0)")

# Mark symmetry axis
ax1.axvline(
    x=2,
    color="purple",
    linestyle=":",
    linewidth=2,
    alpha=0.5,
    label="Symmetry axis x=2",
)

ax1.set_xlabel("x", fontsize=12)
ax1.set_ylabel("y", fontsize=12)
ax1.set_title(
    "Parabola y = x² - 4x + 3: Regions Analysis", fontsize=14, fontweight="bold"
)
ax1.grid(True, alpha=0.3)
ax1.legend(loc="upper left", fontsize=10)
ax1.set_xlim(-2, 6)
ax1.set_ylim(-2, 10)

# ===== Plot 2: Visualizing m intervals =====
# Draw m intervals
ax2.axhline(y=1, color="gray", linestyle="-", linewidth=20, alpha=0.3)

# Show forbidden m values
ax2.plot([3, 6], [1, 1], "r-", linewidth=20, alpha=0.6, label="Forbidden m ∈ (3, 6)")
ax2.plot(4.5, 1, "rx", markersize=15, markeredgewidth=3)

# Show allowed m values
ax2.plot([0, 3], [1, 1], "g-", linewidth=20, alpha=0.6, label="Allowed m ∈ (0, 3]")
ax2.plot(1.5, 1, "g^", markersize=10)

ax2.plot([6, 10], [1, 1], "g-", linewidth=20, alpha=0.6, label="Allowed m ∈ [6, +∞)")
ax2.plot(8, 1, "g^", markersize=10)

# Add markers
ax2.plot(0, 1, "ko", markersize=8)
ax2.plot(3, 1, "ko", markersize=8)
ax2.plot(6, 1, "ko", markersize=8)

# Annotations
ax2.annotate("m = 0", xy=(0, 1.2), ha="center", fontsize=11)
ax2.annotate("m = 3", xy=(3, 1.2), ha="center", fontsize=11)
ax2.annotate("m = 6", xy=(6, 1.2), ha="center", fontsize=11)
ax2.annotate(
    "FORBIDDEN", xy=(4.5, 0.5), ha="center", fontsize=14, fontweight="bold", color="red"
)
ax2.annotate(
    "ALLOWED", xy=(1.5, 0.5), ha="center", fontsize=14, fontweight="bold", color="green"
)
ax2.annotate(
    "ALLOWED", xy=(8, 0.5), ha="center", fontsize=14, fontweight="bold", color="green"
)

ax2.set_xlabel("m values", fontsize=12)
ax2.set_ylabel("", fontsize=12)
ax2.set_title("Valid Range of m: (0, 3] ∪ [6, +∞)", fontsize=14, fontweight="bold")
ax2.set_xlim(-0.5, 10)
ax2.set_ylim(0, 2)
ax2.set_yticks([])
ax2.legend(loc="upper right", fontsize=10)
ax2.grid(True, alpha=0.3, axis="x")

plt.tight_layout()
plt.savefig("m_range_analysis.png", dpi=150, bbox_inches="tight")
print("Plot saved as 'm_range_analysis.png'")
print("\n" + "=" * 60)
print("SOLUTION:")
print("=" * 60)
print("Given: y = x² - 4x + 3, -1 < x₁ < 1")
print("Find m such that y₁ ≠ y₂ for all x₂ ∈ (m-1, m)")
print("\nAnalysis:")
print("  • Parabola symmetric about x = 2")
print("  • For any x₁, y₁ = y₂ when x₂ = 4 - x₁")
print(f"  • When x₁ ∈ (-1, 1), x₂ ∈ (3, 5)")
print(f"  • To ensure y₁ ≠ y₂, interval (m-1, m) must not intersect (3, 5)")
print(f"\n  • Condition: (m-1, m) ∩ (3, 5) = ∅")
print(f"  • This requires: m ≤ 3 or m - 1 ≥ 5")
print(f"  • Solution: m ≤ 3 or m ≥ 6")
print(f"\nSince m > 0:")
print(f"  Answer: m ∈ (0, 3] ∪ [6, +∞)")
print("=" * 60)
