# code by A.Chaitanya
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

# Continuity requires k = lim[x->0] x^2 sin(1/x) = 0.
k = 0.0
x = np.linspace(-1, 1, 5000)
y = x**2 * np.sin(1 / np.where(x == 0, np.inf, x))
y[x == 0] = k

fig, ax = plt.subplots(figsize=(6.2, 3.8))
ax.plot(x, x**2, color="darkorange", ls="--", lw=1.1, label=r"$y=x^2$")
ax.plot(x, -x**2, color="seagreen", ls="--", lw=1.1, label=r"$y=-x^2$")
ax.plot(x, y, color="navy", lw=1.2, label=r"$x^2\sin(1/x)$; $f(0)=k=0$")
ax.scatter([0], [k], color="crimson", zorder=3)
ax.axhline(0, color="black", lw=0.6)
ax.axvline(0, color="black", lw=0.6)
ax.set(xlabel="$x$", ylabel="$y$", title="Squeeze theorem at $x=0$")
ax.grid(alpha=0.25)
ax.legend()
fig.tight_layout()
out = Path(__file__).resolve().parent.parent / "figs" / "2.2.4.png"
fig.savefig(out, dpi=220)
