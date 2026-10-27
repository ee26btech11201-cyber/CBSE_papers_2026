from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from CoordGeo.line.funcs import line_gen
from CoordGeo.plotting.funcs import label_pts

A = np.array([3., 4.])
B = np.array([1., 1.])
C = np.array([-8., 7.])
AB = line_gen(A, B)
BC = line_gen(B, C)
CA = line_gen(C, A)

fig, ax = plt.subplots(figsize=(6, 5))
for seg, label in [(AB, 'AB'), (BC, 'BC'), (CA, 'CA')]:
    ax.plot(seg[0], seg[1], color='royalblue', lw=2, label=label)
pts = np.column_stack((A, B, C))
ax.scatter(pts[0], pts[1], color='crimson', zorder=3)
label_pts(pts, ['A(3,4)', 'B(1,1)', 'C(-8,7)'])
u = (A-B) / np.linalg.norm(A-B)
v = (C-B) / np.linalg.norm(C-B)
corner = [B + 0.35*u, B + 0.35*(u+v), B + 0.35*v]
for X, Y in zip(corner, corner[1:] + corner[:1]):
    mark = line_gen(X, Y)
    ax.plot(mark[0], mark[1], color='black', lw=1.2)
ax.set_aspect('equal', adjustable='box')
ax.set(xlim=(-10, 5), ylim=(-1, 9), xlabel='x', ylabel='y', title='Right triangle ABC')
ax.grid(True, ls=':', alpha=.6)
fig.tight_layout()
out = Path(__file__).resolve().parent.parent / 'figs' / '5.1.22.1.png'
out.parent.mkdir(exist_ok=True)
fig.savefig(out, dpi=300, bbox_inches='tight')
