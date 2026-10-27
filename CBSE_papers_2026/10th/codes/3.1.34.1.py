"""Plot the two lines and calculate their intersection for Question 3.1.34(a)."""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import sys

sys.path.insert(0,str(Path(__file__).resolve().parent))
from CoordGeo.line.funcs import line_isect

# x - 2y = 3 and 3x - 8y = 7
n1=np.array([[1.0],[ -2.0]]); n2=np.array([[3.0],[-8.0]])
P=line_isect(n1,3.0,n2,7.0)
x=np.linspace(-1,9,300)
y1=(x-3)/2; y2=(3*x-7)/8
fig,ax=plt.subplots(figsize=(5.2,3.8))
ax.plot(x,y1,label=r"$x-2y=3$",color="navy")
ax.plot(x,y2,label=r"$3x-8y=7$",color="darkorange")
ax.scatter(P[0,0],P[1,0],color="crimson",zorder=3)
ax.annotate(f"({P[0,0]:g}, {P[1,0]:g})",P[:,0],xytext=(6,8),textcoords="offset points")
ax.set(xlim=(-1,9),ylim=(-2,4),xlabel="$x$",ylabel="$y$",title="Graphical solution of the pair of lines")
ax.grid(alpha=.25); ax.legend(); fig.tight_layout()
print(f"The lines intersect at ({P[0,0]:g}, {P[1,0]:g}).")
out=Path(__file__).resolve().parent.parent/"figs"/"3.1.34.1.png"
fig.savefig(out,dpi=300,bbox_inches="tight"); print(f"Figure saved to {out}")
