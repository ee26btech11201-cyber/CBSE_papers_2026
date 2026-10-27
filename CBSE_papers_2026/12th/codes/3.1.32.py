import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-8, 8, 1200)
f = x / np.sqrt(1 + x**2)
fig, ax = plt.subplots(figsize=(6.2, 3.8))
ax.plot(x, f, color="navy", label=r"$f(x)=x/\sqrt{1+x^2}$")
ax.axhline(1, color="gray", ls="--", lw=0.9)
ax.axhline(-1, color="gray", ls="--", lw=0.9)
ax.text(5.5, 1.04, "$y=1$ (not attained)", fontsize=8)
ax.text(5.5, -1.10, "$y=-1$ (not attained)", fontsize=8)
ax.set(xlabel="$x$", ylabel="$f(x)$", title="One-one function with range $(-1,1)$")
ax.grid(alpha=0.25)
ax.legend()
fig.tight_layout()
fig.savefig("figs/3.1.32.png", dpi=220)
