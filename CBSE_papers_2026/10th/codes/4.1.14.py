"""Draw the circle, tangent and secant, and calculate angle PTR."""
from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from CoordGeo.conics.funcs import circ_gen
from CoordGeo.line.funcs import line_gen, line_isect

radius = 4.0
O = np.array([[0.0], [0.0]])
P = np.array([[0.0], [-radius]])
S = np.array([[0.0], [radius]])

# OP points downward; rotate it 65 degrees toward the right to locate R.
central_angle = np.deg2rad(65)
angle_or = np.deg2rad(-90 + 65)
R = radius * np.array([[np.cos(angle_or)], [np.sin(angle_or)]])

# Intersect the secant SR with the tangent y=-radius to obtain T.
direction = R - S
normal_secant = np.array([[-direction[1, 0]], [direction[0, 0]]])
c_secant = (normal_secant.T @ S).item()
normal_tangent = np.array([[0.0], [1.0]])
T = line_isect(normal_secant, c_secant, normal_tangent, -radius)
Q = np.array([[8.0], [-radius]])

circle = circ_gen(O, radius)
fig, ax = plt.subplots(figsize=(5.8, 5.0))
ax.plot(circle[0], circle[1], color="navy", label="Circle")
ax.plot(*line_gen(P, Q), color="royalblue", label="Tangent PQ")
ax.plot(*line_gen(S, T), color="darkorange", label="Secant SRT")
ax.plot(*line_gen(O, P), "--", color="gray", label="Radius OP")
ax.plot(*line_gen(O, R), ":", color="gray", label="Radius OR")
points = (O, P, Q, S, R, T)
ax.scatter([p[0, 0] for p in points], [p[1, 0] for p in points],
           color="crimson", zorder=3)
for point, label, offset in ((O, "O", (-12, 4)), (P, "P", (-10, -17)),
                             (Q, "Q", (5, -14)), (S, "S", (-8, 7)),
                             (R, "R", (7, -2)), (T, "T", (5, -14))):
    ax.annotate(label, (point[0, 0], point[1, 0]), xytext=offset,
                textcoords="offset points")
ax.text(0.35, -1.0, r"$65^\circ$", fontsize=10)
ax.text(T[0, 0] - 0.9, -radius + 0.35, r"$57.5^\circ$", fontsize=10)
ax.set_title("Tangent and secant from the diagram")
ax.set_xlabel("x (cm)")
ax.set_ylabel("y (cm)")
ax.set_aspect("equal", adjustable="box")
ax.set_xlim(-5, 10)
ax.set_ylim(-5, 6)
ax.grid(True, alpha=0.35)
ax.legend(loc="upper right", fontsize=8)
fig.tight_layout()

v1 = P - T
v2 = R - T
cos_angle = ((v1.T @ v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))).item()
angle_ptr = np.degrees(np.arccos(np.clip(cos_angle, -1.0, 1.0)))
print(f"m(angle PTR) = {angle_ptr:.1f} degrees")
output = Path(__file__).resolve().parent.parent / "figs" / "4.1.14.png"
fig.savefig(output, dpi=300, bbox_inches="tight")
print(f"Figure saved to {output}")
