"""Plot both 3D lines and calculate their acute angle using CoordGeo points."""
from pathlib import Path
import sys
import matplotlib.pyplot as plt
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parent))
from CoordGeo.line.funcs import line_gen

P=np.array([[2.],[-5.],[1.]])
Q=np.array([[7.],[0.],[6.]])
d1=np.array([[3.],[2.],[6.]])
d2=np.array([[1.],[2.],[2.]])
cosine=abs(float((d1.T@d2)[0,0]/(np.linalg.norm(d1)*np.linalg.norm(d2))))
angle=np.arccos(cosine)
line1=line_gen(P-2*d1,P+2*d1);line2=line_gen(Q-2*d2,Q+2*d2)
fig=plt.figure(figsize=(5.5,4.5));ax=fig.add_subplot(111,projection="3d")
ax.plot(*line1,color="navy",lw=2,label="Line 1")
ax.plot(*line2,color="darkorange",lw=2,label="Line 2")
ax.scatter(*P[:,0],color="navy");ax.scatter(*Q[:,0],color="darkorange")
ax.set(xlabel="$x$",ylabel="$y$",zlabel="$z$",title="Pair of lines in symmetric form")
ax.legend();ax.set_box_aspect((1,1,1));fig.tight_layout()
print(f"d1·d2=19, |d1|=7, |d2|=3; acute angle=cos⁻¹(19/21)={np.degrees(angle):.3f}°.")
out=Path(__file__).resolve().parent.parent/"figs"/"5.1.25.png"
fig.savefig(out,dpi=300,bbox_inches="tight");print(f"Figure saved to {out}")
