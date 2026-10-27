"""Plot the two lines for Question 4.1.8 and determine k."""
from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from CoordGeo.line.funcs import line_gen

# For inconsistency, the lines must be parallel and distinct.
k = 4 / 3
x = np.array([[-1.0], [11.0]])
y_first = np.array([[15 - 1.5 * x[0, 0]], [15 - 1.5 * x[1, 0]]])
y_second = np.array([[21 / 4 - 1.5 * x[0, 0]], [21 / 4 - 1.5 * x[1, 0]]])
line1 = line_gen(np.vstack((x[0], y_first[0])), np.vstack((x[1], y_first[1])))
line2 = line_gen(np.vstack((x[0], y_second[0])), np.vstack((x[1], y_second[1])))

fig, ax = plt.subplots(figsize=(6.0, 4.6))
ax.plot(line1[0], line1[1], color="royalblue", label=r"$x/2+y/3=5$")
ax.plot(line2[0], line2[1], color="darkorange", label=r"$2x+(4/3)y=7$")
ax.set_title(r"Parallel lines when $k=4/3$ (no intersection)")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_xlim(-1, 11)
ax.set_ylim(-2, 18)
ax.grid(True, alpha=0.35)
ax.legend()
fig.tight_layout()

print(f"For inconsistent equations, k = {k:.3f} = 4/3.")
output = Path(__file__).resolve().parent.parent / "figs" / "4.1.8.png"
fig.savefig(output, dpi=300, bbox_inches="tight")
print(f"Figure saved to {output}")
