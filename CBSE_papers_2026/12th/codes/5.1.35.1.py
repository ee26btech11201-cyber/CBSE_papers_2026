"""Plot the 3D line and the perpendicular from P; calculate the foot and length."""
from pathlib import Path
import sys
import matplotlib.pyplot as plt
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parent))
from CoordGeo.line.funcs import line_gen

P=np.array([[0.],[2.],[3.]])
A=np.array([[-3.],[1.],[-4.]])
d=np.array([[5.],[2.],[3.]])
t=float((d.T@(P-A))[0,0]/(d.T@d)[0,0])
H=A+t*d
distance=float(np.linalg.norm(P-H))
line=line_gen(A-1.7*d,A+1.7*d)
perp=line_gen(P,H)
fig=plt.figure(figsize=(5.4,4.5));ax=fig.add_subplot(111,projection="3d")
ax.plot(*line,color="navy",lw=2,label="Given line")
ax.plot(*perp,color="darkorange",lw=2,label="Perpendicular PH")
ax.scatter(*P[:,0],color="crimson");ax.text(*P[:,0],"P(0,2,3)")
ax.scatter(*H[:,0],color="green");ax.text(*H[:,0],"H(2,3,-1)")
ax.set(xlabel="$x$",ylabel="$y$",zlabel="$z$",title="Foot of perpendicular from P to the line")
ax.legend(fontsize=8);ax.set_box_aspect((1,1,1));fig.tight_layout()
print(f"Projection parameter t={t:g}; foot H=({H[0,0]:g},{H[1,0]:g},{H[2,0]:g}); PH=√21≈{distance:.4f}.")
out=Path(__file__).resolve().parent.parent/"figs"/"5.1.35.1.png"
fig.savefig(out,dpi=300,bbox_inches="tight");print(f"Figure saved to {out}")
