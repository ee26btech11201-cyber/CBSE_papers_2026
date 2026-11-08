# code by A.Chaitanya
from pathlib import Path

import cvxpy as cp
import matplotlib.pyplot as plt
import numpy as np

from CoordGeo.line.funcs import line_gen
from CoordGeo.plotting.funcs import label_pts

# Solve the linear program with CVXPY.
x_var = cp.Variable(nonneg=True, name="x")
y_var = cp.Variable(nonneg=True, name="y")
constraints = [
    x_var + 2 * y_var <= 12,
    4 * x_var + 5 * y_var >= 20,
    2 * x_var + y_var <= 12,
]
problem = cp.Problem(cp.Maximize(600 * x_var + 400 * y_var), constraints)
problem.solve()

if problem.status not in (cp.OPTIMAL, cp.OPTIMAL_INACCURATE):
    raise RuntimeError(f"CVXPY could not solve the problem: {problem.status}")

x_opt = float(x_var.value)
y_opt = float(y_var.value)
print(f"CVXPY optimum: (x, y) = ({x_opt:.6f}, {y_opt:.6f})")
print(f"Maximum Z = {problem.value:.6f}")

# Plot the constraints, feasible vertices, and CVXPY's computed optimum.
lines = [
    (np.array([12.0, 0.0]), np.array([0.0, 6.0]), r"$x+2y=12$"),
    (np.array([5.0, 0.0]), np.array([0.0, 4.0]), r"$4x+5y=20$"),
    (np.array([6.0, 0.0]), np.array([0.0, 12.0]), r"$2x+y=12$"),
]
vertices = np.array([[0, 4], [0, 6], [4, 4], [6, 0], [5, 0]], dtype=float)
vertex_labels = ["A", "B", "C", "D", "E"]

fig, ax = plt.subplots(figsize=(6.2, 4.4))
for point_a, point_b, label in lines:
    line_points = line_gen(point_a, point_b)
    ax.plot(line_points[0], line_points[1], label=label)

ax.fill(vertices[:, 0], vertices[:, 1], color="gold", alpha=0.22,
        label="Feasible region")
ax.scatter(vertices[:, 0], vertices[:, 1], color="black", s=18, zorder=3)
label_pts(vertices.T, vertex_labels)
ax.scatter([x_opt], [y_opt], color="crimson", marker="*", s=150,
           edgecolor="black", zorder=4, label="CVXPY optimum")
ax.set(xlim=(-0.5, 7), ylim=(-0.5, 7), xlabel="$x$", ylabel="$y$",
       title=rf"Linear program optimum $( {x_opt:.0f}, {y_opt:.0f} )$")
ax.grid(alpha=0.25)
ax.legend(fontsize=8, loc="upper right")
fig.tight_layout()

output = Path(__file__).resolve().parent.parent / "figs" / "2.2.13.png"
fig.savefig(output, dpi=220)
plt.close(fig)
