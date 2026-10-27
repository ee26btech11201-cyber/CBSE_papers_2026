"""Draw the circle and calculate its diameter for Question 4.1.7."""
from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np

# Use the CoordGeo library for the circle and diameter segment.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from CoordGeo.conics.funcs import circ_gen
from CoordGeo.line.funcs import line_gen

A = np.array([[0.0], [4.0]])  # intersection of the diameter with the y-axis
B = np.array([[2.0], [0.0]])  # intersection of the diameter with the x-axis
center = np.array([[1.0], [2.0]])

diameter = np.linalg.norm(B - A)
radius = diameter / 2
circle = circ_gen(center, radius)
diameter_segment = line_gen(A, B)

fig, ax = plt.subplots(figsize=(5.5, 5.0))
ax.plot(circle[0], circle[1], color="navy", label="Circle")
ax.plot(diameter_segment[0], diameter_segment[1], color="royalblue",
        linewidth=2, label="Diameter")
ax.axhline(0, color="black", linewidth=1)
ax.axvline(0, color="black", linewidth=1)
ax.scatter([A[0, 0], B[0, 0], center[0, 0]],
           [A[1, 0], B[1, 0], center[1, 0]], color="crimson", zorder=3)
ax.annotate("A(0, 4)", (A[0, 0], A[1, 0]), xytext=(7, 5),
            textcoords="offset points")
ax.annotate("B(2, 0)", (B[0, 0], B[1, 0]), xytext=(7, -17),
            textcoords="offset points")
ax.annotate("(1, 2)", (center[0, 0], center[1, 0]), xytext=(8, 7),
            textcoords="offset points")
ax.annotate("x", (3.7, 0), xytext=(4, -4), textcoords="offset points")
ax.annotate("y", (0, 5.0), xytext=(-4, 4), textcoords="offset points")
ax.set_title("Circle centred at (1, 2)")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_aspect("equal", adjustable="box")
ax.set_xlim(-1.5, 4)
ax.set_ylim(-1, 5.5)
ax.grid(True, alpha=0.35)
ax.legend(loc="lower right", fontsize=8)
fig.tight_layout()

print(f"Diameter = {diameter:.3f} = 2*sqrt(5)")
output = Path(__file__).resolve().parent.parent / "figs" / "4.1.7.png"
fig.savefig(output, dpi=300, bbox_inches="tight")
print(f"Figure saved to {output}")
