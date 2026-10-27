"""Plot the two lines and solve Question 4.1.26(b) graphically."""
from pathlib import Path
import sys
import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from CoordGeo.line.funcs import line_gen

x = np.array([[-1.], [6.]])
y1 = 14 - 3*x
y2 = np.full_like(x, 2.)
fig, ax = plt.subplots(figsize=(5.5, 4.2))
ax.plot(*line_gen(np.vstack((x[0],y1[0])),np.vstack((x[1],y1[1]))), label=r"$3x+y=14$", color="royalblue")
ax.plot(*line_gen(np.vstack((x[0],y2[0])),np.vstack((x[1],y2[1]))), label=r"$y=2$", color="darkorange")
ax.scatter([4],[2],color="crimson",zorder=3)
ax.annotate("(4, 2)",(4,2),xytext=(7,8),textcoords="offset points")
ax.set(xlim=(-1,6),ylim=(-3,16),xlabel="x",ylabel="y",title="Graphical solution: intersection (4, 2)")
ax.grid(alpha=.3); ax.legend(); fig.tight_layout()
print("Intersection: x=4, y=2")
out=Path(__file__).resolve().parent.parent/"figs"/"4.1.26.2.png"
fig.savefig(out,dpi=300,bbox_inches="tight")
print(f"Figure saved to {out}")
