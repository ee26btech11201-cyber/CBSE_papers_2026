"""Plot all boundary lines and the feasible region for the assertion-reason LPP."""
from pathlib import Path
import sys
import matplotlib.pyplot as plt
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parent))
from CoordGeo.line.funcs import line_gen

x=np.linspace(-.5,8,350)
fig,ax=plt.subplots(figsize=(5.5,3.9))
ax.plot(x,3-2*x,color="royalblue",label=r"$2x+y=3$")
ax.plot(x,3-x/2,color="darkorange",label=r"$x+2y=6$ (minimum $Z=6$)")
ax.axhline(0,color="black",lw=.9,label="$y=0$")
ax.axvline(0,color="gray",lw=.9,label="$x=0$")
# Feasible set is above both lines in the first quadrant.
xf=np.linspace(0,8,200); lower=np.maximum(0,np.maximum(3-2*xf,3-xf/2))
ax.fill_between(xf,lower,8,color="lightgreen",alpha=.23,label="Feasible region (shown to y=8)")
ax.scatter([0,6],[3,0],color="crimson",zorder=3)
ax.annotate("(0,3)",(0,3),xytext=(5,6),textcoords="offset points")
ax.annotate("(6,0)",(6,0),xytext=(5,6),textcoords="offset points")
ax.set(xlim=(-.5,8),ylim=(-.5,8),xlabel="$x$",ylabel="$y$",title="LPP boundaries and minimum objective segment")
ax.grid(alpha=.25);ax.legend(fontsize=7,loc="upper right");fig.tight_layout()
print("Both corner points give Z=x+2y=6; every point on their joining segment is optimal.")
print("Assertion and Reason are true, and the Reason explains the Assertion: option (A).")
out=Path(__file__).resolve().parent.parent/"figs"/"5.1.20.png"
fig.savefig(out,dpi=300,bbox_inches="tight");print(f"Figure saved to {out}")
