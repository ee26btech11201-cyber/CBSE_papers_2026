import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import numpy as np
import matplotlib.pyplot as plt
from CoordGeo.line.funcs import line_gen

fig = plt.figure(figsize=(9, 4.2))
ax1 = fig.add_subplot(121, projection="3d")
ax2 = fig.add_subplot(122, projection="3d")

# (a) Direction vectors are perpendicular when their dot product is zero.
# For p = +/-2, directions are (1,-1,p) and (-3,5,2p).
for p, color in [(2, "tab:blue"), (-2, "tab:orange")]:
    d1 = np.array([1., -1., float(p)])
    d2 = np.array([-3., 5., float(2*p)])
    print(f"(a) p={p}: direction dot product = {d1 @ d2:.0f}")
    ax1.plot(*line_gen(np.array([3., 1., -2.]), np.array([3., 1., -2.]) + d1).T,
             color=color, label=fr"$L_1$, $p={p}$")
    ax1.plot(*line_gen(np.array([2., -1., -56.]), np.array([2., -1., -56.]) + d2).T,
             color=color, ls="--", label=fr"$L_2$, $p={p}$")
ax1.set_title("25(a): perpendicular lines")
ax1.legend(fontsize=7)

# (b) A normal to both given directions is their cross product.
u = np.cross([3, 4, 2], [1, -1, 1])
print(f"(b) perpendicular direction = {u.astype(int)}")
base = np.zeros(3)
ax2.quiver(*base, *np.array([3, 4, 2]), color="tab:blue", label="first direction")
ax2.quiver(*base, *np.array([1, -1, 1]), color="tab:orange", label="second direction")
ax2.quiver(*base, *u, color="tab:green", label="required direction")
ax2.set_title(r"25(b): $\vec{n}=(6,-1,-7)$")
ax2.legend(fontsize=7)
for ax in (ax1, ax2):
    ax.set_xlabel("x"); ax.set_ylabel("y"); ax.set_zlabel("z")
fig.tight_layout()
fig.savefig("figs/3.1.25.png", dpi=220)
