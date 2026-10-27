from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from CoordGeo.line.funcs import line_gen
from CoordGeo.plotting.funcs import label_pts

# Scale the given diagram so EB=5, BC=10, CF=5. The inner triangle
# is half the size of the outer triangle because its sides are parallel.
E = np.array([0., 0.]); B = np.array([5., 0.]); C = np.array([15., 0.]); F = np.array([20., 0.])
D = np.array([10., 12.]); A = np.array([10., 6.])
segments = [(E,D,'ED'), (D,F,'DF'), (F,E,'FE'), (B,A,'BA'), (A,C,'AC'), (C,B,'CB')]
fig, ax = plt.subplots(figsize=(6, 5))
for X, Y, _ in segments:
    seg = line_gen(X, Y)
    ax.plot(seg[0], seg[1], color='black', lw=1.8)
pts = np.column_stack((E,D,F,B,A,C))
ax.scatter(pts[0], pts[1], color='black', s=18, zorder=3)
label_pts(pts, ['E','D','F','B','A','C'])
ax.text(2.1, .25, '5 cm', ha='center')
ax.text(10, .25, '10 cm', ha='center')
ax.text(17.5, .25, '5 cm', ha='center')
ax.text(7.5, 3.5, 'AB = 7 cm', rotation=50, ha='center')
ax.set_aspect('equal', adjustable='box')
ax.set_xlim(-1, 21); ax.set_ylim(-1, 14)
ax.axis('off')
ax.set_title(r'$AB\parallel DE,\quad AC\parallel DF$')
fig.tight_layout()
out = Path(__file__).resolve().parent.parent / 'figs' / '5.1.23.png'
out.parent.mkdir(exist_ok=True)
fig.savefig(out, dpi=300, bbox_inches='tight')
