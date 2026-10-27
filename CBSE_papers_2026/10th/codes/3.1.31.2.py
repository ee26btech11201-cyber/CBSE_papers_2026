"""Draw the tangent configuration and calculate PB for Question 3.1.31(b)."""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import sys

sys.path.insert(0,str(Path(__file__).resolve().parent))
from CoordGeo.conics.funcs import circ_gen
from CoordGeo.line.funcs import line_gen

OA=10.0; AB=8.0
OB=np.sqrt(OA**2-AB**2)
PB=AB**2/OB  # From PA²=PB²+AB² and PA²=PO²-OA²
O=np.array([[0.0],[0.0]])
B=np.array([[-OB],[0.0]])
A=np.array([[-OB],[-AB]])
P=np.array([[-OB-PB],[0.0]])
circle=circ_gen(O,OA)

fig,ax=plt.subplots(figsize=(5.2,4.2))
ax.plot(circle[0],circle[1],color="navy",lw=1.5)
for U,V,color in ((P,A,"darkorange"),(P,O,"gray"),(O,A,"royalblue"),(A,B,"seagreen")):
    pts=line_gen(U,V); ax.plot(pts[0],pts[1],color=color,lw=1.7)
for Q,label,off in ((P,"P",(-12,4)),(B,"B",(-2,6)),(A,"A",(4,-12)),(O,"O",(5,5))):
    ax.scatter(Q[0,0],Q[1,0],color="crimson",zorder=3); ax.annotate(label,Q[:,0],xytext=off,textcoords="offset points")
ax.annotate("6 cm",((B[0,0]+O[0,0])/2,0),xytext=(0,8),textcoords="offset points",ha="center",fontsize=8)
ax.annotate("8 cm",(B[0,0],A[1,0]/2),xytext=(-20,0),textcoords="offset points",ha="right",va="center",fontsize=8)
ax.set(xlim=(-17,12),ylim=(-13,12),xlabel="$x$ (cm)",ylabel="$y$ (cm)",title="Tangent PA and perpendicular AB")
ax.set_aspect("equal",adjustable="box"); ax.grid(alpha=.22); fig.tight_layout()
print(f"OB=√(10²−8²)=6 cm; PB=AB²/OB={PB:g} cm.")
out=Path(__file__).resolve().parent.parent/"figs"/"3.1.31.2.png"
fig.savefig(out,dpi=300,bbox_inches="tight"); print(f"Figure saved to {out}")
