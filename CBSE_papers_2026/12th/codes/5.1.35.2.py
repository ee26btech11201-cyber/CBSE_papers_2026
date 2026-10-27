"""Plot the two skew lines for both values of p giving shortest distance 3/2."""
from pathlib import Path
import sys
import matplotlib.pyplot as plt
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parent))
from CoordGeo.line.funcs import line_gen

P=np.array([[1.],[2.],[1.]])
d1=np.array([[1.],[-1.],[1.]])
d2=np.array([[2.],[1.],[2.]])
cross=np.cross(d1[:,0],d2[:,0]);pvalues=(2.0,-4.0)
fig=plt.figure(figsize=(5.5,4.5));ax=fig.add_subplot(111,projection="3d")
L1=line_gen(P-2*d1,P+2*d1);ax.plot(*L1,color="navy",lw=2,label="First line")
for p,color in zip(pvalues,("darkorange","seagreen")):
    Q=np.array([[p],[-1.],[-1.]])
    L2=line_gen(Q-2*d2,Q+2*d2)
    ax.plot(*L2,color=color,lw=1.6,label=f"Second line, p={p:.3f}")
ax.set(xlabel="$x$",ylabel="$y$",zlabel="$z$",title="Skew lines for the two valid p values")
ax.legend(fontsize=7);ax.set_box_aspect((1,1,1));fig.tight_layout()
print(f"Cross direction d1×d2={cross}.")
print("Distance = |(Q-P)·(d1×d2)|/|d1×d2| = |p+1|/√2 = 3/√2.")
print(f"Therefore |p+1|=3, so p={pvalues[0]:g} or {pvalues[1]:g}.")
out=Path(__file__).resolve().parent.parent/"figs"/"5.1.35.2.png"
fig.savefig(out,dpi=300,bbox_inches="tight");print(f"Figure saved to {out}")
