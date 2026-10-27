from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.insert(0,str(Path(__file__).resolve().parent/'CoordGeo'))
sys.path.insert(0,str(Path(__file__).resolve().parent))
from CoordGeo.triangle.funcs import tri_sides
A=np.array([0.,1.,1.]); B=np.array([2.,0.,-1.]); C=np.array([1.,0.,3.])
sides=tri_sides(A,B,C)
a,b,c=sides
s=(a+b+c)/2
area=np.sqrt(s*(s-a)*(s-b)*(s-c))
fig=plt.figure(figsize=(5,4)); ax=fig.add_subplot(111,projection='3d')
V=np.array([A,B,C,A]); ax.plot(*V.T,color='navy',lw=2)
for P,n in [(A,'A(0,1,1)'),(B,'B(2,0,-1)'),(C,'C(1,0,3)')]: ax.scatter(*P,s=35); ax.text(*P,n,fontsize=8)
ax.set(xlabel='$x$',ylabel='$y$',zlabel='$z$',title=f'Triangle ABC; area = {area:.4f}')
ax.set_box_aspect((1,1,1)); fig.tight_layout(); out=Path(__file__).resolve().parent.parent/'figs'/'4.1.17.png'; fig.savefig(out,dpi=250)
print(f'CoordGeo sides={sides}; Heron area = √53/2 ≈ {area:.4f}; choice (A). Figure: {out}')
