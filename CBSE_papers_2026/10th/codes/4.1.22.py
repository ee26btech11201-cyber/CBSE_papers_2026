"""Draw the triangle configuration and verify CA^2 = CB*CD."""
from pathlib import Path
import sys
import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from CoordGeo.line.funcs import line_gen

# A convenient similar-triangle example: CA=6, CD=4, CB=9.
# Set C=(0,0), A=(0,6), D=(4,0), B=(9,0).
C = np.array([[0.], [0.]])
A = np.array([[0.], [6.]])
D = np.array([[4.], [0.]])
B = np.array([[9.], [0.]])

fig, ax = plt.subplots(figsize=(5.4, 4.2))
for U, V, color in ((A, B, "royalblue"), (A, C, "royalblue"), (C, B, "royalblue"), (A, D, "darkorange")):
    ax.plot(*line_gen(U, V), color=color, lw=1.8)
for p, name, off in ((A,"A",(-12,5)), (B,"B",(5,-12)), (C,"C",(-12,-12)), (D,"D",(4,-12))):
    ax.scatter(p[0,0], p[1,0], color="crimson", zorder=3)
    ax.annotate(name, (p[0,0],p[1,0]), xytext=off, textcoords="offset points")
ax.text(0.2, 3.2, r"$\angle CAB=\angle CDA$")
ax.set_title("Given configuration for Question 4.1.22")
ax.set_aspect("equal", adjustable="box"); ax.set_xlim(-1,10); ax.set_ylim(-1,7)
ax.axis("off"); fig.tight_layout()

print(f"CA^2 = {np.linalg.norm(A-C)**2:.0f}; CB*CD = {np.linalg.norm(B-C)*np.linalg.norm(D-C):.0f}")
out = Path(__file__).resolve().parent.parent / "figs" / "4.1.22.png"
fig.savefig(out, dpi=300, bbox_inches="tight")
print(f"Figure saved to {out}")
