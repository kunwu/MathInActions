import numpy as np


def parabola(x):
    return x**2 - 4 * x + 3


def geometric_check(m):
    """几何检查：区间(m-1,m)是否与禁用区间(3,5)相交"""
    lower, upper = m - 1, m
    forbidden_lower, forbidden_upper = 3, 5

    if upper <= forbidden_lower or lower >= forbidden_upper:
        return True, "不相交"
    else:
        return (
            False,
            f"相交于 ({max(lower, forbidden_lower):.2f}, {min(upper, forbidden_upper):.2f})",
        )


def detailed_check(m):
    """详细检查：找到具体的x1,x2使得y1=y2"""
    lower, upper = m - 1, m

    for x1 in np.linspace(-0.9, 0.9, 100):
        x2_sym = 4 - x1
        if lower < x2_sym < upper:
            y = parabola(x1)
            return False, x1, x2_sym, y

    return True, None, None, None


print("=" * 70)
print("验证：测试m的取值")
print("=" * 70)

test_cases = [
    (0.5, "应该有效"),
    (2.0, "应该有效"),
    (3.0, "应该有效（边界）"),
    (3.5, "应该无效"),
    (4.0, "应该无效"),
    (4.5, "应该无效"),
    (5.5, "应该无效"),
    (6.0, "应该有效（边界）"),
    (7.0, "应该有效"),
    (10.0, "应该有效"),
]

print(f"{'m值':<10} {'几何检查':<35} {'详细检查':<30} {'预期'}")
print("-" * 100)

for m, expected in test_cases:
    geo_valid, geo_reason = geometric_check(m)
    det_valid, x1, x2, y = detailed_check(m)

    geo_str = "✓" if geo_valid else "✗"
    if not geo_valid:
        geo_display = f"{geo_str} {geo_reason}"
    else:
        geo_display = f"{geo_str} {geo_reason}"

    if not det_valid and x1 is not None:
        det_display = f"✗ 反例: x1={x1:.3f}, x2={x2:.3f}, y={y:.3f}"
    else:
        det_display = f"✓ 无反例"

    print(f"{m:<10.1f} {geo_display:<35} {det_display:<30} {expected}")

print("=" * 70)
print("\n解题过程：")
print("1. 抛物线 y = x² - 4x + 3 关于 x = 2 对称")
print("2. 对任意 x1，存在唯一的 x2 = 4 - x1 使得 y1 = y2")
print("3. 当 x1 ∈ (-1, 1) 时，x2 = 4 - x1 ∈ (3, 5)")
print("4. 要使 y1 ≠ y2 对所有 x2 ∈ (m-1, m)，需要区间 (m-1, m) 与 (3, 5) 不相交")
print("5. 条件：m ≤ 3 或 m - 1 ≥ 5")
print("6. 即：m ≤ 3 或 m ≥ 6")
print("7. 因为 m > 0，所以 m ∈ (0, 3] ∪ [6, +∞)")
print("=" * 70)
print("\n答案：m 的取值范围是 (0, 3] ∪ [6, +∞)")
print("=" * 70)
