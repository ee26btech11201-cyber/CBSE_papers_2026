"""Plot both possible triangles for the given area."""
from pathlib import Path
import sys
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
sys.path.insert(0,str(Path(__file__).resolve().parent))
from CoordGeo.line.funcs import line_gen

A=np.array([[3.],[1.]])
B=np.array([[-2.],[1.]])
fig,ax=plt.subplots(figsize=(5,3.7))
for k,color in ((3,"darkorange"),(-1,"royalblue")):
    C=np.array([[0.],[float(k)]])
    for U,V in ((A,B),(B,C),(C,A)):
        q=line_gen(U,V); ax.plot(q[0],q[1],color=color,lw=1.7)
    ax.scatter([A[0,0],B[0,0],C[0,0]],[A[1,0],B[1,0],C[1,0]],color=color,zorder=3)
    ax.annotate(f"C(0,{k})",C[:,0],xytext=(5,3),textcoords="offset points",fontsize=8)
ax.scatter([3,-2],[1,1],color="black",zorder=4)
ax.annotate("A(3,1)",(3,1),xytext=(5,4),textcoords="offset points",fontsize=8)
ax.annotate("B(-2,1)",(-2,1),xytext=(-48,5),textcoords="offset points",fontsize=8)
ax.set(xlabel="$x$",ylabel="$y$",title=r"Triangles with area $5$ square units")
ax.set_aspect("equal",adjustable="box");ax.grid(alpha=.25)
ax.legend(handles=[Line2D([0],[0],color="darkorange",label="k=3"),Line2D([0],[0],color="royalblue",label="k=-1")])
fig.tight_layout()
print("Area = 1/2 * 5 * |k-1| = 5, so k=3 or k=-1 (option B).")
out=Path(__file__).resolve().parent.parent/"figs"/"5.1.7.png"
fig.savefig(out,dpi=300,bbox_inches="tight");print(f"Figure saved to {out}")
