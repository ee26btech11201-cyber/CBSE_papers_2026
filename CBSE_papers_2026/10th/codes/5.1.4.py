from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc
from CoordGeo.conics.funcs import circ_gen
from CoordGeo.line.funcs import line_gen

O = np.array([0.0, 0.0])
radius = 1.0
S = np.array([1.0, 0.0])

# Central angle QOS is 110 degrees, so angle SQT is 55 degrees.
Q = np.array([np.cos(np.deg2rad(110)), np.sin(np.deg2rad(110))])

# Find P where the tangent at Q meets the x-axis.
P = np.array([radius**2 / Q[0], 0.0])
tangent_direction = np.array([Q[1], -Q[0]])
T = Q + 0.85 * tangent_direction

circle = circ_gen(O.reshape(2, 1), radius)
pq = line_gen(P, Q)
qt = line_gen(Q, T)
qs = line_gen(Q, S)
ps = line_gen(P, S)
oq = line_gen(O, Q)

fig, ax = plt.subplots(figsize=(7, 5))
ax.plot(circle[0], circle[1], color="black", linewidth=1.5)
ax.plot(pq[0], pq[1], color="royalblue", linewidth=2, label="Tangent PT")
ax.plot(qt[0], qt[1], color="royalblue", linewidth=2)
ax.plot(qs[0], qs[1], color="darkorange", linewidth=1.8, label="Chord QS")
ax.plot(ps[0], ps[1], color="seagreen", linewidth=1.8, label="Line PS")
ax.plot(oq[0], oq[1], color="gray", linestyle="--", linewidth=1.2, label="Radius OQ")

for point, name, offset in [
    (P, "P", (-12, -18)),
    (Q, "Q", (-12, 8)),
    (T, "T", (6, 2)),
    (O, "O", (5, -16)),
    (S, "S", (6, -3)),
]:
    ax.scatter(*point, color="crimson" if name == "Q" else "black", zorder=4)
    ax.annotate(name, point, xytext=offset, textcoords="offset points", fontsize=11)

ax.add_patch(Arc(Q, 0.38, 0.38, theta1=-35, theta2=20,
                 color="purple", linewidth=1.5))
ax.text(Q[0] + 0.18, Q[1] - 0.25, r"$55^\circ$", color="purple")

ax.add_patch(Arc(P, 0.65, 0.65, theta1=0, theta2=20,
                 color="purple", linewidth=1.5))
ax.text(P[0] + 0.36, P[1] + 0.09, r"$20^\circ$", color="purple")

ax.set_aspect("equal", adjustable="box")
ax.set_xlim(P[0] - 0.35, 1.35)
ax.set_ylim(-1.35, 1.55)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Tangent and chord angle")
ax.grid(True, linestyle=":", alpha=0.6)
ax.legend(loc="lower right", fontsize=8)
fig.tight_layout()

output = Path(__file__).resolve().parent.parent / "figs" / "5.1.4.png"
fig.savefig(output, dpi=300, bbox_inches="tight")
