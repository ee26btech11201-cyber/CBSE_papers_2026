from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from CoordGeo.line.funcs import line_gen

# Endpoints of the segment from the question
P = np.array([-4.0, -2.0])
Q = np.array([10.0, 4.0])

# Generate the segment using the CoordGeo line-generation function
segment = line_gen(P, Q)

# The y-axis intersection divides PQ in the ratio 2:5
R = np.array([0.0, -2.0 / 7.0])

fig, ax = plt.subplots(figsize=(7, 5))
ax.plot(segment[0], segment[1], color="royalblue", linewidth=2, label="Segment PQ")
ax.axhline(0, color="black", linewidth=0.8)
ax.axvline(0, color="black", linewidth=1.2, label="y-axis")

ax.scatter(*P, color="darkorange", zorder=3)
ax.scatter(*Q, color="darkorange", zorder=3)
ax.scatter(*R, color="crimson", zorder=4)

ax.annotate(r"$P(-4,-2)$", P, xytext=(-8, -18), textcoords="offset points", ha="right")
ax.annotate(r"$Q(10,4)$", Q, xytext=(7, 5), textcoords="offset points")
ax.annotate(r"$R(0,-\frac{2}{7})$", R, xytext=(8, -18), textcoords="offset points")

ax.set_xlim(-6, 12)
ax.set_ylim(-4, 6)
ax.set_aspect("equal", adjustable="box")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Line segment divided by the y-axis")
ax.grid(True, linestyle=":", alpha=0.7)
ax.legend(loc="upper left")
fig.tight_layout()

output = Path(__file__).resolve().parent.parent / "figs" / "5.1.2.png"
fig.savefig(output, dpi=300, bbox_inches="tight")
