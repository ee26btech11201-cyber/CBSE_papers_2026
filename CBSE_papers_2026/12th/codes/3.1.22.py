import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.001, np.pi / 2 - 0.001, 1500)
f = np.tan(x) - 4*x

fig, ax = plt.subplots(figsize=(6.2, 3.8))
ax.plot(x, f, color="navy", label=r"$f(x)=\tan x-4x$")
ax.axvspan(np.pi/3, np.pi/2, color="limegreen", alpha=0.16,
           label=r"Increasing: $(\pi/3,\pi/2)$")
ax.axvline(np.pi/3, color="darkgreen", ls="--", lw=1)
ax.set(xlim=(0, np.pi/2), xlabel="$x$ (radians)", ylabel="$f(x)$",
       title=r"$f(x)=\tan x-4x$ on $(0,\pi/2)$")
ax.set_xticks([0, np.pi/3, np.pi/2], ["0", r"$\pi/3$", r"$\pi/2$"])
ax.grid(alpha=0.25)
ax.legend()
fig.tight_layout()
fig.savefig("figs/3.1.22.png", dpi=220)
