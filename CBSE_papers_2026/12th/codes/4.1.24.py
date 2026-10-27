from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
sys_path=Path(__file__).resolve().parent
import sys; sys.path.insert(0,str(sys_path/'CoordGeo'))
sys.path.insert(0,str(sys_path))
from CoordGeo.triangle.funcs import tri_sides
A=np.array([3.,1.,0.]); B=np.array([5.,6.,-3.]); C=np.array([0.,4.,0.])
sides=tri_sides(A,B,C)
fig=plt.figure(figsize=(5,4)); ax=fig.add_subplot(111,projection='3d'); P=np.array([A,B,C,A]); ax.plot(*P.T,color='navy',lw=2)
for X,n in [(A,'A'),(B,'B'),(C,'C')]: ax.scatter(*X); ax.text(*X,n)
ax.set(xlabel='$x$',ylabel='$y$',zlabel='$z$',title='Isosceles triangle in 3D'); ax.set_box_aspect((1,1,1)); fig.tight_layout()
out=Path(__file__).resolve().parent.parent/'figs'/'4.1.24.png'; fig.savefig(out,dpi=250)
print(f'AB={sides[0]:.4f}, BC={sides[1]:.4f}, AC={sides[2]:.4f}; AB=BC=√38, hence isosceles. Figure: {out}')
