from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from CoordGeo.line.funcs import line_gen
from CoordGeo.plotting.funcs import label_pts

A = np.array([-1., 7.]); B = np.array([4., -3.]); P = np.array([2., 1.])
AB = line_gen(A, B)
AP = line_gen(A, P); PB = line_gen(P, B)
line = line_gen(np.array([-8., -7/3]), np.array([8., 3.])) # x-3y=-1
fig, ax = plt.subplots(figsize=(6, 5))
ax.plot(AB[0], AB[1], color='gray', ls='--', label='Segment AB')
ax.plot(AP[0], AP[1], color='royalblue', lw=2, label='AP')
ax.plot(PB[0], PB[1], color='seagreen', lw=2, label='PB')
ax.plot(line[0], line[1], color='darkorange', lw=1.5, label=r'$x-3y=-1$')
pts = np.column_stack((A, P, B))
ax.scatter(pts[0], pts[1], color='crimson', zorder=3)
label_pts(pts, ['A(-1,7)','P(2,1)','B(4,-3)'])
ax.set_aspect('equal', adjustable='box')
ax.set(xlim=(-3, 6), ylim=(-5, 9), xlabel='x', ylabel='y', title='Point P divides AB in the ratio 3:2')
ax.grid(True, ls=':', alpha=.6)
ax.legend(fontsize=8)
fig.tight_layout()
out = Path(__file__).resolve().parent.parent / 'figs' / '5.1.29.2.png'
out.parent.mkdir(exist_ok=True)
fig.savefig(out, dpi=300, bbox_inches='tight')
