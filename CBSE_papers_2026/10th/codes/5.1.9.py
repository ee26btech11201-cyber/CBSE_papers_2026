from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from CoordGeo.conics.funcs import parab_gen
from CoordGeo.line.funcs import line_gen

# The rational-root option is p = -5, so y = x^2 + 5x + 6.
x = np.linspace(-5, 1, 500)
t = x + 2.5
y = parab_gen(t, 1.0) - 0.25
roots = np.array([-3.0, -2.0])
vertex_x = -2.5
vertex_y = vertex_x**2 + 5 * vertex_x + 6

fig, ax = plt.subplots(figsize=(7, 5))
ax.plot(x, y, color="royalblue", linewidth=2,
        label=r"$y=x^2+5x+6=(x+3)(x+2)$")
x_axis = line_gen(np.array([-5.0, 0.0]), np.array([1.0, 0.0]))
y_axis = line_gen(np.array([0.0, -2.0]), np.array([0.0, 8.0]))
ax.plot(x_axis[0], x_axis[1], color="black", linewidth=0.8)
ax.plot(y_axis[0], y_axis[1], color="black", linewidth=0.8)
ax.scatter(roots, [0, 0], color="crimson", zorder=3,
           label="Rational roots")
ax.scatter(vertex_x, vertex_y, color="darkorange", zorder=3,
           label="Vertex")
ax.annotate(r"$(-3,0)$", (-3, 0), xytext=(-26, 10),
            textcoords="offset points")
ax.annotate(r"$(-2,0)$", (-2, 0), xytext=(5, 10),
            textcoords="offset points")
ax.annotate(r"$(-2.5,-0.25)$", (vertex_x, vertex_y), xytext=(-5, -22),
            textcoords="offset points", ha="center")

ax.set_xlim(-5, 1)
ax.set_ylim(-2, 8)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title(r"Graph of $x^2+5x+6=0$ for $p=-5$")
ax.grid(True, linestyle=":", alpha=0.7)
ax.legend()
fig.tight_layout()

output = Path(__file__).resolve().parent.parent / "figs" / "5.1.9.png"
fig.savefig(output, dpi=300, bbox_inches="tight")
