"""Draw the two tangents and calculate their lengths for Question 3.1.2."""
from pathlib import Path
import sys
import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from CoordGeo.conics.funcs import circ_gen
from CoordGeo.line.funcs import line_gen

radius = 3.0
O = np.array([[0.0], [0.0]])
P = np.array([[2*radius], [0.0]])
contact_x = radius**2 / P[0, 0]
contact_y = np.sqrt(radius**2 - contact_x**2)
Q = np.array([[contact_x], [contact_y]])
R = np.array([[contact_x], [-contact_y]])
circle = circ_gen(O, radius)
pq = float(np.linalg.norm(P-Q))
pr = float(np.linalg.norm(P-R))

fig, ax = plt.subplots(figsize=(5.5, 4.6))
ax.plot(circle[0], circle[1], color="navy", label="Circle")
for U, V, color, label in ((P,Q,"royalblue","Tangent PQ"),
                           (P,R,"darkorange","Tangent PR"),
                           (O,Q,"gray","Radius OQ"),
                           (O,R,"gray","Radius OR")):
    ax.plot(*line_gen(U,V), color=color, ls="--" if "Radius" in label else "-",
            label=label)
for pt, name, offset in ((O,"O",(-13,-12)),(P,"P",(5,-4)),
                         (Q,"Q",(5,5)),(R,"R",(5,-12))):
    ax.scatter(pt[0,0],pt[1,0],color="crimson",zorder=3)
    ax.annotate(name,(pt[0,0],pt[1,0]),xytext=offset,textcoords="offset points")
ax.text(4.6, .15, r"$60^\circ$")
ax.set(xlim=(-3.5,7),ylim=(-4.5,4.5),xlabel="x (cm)",ylabel="y (cm)",
       title="Two tangents from an external point")
ax.set_aspect("equal",adjustable="box"); ax.grid(alpha=.25)
ax.legend(fontsize=7,loc="upper left"); fig.tight_layout()
print(f"PQ = PR = {pq:.3f} cm = 3*sqrt(3) cm")
print(f"Independent calculation check: PR = {pr:.3f} cm")
out=Path(__file__).resolve().parent.parent/"figs"/"3.1.2.png"
fig.savefig(out,dpi=300,bbox_inches="tight")
print(f"Figure saved to {out}")
