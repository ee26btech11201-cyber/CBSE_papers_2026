"""Draw the tangent-radius configuration and calculate OP."""
from pathlib import Path
import sys
import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from CoordGeo.conics.funcs import circ_gen
from CoordGeo.line.funcs import line_gen

r=3.0
O=np.array([[0.],[0.]])
T=np.array([[r],[0.]])
P=np.array([[r],[r]])
circle=circ_gen(O,r)
op=float(np.linalg.norm(P-O))

fig,ax=plt.subplots(figsize=(5.3,4.4))
ax.plot(circle[0],circle[1],color="navy",label="Circle")
ax.plot(*line_gen(np.array([[r],[-1.0]]),np.array([[r],[r+2]])),
        color="darkorange",label="Tangent PT")
ax.plot(*line_gen(O,T),color="gray",ls="--",label="Radius OT")
ax.plot(*line_gen(O,P),color="royalblue",label="OP")
for pt,name,offset in ((O,"O",(-12,-12)),(T,"T",(5,-10)),(P,"P",(5,5))):
    ax.scatter(pt[0,0],pt[1,0],color="crimson",zorder=3)
    ax.annotate(name,(pt[0,0],pt[1,0]),xytext=offset,textcoords="offset points")
ax.text(.8,.25,r"$45^\circ$")
ax.set(xlim=(-4,6),ylim=(-4,6),xlabel="x",ylabel="y",
       title="Radius perpendicular to tangent at T")
ax.set_aspect("equal",adjustable="box"); ax.grid(alpha=.25); ax.legend(fontsize=8)
fig.tight_layout()
print(f"OP = r*sqrt(2) = {op:.3f} cm when r=3 cm; correct option (A).")
out=Path(__file__).resolve().parent.parent/"figs"/"3.1.12.png"
fig.savefig(out,dpi=300,bbox_inches="tight")
print(f"Figure saved to {out}")
