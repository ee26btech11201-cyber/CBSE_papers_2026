import numpy as np
from CoordGeo.conics.funcs import parab_gen
from CoordGeo.line.funcs import line_gen
import matplotlib.pyplot as plt

k = -9 / 4

x = np.linspace(-4, 2, 500)
y = parab_gen(x + 4/3, -4/9)

# The repeated root is x = -4/3
root = -4 / 3

plt.figure(figsize=(7, 5))
plt.plot(x, y, label=r"$y=-\frac{9}{4}x^2-6x-4$")
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.scatter(root, 0, color="red", zorder=3, label=r"Repeated root $(-\frac{4}{3}, 0)$")

plt.xlim(-4, 2)
plt.ylim(-16, 3)
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.title(r"Graph for $k=-\frac{9}{4}$")
plt.grid(True)
plt.legend()
plt.tight_layout()
from pathlib import Path

output = Path(__file__).resolve().parent.parent / "figs" / "5.1.1.png"
plt.savefig(output, dpi=300)
