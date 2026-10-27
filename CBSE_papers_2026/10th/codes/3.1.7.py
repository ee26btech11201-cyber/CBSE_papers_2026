"""Numerically maximize the volume of a cone that fits in a cube."""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

edge = 1.0  # scale-free optimization; volume scales as edge**3
radii = np.linspace(0, edge/2, 1001)
heights = np.linspace(0, edge, 1001)
volumes = (np.pi/3) * radii[:,None]**2 * heights[None,:]
i,j = np.unravel_index(np.argmax(volumes), volumes.shape)
r_opt,h_opt = radii[i],heights[j]
v_opt = volumes[i,j]

fig, ax = plt.subplots(figsize=(5.4,3.8))
ax.plot(radii, (np.pi/3)*radii**2*edge, label=r"$h=\ell$")
ax.scatter([r_opt],[v_opt],color="crimson",zorder=3,
           label=rf"maximum: $r={r_opt:.2f}\ell$, $h={h_opt:.0f}\ell$")
ax.set(xlabel=r"Base radius $r/\ell$",ylabel=r"Volume $V/\ell^3$",
       title="Cone volume under cube constraints")
ax.grid(alpha=.3); ax.legend(); fig.tight_layout()
print(f"Optimal radius = {r_opt:.3f}*l; optimal height = {h_opt:.3f}*l")
print(f"Maximum volume = {v_opt:.6f}*l^3 = pi*l^3/12")
print("Correct option: (A)")
out=Path(__file__).resolve().parent.parent/"figs"/"3.1.7.png"
fig.savefig(out,dpi=300,bbox_inches="tight")
print(f"Figure saved to {out}")
