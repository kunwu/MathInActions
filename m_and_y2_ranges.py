import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.sans-serif"] = ["PingFang SC", "Arial Unicode MS", "STHeiti"]
plt.rcParams["axes.unicode_minus"] = False


def parabola(x):
    return x**2 - 4 * x + 3


def y2_range_for_m(m):
    """计算给定m时y2的范围"""
    x2_min = m - 1
    x2_max = m
    y2_min = min(parabola(x2_min), parabola(x2_max))
    y2_max = max(parabola(x2_min), parabola(x2_max))

    if x2_min < 2 < x2_max:
        y2_min = -1

    return y2_min, y2_max


fig = plt.figure(figsize=(14, 16))
gs = fig.add_gridspec(4, 2, hspace=0.4, wspace=0.25)

ax1 = fig.add_subplot(gs[0, :])
x = np.linspace(-2, 8, 1000)
y = parabola(x)

ax1.plot(x, y, "b-", linewidth=2, label="y = x² - 4x + 3")
ax1.axhline(y=0, color="k", linestyle="-", linewidth=0.5, alpha=0.5)
ax1.axvline(x=0, color="k", linestyle="-", linewidth=0.5, alpha=0.5)

# 标记顶点
ax1.plot(2, -1, "ko", markersize=10, label=f"顶点 (2, -1)")

# 标记对称轴
ax1.axvline(
    x=2, color="purple", linestyle=":", linewidth=2, alpha=0.5, label="对称轴 x=2"
)

# 标记 x1 范围 (-1, 1)
ax1.axvline(x=-1, color="green", linestyle="--", linewidth=2, alpha=0.7)
ax1.axvline(x=1, color="green", linestyle="--", linewidth=2, alpha=0.7)
ax1.fill_between(
    [-1, 1], min(y), max(y), alpha=0.1, color="green", label="x1 ∈ (-1, 1)"
)

# 标记 x2 禁用范围 (3, 5)
ax1.axvline(x=3, color="red", linestyle="--", linewidth=2, alpha=0.7)
ax1.axvline(x=5, color="red", linestyle="--", linewidth=2, alpha=0.7)
ax1.fill_between(
    [3, 5], min(y), max(y), alpha=0.1, color="red", label="禁用 x2 ∈ (3, 5)"
)

ax1.set_xlabel("x", fontsize=12)
ax1.set_ylabel("y", fontsize=12)
ax1.set_title("抛物线 y = x² - 4x + 3", fontsize=14, fontweight="bold")
ax1.grid(True, alpha=0.3)
ax1.legend(loc="upper left", fontsize=10)
ax1.set_xlim(-2, 8)
ax1.set_ylim(-3, 40)

# ===== 图2: m 的有效范围 =====
ax2 = fig.add_subplot(gs[1, :])

# 绘制 m 轴
ax2.axhline(y=1, color="gray", linestyle="-", linewidth=3, alpha=0.5)
ax2.set_xlim(-1, 11)
ax2.set_ylim(0.5, 1.5)

# 有效区域 (0, 3]
ax2.plot([0, 3], [1, 1], "g-", linewidth=15, alpha=0.6, label="有效: m ∈ (0, 3]")
ax2.plot(1.5, 1, "g^", markersize=12)
ax2.plot(0, 1, "ko", markersize=8)
ax2.plot(3, 1, "ko", markersize=8)

# 无效区域 (3, 6)
ax2.plot([3, 6], [1, 1], "r-", linewidth=15, alpha=0.6, label="无效: m ∈ (3, 6)")
ax2.plot(4.5, 1, "rx", markersize=15, markeredgewidth=3)

# 有效区域 [6, +∞)
ax2.plot([6, 10], [1, 1], "g-", linewidth=15, alpha=0.6, label="有效: m ∈ [6, +∞)")
ax2.plot(8, 1, "g^", markersize=12)
ax2.plot(6, 1, "ko", markersize=8)

# 标注
ax2.annotate("m = 0", xy=(0, 1.25), ha="center", fontsize=12, fontweight="bold")
ax2.annotate("m = 3", xy=(3, 1.25), ha="center", fontsize=12, fontweight="bold")
ax2.annotate("m = 6", xy=(6, 1.25), ha="center", fontsize=12, fontweight="bold")

ax2.set_xlabel("m 的取值", fontsize=12)
ax2.set_ylabel("", fontsize=12)
ax2.set_title("m 的有效取值范围: (0, 3] ∪ [6, +∞)", fontsize=14, fontweight="bold")
ax2.set_yticks([])
ax2.legend(loc="upper right", fontsize=10)
ax2.grid(True, alpha=0.3, axis="x")

# ===== 图3: y2 随 m 的变化（当 m ∈ (0, 3]）=====
ax3 = fig.add_subplot(gs[2, 0])

m_values_1 = np.linspace(0.1, 3, 100)
y2_min_list_1 = []
y2_max_list_1 = []

for m in m_values_1:
    y2_min, y2_max = y2_range_for_m(m)
    y2_min_list_1.append(y2_min)
    y2_max_list_1.append(y2_max)

ax3.plot(m_values_1, y2_min_list_1, "b-", linewidth=2, label="y₂ 最小值")
ax3.plot(m_values_1, y2_max_list_1, "r-", linewidth=2, label="y₂ 最大值")
ax3.fill_between(
    m_values_1, y2_min_list_1, y2_max_list_1, alpha=0.2, color="yellow", label="y₂ 范围"
)

