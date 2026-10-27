"""Draw the tangent configuration and calculate OP for Question 4.1.4."""
from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np

# Load the CoordGeo library stored beside this script.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from CoordGeo.conics.funcs import circ_gen, contact
from CoordGeo.line.funcs import line_gen

radius = 4.0
O = np.array([[0.0], [0.0]])
P = np.array([[4 * np.sqrt(2)], [0.0]])

# The circle is x^T V x + 2u^T x + f = 0.
V = np.eye(2)
u = np.zeros((2, 1))
f = -(radius**2)
Q, R = contact(V, u, f, P)

circle = circ_gen(O, radius)
fig, ax = plt.subplots(figsize=(5.5, 5.0))
ax.plot(circle[0], circle[1], color="navy", label="Circle")
ax.plot(*line_gen(O, Q), "--", color="gray", label="Radii")
ax.plot(*line_gen(O, R), "--", color="gray")
ax.plot(*line_gen(Q, P), color="royalblue", label="Tangents")
ax.plot(*line_gen(R, P), color="royalblue")
ax.scatter([O[0, 0], P[0, 0], Q[0, 0], R[0, 0]],
           [O[1, 0], P[1, 0], Q[1, 0], R[1, 0]], color="crimson", zorder=3)

for point, name, offset in ((O, "O", (-0.35, -0.45)),
                            (P, "P", (0.12, 0.08)),
                            (Q, "Q", (-0.35, -0.4)),
                            (R, "R", (-0.35, 0.15))):
    ax.annotate(name, (point[0, 0], point[1, 0]), xytext=offset,
                textcoords="offset fontsize", fontsize=11)

ax.text(P[0, 0] - 2.45, 0.25, r"$90^\circ$", fontsize=10)
ax.set_title("Two tangents with $\\angle QPR=90^\\circ$")
ax.set_xlabel("x (cm)")
ax.set_ylabel("y (cm)")
ax.set_aspect("equal", adjustable="box")
ax.set_xlim(-5, 7)
ax.set_ylim(-6, 6)
ax.grid(True, alpha=0.35)
ax.legend(loc="upper left", fontsize=8)
fig.tight_layout()

OP = np.linalg.norm(P - O)
print(f"OP = {OP:.3f} cm = 4*sqrt(2) cm")
output = Path(__file__).resolve().parent.parent / "figs" / "4.1.4.png"
fig.savefig(output, dpi=300, bbox_inches="tight")
print(f"Figure saved to {output}")
