# code by A.Chaitanya
from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np

code_dir = Path(__file__).resolve().parent
sys.path.insert(0, str(code_dir))
from CoordGeo.line.funcs import line_gen
from CoordGeo.plotting.funcs import label_pts

A = np.array([[0.0], [4.0]])
B = np.array([[-2.0], [0.0]])
C = np.array([[3.0], [0.0]])
O = np.array([[0.0], [0.0]])

fig, ax = plt.subplots(figsize=(5.2, 3.8))
ax.fill([O[0, 0], A[0, 0], C[0, 0]],
        [O[1, 0], A[1, 0], C[1, 0]],
        color="cornflowerblue", alpha=0.28, label=r"$\triangle OAC$")
ax.fill([O[0, 0], A[0, 0], B[0, 0]],
        [O[1, 0], A[1, 0], B[1, 0]],
        color="sandybrown", alpha=0.34, label=r"$\triangle AOB$")

for P, Q in ((A, B), (A, C), (B, C), (A, O)):
    segment = line_gen(P, Q)
    ax.plot(segment[0], segment[1], color="navy", linewidth=1.5)

vertices = np.hstack((A, B, C, O))
ax.scatter(vertices[0], vertices[1], color="black", s=18, zorder=3)
label_pts(vertices, ["A", "B", "C", "O"])

ax.axhline(0, color="gray", linewidth=0.6)
ax.axvline(0, color="gray", linewidth=0.6)
ax.set(xlim=(-2.6, 3.6), ylim=(-0.7, 4.8), xlabel="$x$", ylabel="$y$",
       title="Triangular park and the two integration regions")
ax.set_aspect("equal", adjustable="box")
ax.set_xticks(range(-2, 4))
ax.set_yticks(range(0, 5))
ax.grid(alpha=0.22)
ax.legend(loc="upper right", fontsize=8)
fig.tight_layout()

output = code_dir.parent / "figs" / "2.2.18.png"
output.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(output, dpi=220)
plt.close(fig)
