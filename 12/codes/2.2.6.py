# code by A.Chaitanya
from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np

output = Path(__file__).resolve().parent.parent / "figs" / "2.2.6.png"
output.parent.mkdir(parents=True, exist_ok=True)

# Draw the circle and shade the circular cap above y = 1.
theta = np.linspace(0, 2 * np.pi, 800)
y_cap = np.linspace(1, 3, 500)
x_cap = np.sqrt(9 - y_cap**2)

fig, ax = plt.subplots(figsize=(5.4, 4.0))
ax.fill_betweenx(y_cap, -x_cap, x_cap, color="cornflowerblue", alpha=0.35,
                 label="Shaded cap")
ax.plot(3 * np.cos(theta), 3 * np.sin(theta), color="navy", linewidth=1.7,
        label=r"$x^2+y^2=9$")
ax.plot([-np.sqrt(8), np.sqrt(8)], [1, 1], color="darkorange", linewidth=1.5,
        label=r"$y=1$")
ax.axhline(0, color="black", linewidth=0.6)
ax.axvline(0, color="black", linewidth=0.6)
ax.set_aspect("equal", adjustable="box")
ax.set(xlim=(-3.4, 3.4), ylim=(-3.4, 3.4), xlabel="$x$", ylabel="$y$",
       title="Circular cap above $y=1$")
ax.grid(alpha=0.25)
ax.legend(loc="lower left")
fig.tight_layout()
fig.savefig(output, dpi=220)
plt.close(fig)

try:
    import cvxpy as cp
except ModuleNotFoundError:
    print(f"Saved diagram to {output}")
    print("Install CVXPY to run the numerical optimization: python3 -m pip install cvxpy")
    sys.exit(0)

# Use midpoint horizontal slices. The optimization chooses the greatest
# feasible width in each slice, subject to the circle's boundary.
n = 2000
dy = 2 / n
y_mid = 1 + (np.arange(n) + 0.5) * dy
max_width = 2 * np.sqrt(9 - y_mid**2)
width = cp.Variable(n, nonneg=True)
problem = cp.Problem(cp.Maximize(dy * cp.sum(width)), [width <= max_width])
problem.solve()

if problem.status not in (cp.OPTIMAL, cp.OPTIMAL_INACCURATE):
    raise RuntimeError(f"CVXPY did not find an optimum: {problem.status}")

# Numerically approximate all four choices to identify the matching one.
def midpoint_integral(lower, upper, integrand, count=n):
    step = (upper - lower) / count
    points = lower + (np.arange(count) + 0.5) * step
    return step * np.sum(integrand(points))


option_areas = {
    "a)": midpoint_integral(1, 3, lambda y: np.sqrt(9 - y**2)),
    "b)": midpoint_integral(1, 3, lambda y: 2 * np.sqrt(9 - y**2)),
    "c)": midpoint_integral(0, 3, lambda x: np.sqrt(9 - x**2)),
    "d)": midpoint_integral(0, 3, lambda x: 2 * np.sqrt(9 - x**2)),
}
answer = min(option_areas, key=lambda option: abs(option_areas[option] - problem.value))
print(f"CVXPY midpoint-slice area = {problem.value:.6f}")
print(f"Closest listed integral: {answer} (area approximately {option_areas[answer]:.6f})")
print(f"Saved diagram to {output}")
