from pathlib import Path
import sys
import numpy as np
import matplotlib.pyplot as plt
sys.path.insert(0,str(Path(__file__).resolve().parent))
from CoordGeo.line.funcs import line_gen
P=np.array([[2.],[1.],[3.]])
d=np.array([[3.],[-2.],[2.]])
Q=np.array([[1.],[2.],[3.]])
roots=np.roots([17,10,0]); pts=[P[:,0]+t*d[:,0] for t in roots if abs(np.linalg.norm(P[:,0]+t*d[:,0]-Q[:,0])-np.sqrt(2))<1e-7]
L=line_gen(P-1.2*d,P+1.2*d)
fig=plt.figure(figsize=(5,4)); ax=fig.add_subplot(111,projection='3d'); ax.plot(*L,color='steelblue',label='given line')
ax.scatter(*Q[:,0],color='black',label='(1,2,3)')
for i,R in enumerate(pts): ax.scatter(*R,label=f'point {i+1}'); ax.text(*R,f'({R[0]:.2f},{R[1]:.2f},{R[2]:.2f})',fontsize=7)
ax.set(xlabel='$x$',ylabel='$y$',zlabel='$z$',title='Points on the line at distance $\\sqrt{2}$'); ax.legend(fontsize=7); ax.set_box_aspect((1,1,1)); fig.tight_layout()
out=Path(__file__).resolve().parent.parent/'figs'/'4.1.30a.png'; fig.savefig(out,dpi=250)
print('Points:',*[tuple(np.round(R,6)) for R in pts]); print('Figure:',out)
