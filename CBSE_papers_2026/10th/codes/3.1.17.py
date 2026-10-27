"""Plot the equilateral triangle and calculate B,C for Question 3.1.17."""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from CoordGeo.line.funcs import line_gen

h = 5*np.sqrt(3)/2
A = np.array([[0.0], [h]])
D = np.array([[0.0], [0.0]])
side = 2*h/np.sqrt(3)
B = np.array([[-side/2], [0.0]])
C = np.array([[side/2], [0.0]])

fig, ax = plt.subplots(figsize=(4.7, 4.2))
for U,V in ((A,B),(A,C),(B,C),(A,D)):
    pts = line_gen(U,V)
    ax.plot(pts[0], pts[1], color="navy", lw=1.7)
for P,label,off in ((A,"A (0, 5√3/2)",(5,4)),(B,"B (-5/2, 0)",(-60,-15)),
                    (C,"C (5/2, 0)",(5,-15)),(D,"D (0, 0)",(5,-15))):
    ax.scatter(P[0,0],P[1,0],color="crimson",zorder=3)
    ax.annotate(label,(P[0,0],P[1,0]),xytext=off,textcoords="offset points",fontsize=8)
ax.set(xlim=(-4,4),ylim=(-1,6),xlabel="$x$",ylabel="$y$",title="Equilateral triangle with median AD")
ax.set_aspect("equal",adjustable="box"); ax.grid(alpha=.25); fig.tight_layout()
print(f"Altitude h={h:.4f}; side=2h/√3={side:.4f}.")
print("B=(-5/2, 0), C=(5/2, 0); option (B).")
out=Path(__file__).resolve().parent.parent/"figs"/"3.1.17.png"
fig.savefig(out,dpi=300,bbox_inches="tight"); print(f"Figure saved to {out}")