# 标注关键点
ax3.plot(0, 0, "go", markersize=8, label="m=0: y₂ ∈ [0, 0]")
ax3.plot(1, -1, "bo", markersize=8, label="m=1: y₂ 最小值=-1")
ax3.plot(2, 0, "ro", markersize=8, label="m=2: y₂ 最大值=0")
ax3.plot(3, 8, "mo", markersize=8, label="m=3: y₂=[0, 8]")

ax3.set_xlabel("m ∈ (0, 3]", fontsize=11)
ax3.set_ylabel("y₂ 的值", fontsize=11)
ax3.set_title("y₂ 的取值范围（m ∈ (0, 3]）", fontsize=12, fontweight="bold")
ax3.grid(True, alpha=0.3)
ax3.legend(loc="upper left", fontsize=8)
ax3.set_xlim(0, 3.2)
ax3.set_ylim(-2, 10)

# ===== 图4: y2 随 m 的变化（当 m ∈ [6, +∞)）=====
ax4 = fig.add_subplot(gs[2, 1])

m_values_2 = np.linspace(6, 10, 100)
y2_min_list_2 = []
y2_max_list_2 = []

for m in m_values_2:
    y2_min, y2_max = y2_range_for_m(m)
    y2_min_list_2.append(y2_min)
    y2_max_list_2.append(y2_max)

ax4.plot(m_values_2, y2_min_list_2, "b-", linewidth=2, label="y₂ 最小值")
ax4.plot(m_values_2, y2_max_list_2, "r-", linewidth=2, label="y₂ 最大值")
ax4.fill_between(
    m_values_2, y2_min_list_2, y2_max_list_2, alpha=0.2, color="yellow", label="y₂ 范围"
)

# 标注关键点
ax4.plot(6, 8, "go", markersize=8, label="m=6: y₂=[8, 18]")
ax4.plot(7, 12, "bo", markersize=8, label="m=7: y₂=[12, 24]")
ax4.plot(10, 24, "ro", markersize=8, label="m=10: y₂=[24, 43]")

ax4.set_xlabel("m ∈ [6, +∞)", fontsize=11)
ax4.set_ylabel("y₂ 的值", fontsize=11)
ax4.set_title("y₂ 的取值范围（m ∈ [6, +∞)）", fontsize=12, fontweight="bold")
ax4.grid(True, alpha=0.3)
ax4.legend(loc="upper left", fontsize=8)
ax4.set_xlim(5.8, 10.2)
ax4.set_ylim(6, 45)

ax5 = fig.add_subplot(gs[3, :])

m_values_3 = np.concatenate([np.linspace(0.1, 3, 50), np.linspace(6, 10, 50)])
x2_min_list = [m - 1 for m in m_values_3]
x2_max_list = [m for m in m_values_3]

color = ["green" if m <= 3 else "blue" for m in m_values_3]
for i, m in enumerate(m_values_3):
    ax5.plot(
        [x2_min_list[i], x2_max_list[i]],
        [i, i],
        color=color[i],
        linewidth=15,
        alpha=0.4,
    )

ax5.plot(0.5, 5, "g^", markersize=10, label="m ∈ (0, 3]: x₂ ∈ (m-1, m)")
ax5.plot(7, 55, "b^", markersize=10, label="m ∈ [6, +∞): x₂ ∈ (m-1, m)")

ax5.axvline(
    x=2, color="purple", linestyle=":", linewidth=2, alpha=0.5, label="顶点 x=2"
)
ax5.axvspan(3, 5, alpha=0.1, color="red", label="禁用 x₂ ∈ (3, 5)")

ax5.set_xlabel("x₂ 的值", fontsize=11)
ax5.set_ylabel("m", fontsize=11)
ax5.set_title("x₂ 的取值范围（x₂ ∈ (m-1, m)）", fontsize=12, fontweight="bold")
ax5.grid(True, alpha=0.3, axis="x")
ax5.legend(loc="upper right", fontsize=9)
ax5.set_xlim(-2, 11)
ax5.set_yticks([0, 25, 50, 75, 100])
ax5.set_yticklabels(["m=0.1", "m≈4.5(禁)", "m=6", "m=8", "m=10"])

plt.suptitle("m、x₂、y₂ 的取值范围分析", fontsize=16, fontweight="bold", y=0.995)
plt.savefig("m_and_x2_y2_ranges.png", dpi=150, bbox_inches="tight")
print("图像已保存为 'm_and_x2_y2_ranges.png'")
print("\n" + "=" * 70)
print("分析结果：")
print("=" * 70)
print("m 的有效取值范围：(0, 3] ∪ [6, +∞)")
print()
print("对应的 x₂ 取值范围：")
print("  • 当 m ∈ (0, 3] 时：x₂ ∈ (m-1, m) ⊂ (-1, 3]")
print("    - 包含顶点 x=2 的区间：当 m > 2 且 m-1 < 2，即 m ∈ (2, 3]")
print("  • 当 m ∈ [6, +∞) 时：x₂ ∈ (m-1, m) ⊂ [5, +∞)")
print()
print("对应的 y₂ 取值范围：")
print("  • 当 m ∈ (0, 3] 时：y₂ ∈ [-1, 8]")
print("    - 最小值：-1（当区间包含 x=2 时）")
print("    - 最大值：8（当 m=3 时，x₂ ∈ (2, 3)）")
print()
print("  • 当 m ∈ [6, +∞) 时：y₂ ∈ [8, +∞)")
print("    - 当 m=6 时：y₂ ∈ [8, 18]")
print("    - 随着 m 增大，y₂ 单调递增")
print("=" * 70)
