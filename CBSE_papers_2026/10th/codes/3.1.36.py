"""Plot the arch polynomial and calculate height, zeros, span, and y-intercept."""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-3.2,5.2,600)
p=lambda z: -z**2+2*z+8
zeros=(-2.0,4.0)
vertex_x=1.0; vertex_y=p(vertex_x)
fig,ax=plt.subplots(figsize=(5.6,3.8))
ax.plot(x,p(x),color="navy",lw=2,label=r"$p(x)=-x^2+2x+8$")
ax.axhline(0,color="black",lw=.8); ax.axvline(0,color="black",lw=.8)
ax.scatter([*zeros,vertex_x,0],[0,0,vertex_y,8],color="crimson",zorder=3)
for pt,label,off in (((-2,0),"(-2, 0)",(-30,-17)),((4,0),"(4, 0)",(5,-17)),((1,9),"(1, 9)",(5,5)),((0,8),"(0, 8)",(-40,6))):
    ax.annotate(label,pt,xytext=off,textcoords="offset points",fontsize=8)
ax.set(xlim=(-3.2,5.2),ylim=(-3,11),xlabel="Stage distance x (ft)",ylabel="Height p(x) (ft)",title="Parabolic arch")
ax.grid(alpha=.25); ax.legend(); fig.tight_layout()
print("Maximum height = vertex y = 9 ft.")
print("Zeros are x=-2 and x=4; span between intercepts = 6 ft.")
print("The y-intercept is (0, 8).")
out=Path(__file__).resolve().parent.parent/"figs"/"3.1.36.png"
fig.savefig(out,dpi=300,bbox_inches="tight"); print(f"Figure saved to {out}")
