"""Plot the LPP feasible polygon and evaluate the objective at its corners."""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.insert(0,str(Path(__file__).resolve().parent))
from CoordGeo.line.funcs import line_gen

points=np.array([[0,0],[0,40],[20,40],[60,20],[60,0]],dtype=float)
Z=4*points[:,0]+3*points[:,1]
fig,ax=plt.subplots(figsize=(5.2,3.7))
closed=np.vstack([points,points[0]])
ax.fill(points[:,0],points[:,1],color="lightskyblue",alpha=.35,label="Feasible region")
ax.plot(closed[:,0],closed[:,1],color="navy",lw=1.8)
for (x,y),z in zip(points,Z):
    ax.scatter(x,y,color="crimson",zorder=3)
    ax.annotate(f"({x:g},{y:g}), Z={z:g}",(x,y),xytext=(5,5),textcoords="offset points",fontsize=7)
# A parallel objective line through the maximum corner (60,20).
x=np.linspace(0,65,300); ax.plot(x,(300-4*x)/3,"--",color="darkorange",label="$4x+3y=300$")
ax.set(xlim=(-5,70),ylim=(-5,50),xlabel="$x$",ylabel="$y$",title="Feasible region and objective values")
ax.grid(alpha=.25);ax.legend(fontsize=8);fig.tight_layout()
idx=int(np.argmax(Z));print(f"Corner objective values: {Z.tolist()}; maximum Z={Z[idx]:g} at {tuple(points[idx])}, option (B).")
out=Path(__file__).resolve().parent.parent/"figs"/"5.1.15.png"
fig.savefig(out,dpi=300,bbox_inches="tight");print(f"Figure saved to {out}")
