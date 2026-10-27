"""Plot the line and the bounded region for Question 5.1.12."""
from pathlib import Path
import sys
import matplotlib.pyplot as plt
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parent))
from CoordGeo.line.funcs import line_gen

P=np.array([[0.],[-4.]])
Q=np.array([[1.],[-2.]])
segment=line_gen(P,Q)
x=np.linspace(-.5,1.5,300);y=2*x-4
fig,ax=plt.subplots(figsize=(5.1,3.8))
ax.plot(x,y,color="navy",label=r"$y=2x-4$")
ax.axhline(0,color="black",lw=1,label="$x$-axis")
ax.axvline(0,color="gray",lw=1,label="$y$-axis")
ax.axvline(1,color="darkorange",ls="--",label="$x=1$")
ax.fill([0,0,1,1],[0,-4,-2,0],color="lightskyblue",alpha=.55)
ax.set(xlim=(-.5,1.5),ylim=(-4.7,1),xlabel="$x$",ylabel="$y$",title="Region bounded by the line and the axes")
ax.grid(alpha=.25);ax.legend(fontsize=8);fig.tight_layout()
print("Area = integral_0^1 (4-2x) dx = 3 square units (option B).")
out=Path(__file__).resolve().parent.parent/"figs"/"5.1.12.png"
fig.savefig(out,dpi=300,bbox_inches="tight");print(f"Figure saved to {out}")
