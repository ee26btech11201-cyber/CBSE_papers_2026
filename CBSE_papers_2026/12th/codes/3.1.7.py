import numpy as np
import matplotlib.pyplot as plt

# Continuity requires k = lim[x->0] x^2 sin(1/x) = 0.
k = 0.0
x = np.linspace(-1, 1, 5000)
y = x**2 * np.sin(1 / np.where(x == 0, np.inf, x))
y[x == 0] = k

fig, ax = plt.subplots(figsize=(6.2, 3.8))
ax.plot(x, y, color="navy", lw=1.2, label=r"$x^2\sin(1/x)$; $f(0)=k=0$")
ax.scatter([0], [k], color="crimson", zorder=3)
ax.axhline(0, color="black", lw=0.6)
ax.axvline(0, color="black", lw=0.6)
ax.set(xlabel="$x$", ylabel="$f(x)$", title="Continuity at $x=0$")
ax.grid(alpha=0.25)
ax.legend()
fig.tight_layout()
fig.savefig("figs/3.1.7.png", dpi=220)
