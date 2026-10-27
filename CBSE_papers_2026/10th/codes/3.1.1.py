"""Plot (x-1)^2=16 and calculate its roots for Question 3.1.1."""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 7, 600)
parabola = (x - 1) ** 2
roots = (1 - np.sqrt(16), 1 + np.sqrt(16))

fig, ax = plt.subplots(figsize=(5.6, 4.2))
ax.plot(x, parabola, color="royalblue", label=r"$y=(x-1)^2$")
ax.axhline(16, color="darkorange", label=r"$y=16$")
ax.scatter(roots, [16, 16], color="crimson", zorder=3)
for r in roots:
    ax.annotate(f"({r:.0f}, 16)", (r, 16), xytext=(5, 8),
                textcoords="offset points")
ax.set(xlim=(-5, 7), ylim=(-2, 32), xlabel="x", ylabel="y",
       title=r"Intersections for $(x-1)^2=16$")
ax.grid(alpha=.3); ax.legend(); fig.tight_layout()
print(f"Roots: x = {roots[0]:.0f}, {roots[1]:.0f}")
out = Path(__file__).resolve().parent.parent / "figs" / "3.1.1.png"
fig.savefig(out, dpi=300, bbox_inches="tight")
print(f"Figure saved to {out}")
