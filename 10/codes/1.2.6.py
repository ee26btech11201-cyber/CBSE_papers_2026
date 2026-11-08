# code by A.Chaitanya
"""Plot the equal-root quadratics for Question 1.2.6."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

root3 = np.sqrt(3.0)
k_values = (-2.0 * np.sqrt(6.0), 2.0 * np.sqrt(6.0))
x = np.linspace(-4.0, 4.0, 700)
fig, ax = plt.subplots(figsize=(5.8, 4.2))
for k in k_values:
    y = root3 * x**2 - k * x + 2.0 * root3
    repeated_root = k / (2.0 * root3)
    ax.plot(x, y, label=rf"$k={k:.3f}$")
    ax.scatter([repeated_root], [0.0], zorder=3)
    ax.annotate(rf"$x={repeated_root:.2f}$", (repeated_root, 0.0),
                xytext=(5, 8), textcoords="offset points", fontsize=8)
ax.axhline(0.0, color="black", linewidth=0.8)
ax.set(xlim=(-4.0, 4.0), ylim=(-2.0, 32.0), xlabel="x", ylabel="y",
       title=r"Equal-root parabolas: $\sqrt{3}x^2-kx+2\sqrt{3}=0$")
ax.grid(alpha=0.3)
ax.legend()
fig.tight_layout()
out = Path(__file__).resolve().parent.parent / "figs" / "1.2.6.png"
out.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(out, dpi=300, bbox_inches="tight")
