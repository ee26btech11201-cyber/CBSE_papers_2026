from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from CoordGeo.conics.funcs import circ_gen
from CoordGeo.line.funcs import line_gen
from CoordGeo.plotting.funcs import label_pts

O = np.array([2., 1.])
A = np.array([5., 6.])
B1 = np.array([-3., 4.])
B2 = np.array([-3., -2.])
r = np.sqrt(34)
circle = circ_gen(O.reshape(2, 1), r)
fig, ax = plt.subplots(figsize=(6, 5))
ax.plot(circle[0], circle[1], color='royalblue', lw=2, label='Circle')
for B, name, color in [(B1, r'$B_1(-3,4)$', 'darkorange'), (B2, r'$B_2(-3,-2)$', 'seagreen')]:
    chord = line_gen(A, B)
    ax.plot(chord[0], chord[1], lw=1.8, label=f'Chord to {name}')
pts = np.column_stack((O, A, B1, B2))
ax.scatter(pts[0], pts[1], color=['black','crimson','darkorange','seagreen'], zorder=3)
label_pts(pts, ['O(2,1)','A(5,6)','B₁(-3,4)','B₂(-3,-2)'])
ax.set_aspect('equal', adjustable='box')
ax.set(xlim=(-5, 9), ylim=(-6, 8), xlabel='x', ylabel='y', title='Circle and both possible points B')
ax.grid(True, ls=':', alpha=.6)
ax.legend(fontsize=8)
fig.tight_layout()
out = Path(__file__).resolve().parent.parent / 'figs' / '5.1.29.1.png'
out.parent.mkdir(exist_ok=True)
fig.savefig(out, dpi=300, bbox_inches='tight')
