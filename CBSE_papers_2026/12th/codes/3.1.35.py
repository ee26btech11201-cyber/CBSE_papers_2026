import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import numpy as np
import matplotlib.pyplot as plt
from CoordGeo.line.funcs import line_gen

fig = plt.figure(figsize=(9, 4.3))
ax1 = fig.add_subplot(121, projection="3d")
ax2 = fig.add_subplot(122, projection="3d")

# (a) Parametric lines meet at the origin when both parameters equal -1.
p1, d1 = np.array([-3., 1., 5.]), np.array([-3., 1., 5.])
p2, d2 = np.array([-1., 2., 5.]), np.array([-1., 2., 5.])
for p, d, color, label in [(p1, d1, "tab:blue", r"$L_1$"), (p2, d2, "tab:orange", r"$L_2$")]:
    pts = line_gen(p, p + d)
    ax1.plot(*pts, color=color, label=label)
ax1.scatter([0], [0], [0], color="crimson", s=25, label="intersection (0,0,0)")
ax1.set_title("35(a): intersecting lines")
ax1.legend(fontsize=7)

# (b) Visualize a square between the given parallel lines.
a1 = np.array([1., 2., -4.]); a2 = np.array([3., 3., -5.]); b = np.array([2., 3., 6.])
v = a2 - a1
u = v - (v @ b) / (b @ b) * b  # perpendicular separation between lines
side = np.sqrt(293) / 7
edge = b / np.linalg.norm(b) * side
corners = np.array([a1, a1 + u, a1 + u + edge, a1 + edge, a1])
ax2.plot(*corners.T, color="tab:green", marker="o")
ax2.set_title(r"35(b): square; area $293/49$, $p=-2$")
for ax in (ax1, ax2):
    ax.set_xlabel("x"); ax.set_ylabel("y"); ax.set_zlabel("z")
fig.tight_layout(); fig.savefig("figs/3.1.35.png", dpi=220)
print("(b) side length = sqrt(293)/7; area = 293/49; p = -2")
