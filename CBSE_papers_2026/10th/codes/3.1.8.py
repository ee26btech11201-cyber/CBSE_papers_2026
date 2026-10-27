"""Plot the given line and all four choices for Question 3.1.8."""
from pathlib import Path
import sys
import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from CoordGeo.line.funcs import line_gen

x = np.array([[-4.0],[4.0]])
functions = {
    "Given: 2x - 6y = 7": lambda x: x/3 - 7/6,
    "(A) y = 3x - 7": lambda x: 3*x - 7,
    "(B) 2x = 9 - 6y": lambda x: -x/3 + 3/2,
    "(C) x - 3y = 7": lambda x: x/3 - 7/3,
    "(D) x = 7/2 - 3y": lambda x: -x/3 + 7/6,
}
fig,ax=plt.subplots(figsize=(6.0,4.6))
for label, f in functions.items():
    y=np.array([[f(x[0,0])],[f(x[1,0])]])
    seg=line_gen(np.vstack((x[0],y[0])),np.vstack((x[1],y[1])))
    ax.plot(seg[0],seg[1],label=label)
ax.set(xlim=(-4,4),ylim=(-10,5),xlabel="x",ylabel="y",
       title="The original line and every answer choice")
ax.grid(alpha=.3); ax.legend(fontsize=7); fig.tight_layout()
print("Only option (C) has the same slope 1/3 as the given line and a different intercept.")
out=Path(__file__).resolve().parent.parent/"figs"/"3.1.8.png"
fig.savefig(out,dpi=300,bbox_inches="tight")
print(f"Figure saved to {out}")
