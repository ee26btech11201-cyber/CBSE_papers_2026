# code by A.Chaitanya
from math import cos, pi
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def derivative(x):
    return 1 / cos(x) ** 2 - 4


# Bisection locates the zero of f'(x) in (0, pi/2).
low = 0.0
high = pi / 2 - 1e-6
for _ in range(60):
    midpoint = (low + high) / 2
    if derivative(midpoint) < 0:
        low = midpoint
    else:
        high = midpoint

critical = (low + high) / 2
print(f"f'(x) = 0 at x = {critical:.10f} radians")
print(f"f is increasing on approximately ({critical:.10f}, {pi / 2:.10f})")
print(f"Exact boundary: pi/3 = {pi / 3:.10f} radians")

# Plot the function, using the computed critical point to shade its increasing part.
x = np.linspace(0.001, pi / 2 - 0.001, 1500)
y = np.tan(x) - 4 * x

fig, ax = plt.subplots(figsize=(6.2, 3.8))
ax.plot(x, y, color="navy", label=r"$f(x)=\tan x-4x$")
ax.axvspan(critical, pi / 2, color="limegreen", alpha=0.16,
           label="Increasing interval")
ax.axvline(critical, color="darkgreen", ls="--", lw=1,
           label=rf"Bisection root $x\approx{critical:.3f}$")
ax.set(xlim=(0, pi / 2), ylim=(-3, 20), xlabel="$x$ (radians)", ylabel="$f(x)$",
       title=r"$f(x)=\tan x-4x$ and its increasing interval")
ax.set_xticks([0, critical, pi / 2], ["0", rf"{critical:.3f}", r"$\pi/2$"])
ax.grid(alpha=0.25)
ax.legend(loc="upper left")
fig.tight_layout()

out = Path(__file__).resolve().parent.parent / "figs" / "2.2.8.png"
fig.savefig(out, dpi=220)
plt.close(fig)
