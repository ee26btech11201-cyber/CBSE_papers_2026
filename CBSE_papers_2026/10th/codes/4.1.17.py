"""Draw the arc and calculate its central angle for Question 4.1.17."""
from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from CoordGeo.conics.funcs import circ_gen
from CoordGeo.line.funcs import line_gen

radius = 6.3
arc_length = 11.0
theta = np.degrees(arc_length / radius)  # s = r*theta, with theta in radians
O = np.array([[0.0], [0.0]])
P = np.array([[radius], [0.0]])
Q = radius * np.array([[np.cos(np.deg2rad(theta))], [np.sin(np.deg2rad(theta))]])
circle = circ_gen(O, radius)
arc_angles = np.linspace(0, np.deg2rad(theta), 200)

fig, ax = plt.subplots(figsize=(5.3, 4.7))
ax.plot(circle[0], circle[1], color="steelblue", alpha=.55)
ax.plot(radius * np.cos(arc_angles), radius * np.sin(arc_angles), color="darkorange", lw=3, label="Arc PQ = 11 cm")
ax.plot(*line_gen(O, P), color="gray", ls="--")
ax.plot(*line_gen(O, Q), color="gray", ls="--")
ax.scatter([0, P[0, 0], Q[0, 0]], [0, 0, Q[1, 0]], color="crimson", zorder=3)
ax.annotate("O", (0, 0), xytext=(-12, -14), textcoords="offset points")
ax.annotate("P", (P[0, 0], 0), xytext=(5, -14), textcoords="offset points")
ax.annotate("Q", (Q[0, 0], Q[1, 0]), xytext=(5, 5), textcoords="offset points")
ax.text(.4, .55, rf"$\theta={theta:.0f}^\circ$")
ax.set_title("Central angle subtended by arc PQ")
ax.set_aspect("equal", adjustable="box")
ax.set_xlim(-7.2, 7.8); ax.set_ylim(-1, 7.3)
ax.grid(alpha=.25); ax.legend(loc="lower left")
fig.tight_layout()

print(f"theta = s/r = {arc_length}/{radius} radians = {theta:.1f} degrees")
out = Path(__file__).resolve().parent.parent / "figs" / "4.1.17.png"
fig.savefig(out, dpi=300, bbox_inches="tight")
print(f"Figure saved to {out}")
