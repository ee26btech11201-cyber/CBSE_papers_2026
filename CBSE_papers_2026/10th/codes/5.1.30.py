from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from CoordGeo.line.funcs import line_gen

x = np.linspace(-2, 7, 2)
vertical = line_gen(np.array([4., -5.]), np.array([4., 8.]))
sloping = line_gen(np.array([-2., -6.]), np.array([7., 7.5])) # y=(3x-6)/2
fig, ax = plt.subplots(figsize=(6, 5))
ax.plot(vertical[0], vertical[1], lw=2, label=r'$x=4$')
ax.plot(sloping[0], sloping[1], lw=2, label=r'$3x-2y=6$')
ax.scatter(4, 3, color='crimson', zorder=3)
ax.annotate('(4, 3)', (4,3), xytext=(7,8), textcoords='offset points')
ax.axhline(0, color='black', lw=.7); ax.axvline(0, color='black', lw=.7)
ax.set(xlim=(-2,7), ylim=(-6,8), xlabel='x', ylabel='y', title='Graphical solution: (4, 3)')
ax.set_aspect('equal', adjustable='box'); ax.grid(True, ls=':', alpha=.6); ax.legend()
fig.tight_layout()
out = Path(__file__).resolve().parent.parent / 'figs' / '5.1.30.png'
out.parent.mkdir(exist_ok=True)
fig.savefig(out, dpi=300, bbox_inches='tight')
