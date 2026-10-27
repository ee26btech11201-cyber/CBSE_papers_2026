from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Wedge
from CoordGeo.conics.funcs import circ_gen
from CoordGeo.line.funcs import line_gen

r = 10.0
center = np.array([[0.], [0.]])
circle = circ_gen(center, r)
fig, ax = plt.subplots(figsize=(5, 5))
ax.fill_between([], [], color='none')
ax.add_patch(Wedge((0, 0), r, 0, 72, facecolor='lightskyblue', alpha=.75,
                   edgecolor='royalblue', linewidth=2, label='Highlighted sector'))
ax.plot(circle[0], circle[1], color='black', lw=1.5)
for deg in range(0, 360, 72):
    t = np.deg2rad(deg)
    edge = np.array([r*np.cos(t), r*np.sin(t)])
    ray = line_gen(center[:,0], edge)
    ax.plot(ray[0], ray[1], color='black', lw=1)
ax.scatter(0, 0, color='black', s=18)
ax.text(4.3, 2.7, r'$72^\circ$', ha='center')
ax.text(5.5, 6.2, 'one sector', color='navy', ha='center')
ax.set_aspect('equal', adjustable='box')
ax.set_xlim(-11, 11); ax.set_ylim(-11, 11)
ax.axis('off')
ax.set_title('Circle divided into five equal sectors')
fig.tight_layout()
out = Path(__file__).resolve().parent.parent / 'figs' / '5.1.26.png'
out.parent.mkdir(exist_ok=True)
fig.savefig(out, dpi=300, bbox_inches='tight')
