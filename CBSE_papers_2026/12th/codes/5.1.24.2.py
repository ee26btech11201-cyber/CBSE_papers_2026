"""Draw the triangle in 3D and compute its area from AB x AC."""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

A=np.array([0.,0.,0.]); AB=np.array([1.,2.,-1.]); AC=np.array([2.,-3.,0.])
B=A+AB;C=A+AC
cross=np.cross(AB,AC);area=np.linalg.norm(cross)/2
fig=plt.figure(figsize=(5.2,4.2));ax=fig.add_subplot(111,projection="3d")
ax.add_collection3d(Poly3DCollection([[A,B,C]],facecolor="lightskyblue",alpha=.35,edgecolor="navy"))
for P,Q in ((A,B),(A,C),(B,C)):
    ax.plot(*np.array([P,Q]).T,color="navy",lw=2)
for P,label in ((A,"A"),(B,"B"),(C,"C")):
    ax.scatter(*P,color="crimson");ax.text(*P,label)
ax.set(xlabel="$x$",ylabel="$y$",zlabel="$z$",title="Triangle determined by vectors AB and AC")
ax.set_box_aspect((1,1,1));fig.tight_layout()
print(f"AB × AC = {cross}; area = |AB × AC|/2 = √62/2 ≈ {area:.4f} square units.")
out=Path(__file__).resolve().parent.parent/"figs"/"5.1.24.2.png"
fig.savefig(out,dpi=300,bbox_inches="tight");print(f"Figure saved to {out}")
