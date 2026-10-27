"""Plot the continuous extension of the piecewise function in Question 5.1.6."""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-5,3,500)
y=x-5
fig,ax=plt.subplots(figsize=(5.1,3.6))
ax.plot(x,y,color="navy",label=r"$f(x)=x-5$")
ax.scatter([-1],[-6],color="crimson",zorder=3,label=r"$k=-6$ fills the point $(-1,-6)$")
ax.set(xlabel="$x$",ylabel="$f(x)$",title="Continuous graph at x=-1")
ax.grid(alpha=.25);ax.legend(fontsize=8);fig.tight_layout()
print("For x != -1, (x²-4x-5)/(x+1)=x-5, so continuity requires k=-6 (option D).")
out=Path(__file__).resolve().parent.parent/"figs"/"5.1.6.png"
fig.savefig(out,dpi=300,bbox_inches="tight");print(f"Figure saved to {out}")
