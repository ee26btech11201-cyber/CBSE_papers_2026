"""Plot a representative triangle and verify BX=4XY for Question 3.1.33."""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import sys

sys.path.insert(0,str(Path(__file__).resolve().parent))
from CoordGeo.line.funcs import line_gen

# A convenient non-degenerate triangle; the ratio result is affine-invariant.
A=np.array([[0.0],[4.0]]); B=np.array([[0.0],[0.0]]); C=np.array([[2.0],[0.0]])
D=(B+C)/2
X=(3*A+2*D)/5  # AX:XD=2:3
# Intersect BX with AC directly by solving B+t(X-B)=A+s(C-A).
M=np.column_stack((X[:,0]-B[:,0],-(C[:,0]-A[:,0])))
t,s=np.linalg.solve(M,(A-B)[:,0])
Y=B+t*(X-B)
BX=float(np.linalg.norm(X-B)); XY=float(np.linalg.norm(Y-X))

fig,ax=plt.subplots(figsize=(4.8,4.2))
for U,V,color in ((A,B,"navy"),(A,C,"navy"),(B,C,"navy"),(A,D,"darkorange"),(B,Y,"seagreen")):
    pts=line_gen(U,V); ax.plot(pts[0],pts[1],color=color,lw=1.6)
for Q,label,off in ((A,"A",(0,6)),(B,"B",(-12,-12)),(C,"C",(5,-8)),(D,"D",(3,-12)),(X,"X",(6,-3)),(Y,"Y",(5,2))):
    ax.scatter(Q[0,0],Q[1,0],color="crimson",zorder=3); ax.annotate(label,Q[:,0],xytext=off,textcoords="offset points")
ax.set(xlim=(-.8,2.8),ylim=(-.7,4.8),xlabel="$x$",ylabel="$y$",title="Median AD and line BY")
ax.set_aspect("equal",adjustable="box"); ax.grid(alpha=.22); fig.tight_layout()
print(f"AX:XD=2:3 gives X=({X[0,0]:.3f},{X[1,0]:.3f}); Y=({Y[0,0]:.3f},{Y[1,0]:.3f}).")
print(f"BX={BX:.3f}, XY={XY:.3f}, BX/XY={BX/XY:.3f}; hence BX=4XY.")
out=Path(__file__).resolve().parent.parent/"figs"/"3.1.33.png"
fig.savefig(out,dpi=300,bbox_inches="tight"); print(f"Figure saved to {out}")
