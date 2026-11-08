# code by A.Chaitanya
"""Plot the graph for Question 1.2.1."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 7, 600)
roots = (-3, 5)
fig, ax = plt.subplots(figsize=(5.6, 4.2))
ax.plot(x, (x - 1) ** 2, color="royalblue", label=r"$y=(x-1)^2$")
ax.axhline(16, color="darkorange", label=r"$y=16$")
ax.scatter(roots, (16, 16), color="crimson", zorder=3)
for root in roots:
    ax.annotate(f"({root}, 16)", (root, 16), xytext=(5, 8),
                textcoords="offset points")
ax.set(xlim=(-5, 7), ylim=(-2, 32), xlabel="x", ylabel="y",
       title=r"Graph of $(x-1)^2=16$")
ax.grid(alpha=0.3)
ax.legend()
fig.tight_layout()
out = Path(__file__).resolve().parent.parent / "figs" / "1.2.1.png"
out.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(out, dpi=300, bbox_inches="tight")
