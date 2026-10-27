from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
u=np.array([4.,-1.,3.]); v=np.array([-2.,1.,-2.]); n=np.cross(u,v); flag=5*n/np.linalg.norm(n)
fig=plt.figure(figsize=(5,4)); ax=fig.add_subplot(111,projection='3d')
for vec,label,color in [(u,'Rod 1','steelblue'),(v,'Rod 2','darkorange'),(flag,'5 m flag-post','crimson')]:
 ax.quiver(0,0,0,*vec,color=color,arrow_length_ratio=.12,label=label)
ax.set(xlabel='$x$',ylabel='$y$',zlabel='$z$',title='Two rods and perpendicular flag-post'); ax.set_xlim(-3,5); ax.set_ylim(-2,3); ax.set_zlim(-3,5); ax.legend(fontsize=8); ax.set_box_aspect((1,1,1)); fig.tight_layout()
out=Path(__file__).resolve().parent.parent/'figs'/'4.1.25a.png'; fig.savefig(out,dpi=250)
print(f'a×b={n}; |a×b|={np.linalg.norm(n):g}; required vector is ±5/3(-i+2j+2k) m = {flag}. Figure: {out}')
