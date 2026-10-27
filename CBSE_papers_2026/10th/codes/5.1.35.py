from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from CoordGeo.conics.funcs import circ_gen, contact
from CoordGeo.line.funcs import line_gen
from CoordGeo.plotting.funcs import label_pts

O = np.array([0., 0.]); P = np.array([13., 0.]); r = 5.
V = np.eye(2); u = np.zeros((2,1)); h = P.reshape(2,1)
Qmat, Rmat = contact(V, u, -r*r, h)
Q, R = Qmat[:,0], Rmat[:,0]
C = np.array([r, 0.]) # contact of the vertical tangent AB with OP
A = np.array([r, 10/3]); B = np.array([r, -10/3])
circle = circ_gen(O.reshape(2,1), r)
fig, ax = plt.subplots(figsize=(7,5))
ax.plot(circle[0], circle[1], color='black', lw=1.6, label='Circle (r=5 cm)')
for X,Y,c,lw in [(P,Q,'royalblue',1.8),(P,R,'royalblue',1.8),(A,B,'darkorange',2),(O,P,'gray',1.2)]:
    seg=line_gen(X,Y); ax.plot(seg[0],seg[1],color=c,lw=lw)
pts=np.column_stack((O,P,Q,R,C,A,B))
ax.scatter(pts[0],pts[1],color='crimson',s=20,zorder=4)
label_pts(pts,['O','P(13,0)','Q','R','C(5,0)','A','B'])
ax.text(8.2, 2.0, r'$PA=26/3$ cm', rotation=-34, fontsize=9)
ax.text(5.2, .2, r'$AB=20/3$ cm', rotation=90, fontsize=9)
ax.set_aspect('equal', adjustable='box'); ax.set_xlim(-6,15); ax.set_ylim(-7,7)
ax.set_xlabel('x (cm)'); ax.set_ylabel('y (cm)'); ax.set_title('Two tangents from P and tangent AB at C')
ax.grid(True,ls=':',alpha=.5)
fig.tight_layout()
out=Path(__file__).resolve().parent.parent/'figs'/'5.1.35.png'
out.parent.mkdir(exist_ok=True)
fig.savefig(out,dpi=300,bbox_inches='tight')
