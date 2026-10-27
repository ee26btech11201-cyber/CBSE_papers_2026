"""Draw the kite/building diagram and calculate the roof height and string."""
from pathlib import Path
import sys
import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from CoordGeo.line.funcs import line_gen

ground = np.array([[0.0], [0.0]])
roof = np.array([[0.0], [60 - 20*np.sqrt(3)]])
projection = np.array([[60.0], [0.0]])
kite = np.array([[60.0], [60.0]])
roof_height = float(roof[1, 0])
string_length = float(np.linalg.norm(kite - roof))

fig, ax = plt.subplots(figsize=(5.8, 4.3))
ax.plot(*line_gen(ground, np.array([[0.0], [66.0]])), color="black", lw=2,
        label="Building")
ax.plot(*line_gen(ground, projection), color="gray", lw=1.5, label="Ground")
ax.plot(*line_gen(projection, kite), color="gray", ls="--", label="Vertical through kite")
ax.plot(*line_gen(ground, kite), color="royalblue", lw=1.8, label="Sight line from ground")
ax.plot(*line_gen(roof, kite), color="darkorange", lw=2, label="String")
ax.scatter([0, 0, 60], [0, roof_height, 60], color="crimson", zorder=4)
for point, label, offset in ((ground,"O",(-13,-14)), (roof,"R",(-14,4)),
                             (projection,"F",(4,-14)), (kite,"K",(5,4))):
    ax.annotate(label, (point[0,0], point[1,0]), xytext=offset,
                textcoords="offset points")
ax.text(27, 32, r"$45^\circ$"); ax.text(44, 36, r"$30^\circ$")
ax.text(1, 12, f"roof = {roof_height:.1f} m")
ax.text(39, 50, f"string = {string_length:.1f} m", rotation=-30)
ax.set(xlim=(-8, 72), ylim=(-4, 68), xlabel="Horizontal distance (m)",
       ylabel="Height (m)", title="Kite, building and observation angles")
ax.set_aspect("equal", adjustable="box"); ax.grid(alpha=.25)
ax.legend(loc="upper left", fontsize=7); fig.tight_layout()
print(f"Roof height = 60 - 20*sqrt(3) = {roof_height:.2f} m (about 25.4 m)")
print(f"String length = 40*sqrt(3) = {string_length:.2f} m (about 69.2 m)")
out = Path(__file__).resolve().parent.parent / "figs" / "4.1.34.png"
fig.savefig(out, dpi=300, bbox_inches="tight")
print(f"Figure saved to {out}")
