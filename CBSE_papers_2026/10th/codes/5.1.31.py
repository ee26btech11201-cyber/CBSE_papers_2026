from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from CoordGeo.line.funcs import line_gen

width, height, square = 156, 216, 12
fig, ax = plt.subplots(figsize=(6, 7))
for x in range(0, width + 1, square):
    seg = line_gen(np.array([x, 0.]), np.array([x, height]))
    ax.plot(seg[0], seg[1], color='royalblue', lw=.8)
for y in range(0, height + 1, square):
    seg = line_gen(np.array([0., y]), np.array([width, y]))
    ax.plot(seg[0], seg[1], color='royalblue', lw=.8)
ax.set_aspect('equal', adjustable='box')
ax.set_xlim(-5, width+5); ax.set_ylim(-5, height+5)
ax.set_xticks([0, 156]); ax.set_yticks([0, 216])
ax.set_xlabel('156 cm'); ax.set_ylabel('216 cm')
ax.set_title('Window tiled with 12 cm squares (13 × 18)')
ax.grid(False)
fig.tight_layout()
out = Path(__file__).resolve().parent.parent / 'figs' / '5.1.31.png'
out.parent.mkdir(exist_ok=True)
fig.savefig(out, dpi=300, bbox_inches='tight')
