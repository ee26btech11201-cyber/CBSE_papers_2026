# code by A.Chaitanya
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 1001)
y = 1 - np.abs(x)

fig, ax = plt.subplots(figsize=(5.2, 3.2))
ax.fill_between(x, 0, y, color="skyblue", alpha=0.35, label="Area = 1")
ax.plot(x, y, color="navy", linewidth=2, label=r"$f(x)=1-|x|$")
ax.scatter([-1, 0, 1], [0, 1, 0], color="crimson", zorder=3)
ax.set(xlim=(-1.1, 1.1), ylim=(-0.1, 1.15), xlabel="$x$", ylabel="$f(x)$",
       title=r"Graph of $f(x)=1-|x|$")
ax.set_xticks([-1, 0, 1])
ax.set_yticks([0, 0.5, 1])
ax.grid(alpha=0.25)
ax.legend(loc="upper right")
fig.tight_layout()

output = Path(__file__).resolve().parent.parent / "figs" / "2.2.5.png"
output.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(output, dpi=220)
