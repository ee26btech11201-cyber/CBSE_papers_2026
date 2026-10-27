import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import numpy as np
import matplotlib.pyplot as plt
from CoordGeo.line.funcs import line_gen
from CoordGeo.plotting.funcs import label_pts

# Boundary lines are represented using pairs of points and CoordGeo line_gen.
lines = [
    (np.array([12., 0.]), np.array([0., 6.]), r"$x+2y=12$"),
    (np.array([5., 0.]), np.array([0., 4.]), r"$4x+5y=20$"),
    (np.array([6., 0.]), np.array([0., 12.]), r"$2x+y=12$"),
]
fig, ax = plt.subplots(figsize=(6.2, 4.4))
for a, b, label in lines:
    pts = line_gen(a, b)
    ax.plot(pts[0], pts[1], label=label)
vertices = np.array([[0, 4], [0, 6], [4, 4], [6, 0], [5, 0]], dtype=float)
labels = ["A", "B", "C", "D", "E"]
label_pts(vertices.T, labels)
ax.fill(vertices[[0, 1, 2, 3, 4], 0], vertices[[0, 1, 2, 3, 4], 1],
        color="gold", alpha=0.22, label="feasible region")
ax.scatter(vertices[:, 0], vertices[:, 1], color="black", s=18, zorder=3)
ax.set(xlim=(-0.5, 13), ylim=(-0.5, 13), xlabel="$x$", ylabel="$y$",
       title="LPP feasible region; maximum at (4,4)")
ax.grid(alpha=0.25); ax.legend(fontsize=8)
fig.tight_layout(); fig.savefig("figs/3.1.33.png", dpi=220)

# Objective values at the relevant corner points.
for name, (x, y) in zip(labels, vertices):
    print(f"{name}{(int(x), int(y))}: Z={600*x + 400*y:.0f}")
print("Maximum Z = 4000 at (4,4)")
