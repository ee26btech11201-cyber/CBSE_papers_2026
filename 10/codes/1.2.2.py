# code by A.Chaitanya
"""Plot the tangent construction for Question 1.2.2 using CoordGeo."""
from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc

sys.path.insert(0, str(Path(__file__).resolve().parent))
from CoordGeo.conics.funcs import circ_gen
from CoordGeo.line.funcs import line_gen
from CoordGeo.plotting.funcs import label_pts

radius = 3.0
O = np.array([[0.0], [0.0]])
P = np.array([[6.0], [0.0]])
Q = np.array([[1.5], [3.0 * np.sqrt(3.0) / 2.0]])
R = np.array([[1.5], [-3.0 * np.sqrt(3.0) / 2.0]])
points = np.hstack((O, P, Q, R))

fig, ax = plt.subplots(figsize=(5.5, 4.6))
circle = circ_gen(O, radius)
ax.plot(circle[0], circle[1], color="navy", label="Circle")
for start, end, color, label, style in (
    (P, Q, "royalblue", "Tangent PQ", "-"),
    (P, R, "darkorange", "Tangent PR", "-"),
    (O, Q, "gray", "Radii", "--"),
    (O, R, "gray", "_nolegend_", "--"),
):
    segment = line_gen(start, end)
    ax.plot(segment[0], segment[1], color=color, linestyle=style, label=label)

ax.scatter(points[0], points[1], color="crimson", zorder=3)
label_pts(points, ["O", "P", "Q", "R"])
ax.add_patch(Arc((6.0, 0.0), 1.3, 1.3, theta1=150, theta2=210,
                 color="black", linewidth=1.0))
ax.text(4.72, 0.12, r"$60^\circ$", fontsize=9)
ax.text(0.15, 1.05, r"$3$ cm", color="dimgray")
ax.set(xlim=(-3.5, 7.3), ylim=(-4.0, 4.0), xlabel="x (cm)", ylabel="y (cm)",
       title="Two tangents from an external point")
ax.set_aspect("equal", adjustable="box")
ax.grid(alpha=0.25)
ax.legend(fontsize=7, loc="upper left")
fig.tight_layout()
out = Path(__file__).resolve().parent.parent / "figs" / "1.2.2.png"
out.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(out, dpi=300, bbox_inches="tight")
