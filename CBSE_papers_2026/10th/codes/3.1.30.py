"""Plot the points and calculate the ratio and x-coordinate for Question 3.1.30."""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import sys

sys.path.insert(0,str(Path(__file__).resolve().parent))
from CoordGeo.line.funcs import line_gen

A=np.array([[-5.0],[4.0]])
B=np.array([[7.0],[9.0]])
m,n=3,2  # AP:PB from the y-coordinate differences (7-4):(9-7)
P=(n*A+m*B)/(m+n)
segment=line_gen(A,B)
fig,ax=plt.subplots(figsize=(5,3.8))
ax.plot(segment[0],segment[1],color="navy",lw=1.7)
for Q,name,off in ((A,"A (-5, 4)",(-50,8)),(B,"B (7, 9)",(5,5)),(P,"P (11/5, 7)",(5,-15))):
    ax.scatter(Q[0,0],Q[1,0],color="crimson",zorder=3)
    ax.annotate(name,Q[:,0],xytext=off,textcoords="offset points",fontsize=8)
ax.set(xlim=(-7,9),ylim=(2,11),xlabel="$x$",ylabel="$y$",title="Point P divides AB internally")
ax.grid(alpha=.25); ax.legend(["AB"],loc="lower right"); fig.tight_layout()
print(f"AP:PB={m}:{n}; P=({P[0,0]:g}, {P[1,0]:g}), so x=11/5.")
out=Path(__file__).resolve().parent.parent/"figs"/"3.1.30.png"
fig.savefig(out,dpi=300,bbox_inches="tight"); print(f"Figure saved to {out}")
