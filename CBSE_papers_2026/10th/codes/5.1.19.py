from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from CoordGeo.line.funcs import line_gen

# The lines reduce to y=(3x+7)/5 and y=(3x-7)/5.
x0, x1 = -6.0, 6.0
y1 = lambda x: (3*x + 7)/5
y2 = lambda x: (3*x - 7)/5
L1 = line_gen(np.array([x0, y1(x0)]), np.array([x1, y1(x1)]))
L2 = line_gen(np.array([x0, y2(x0)]), np.array([x1, y2(x1)]))

fig, ax = plt.subplots(figsize=(7, 5))
ax.plot(L1[0], L1[1], lw=2, label=r"$3x-5y+7=0$")
ax.plot(L2[0], L2[1], lw=2, label=r"$-6x+10y+14=0$")
ax.axhline(0, color='black', lw=.7)
ax.axvline(0, color='black', lw=.7)
ax.set(xlim=(-6, 6), ylim=(-5, 5), xlabel='x', ylabel='y',
       title='Parallel lines: no point of intersection')
ax.grid(True, ls=':', alpha=.6)
ax.legend()
fig.tight_layout()
out = Path(__file__).resolve().parent.parent / 'figs' / '5.1.19.png'
out.parent.mkdir(exist_ok=True)
fig.savefig(out, dpi=300, bbox_inches='tight')
