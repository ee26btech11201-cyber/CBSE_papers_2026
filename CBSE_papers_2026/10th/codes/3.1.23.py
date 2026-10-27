"""Plot square ABCD from the given opposite vertices and calculate P and side."""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from CoordGeo.line.funcs import line_gen

B=np.array([[9.0],[-2.0]])
D=np.array([[1.0],[6.0]])
P=(B+D)/2
v=B-P
rot=np.array([[0.0,-1.0],[1.0,0.0]])
A=P+rot@v
C=P-rot@v
vertices={"A":A,"B":B,"C":C,"D":D}

fig,ax=plt.subplots(figsize=(4.8,4.4))
for u,vtx in ((A,B),(B,C),(C,D),(D,A),(A,C),(B,D)):
    pts=line_gen(u,vtx); ax.plot(pts[0],pts[1],color="navy",lw=1.5)
for name,Q in vertices.items():
    ax.scatter(Q[0,0],Q[1,0],color="crimson",zorder=3)
    ax.annotate(f"{name} ({Q[0,0]:g}, {Q[1,0]:g})",(Q[0,0],Q[1,0]),xytext=(5,5),textcoords="offset points",fontsize=8)
ax.scatter(P[0,0],P[1,0],color="darkorange",zorder=4)
ax.annotate(f"P ({P[0,0]:g}, {P[1,0]:g})",(P[0,0],P[1,0]),xytext=(5,-12),textcoords="offset points",fontsize=8)
ax.set(xlabel="$x$",ylabel="$y$",title="Square and intersecting diagonals"); ax.set_aspect("equal",adjustable="box")
ax.grid(alpha=.25); fig.tight_layout()
print(f"P=({P[0,0]:g}, {P[1,0]:g}); diagonal BD={np.linalg.norm(B-D):g}; side={np.linalg.norm(A-B):g}.")
out=Path(__file__).resolve().parent.parent/"figs"/"3.1.23.png"
fig.savefig(out,dpi=300,bbox_inches="tight"); print(f"Figure saved to {out}")
