"""Plot the ellipse and calculate its enclosed area."""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

t=np.linspace(0,2*np.pi,700)
a,b=5.,10.
x=a*np.cos(t);y=b*np.sin(t)
fig,ax=plt.subplots(figsize=(5.2,4.0))
ax.fill(x,y,color="lightskyblue",alpha=.3)
ax.plot(x,y,color="navy",lw=2,label=r"$100x^2+25y^2=2500$")
ax.axhline(0,color="black",lw=.8);ax.axvline(0,color="black",lw=.8)
ax.scatter([-5,5,0,0],[0,0,-10,10],color="crimson",zorder=3)
ax.set(xlim=(-6,6),ylim=(-11,11),xlabel="$x$",ylabel="$y$",title="Ellipse with semi-axes 5 and 10")
ax.set_aspect("equal",adjustable="box");ax.grid(alpha=.2);ax.legend(loc="upper right",fontsize=8,framealpha=.9);fig.tight_layout()
print("The ellipse is x²/25 + y²/100 = 1; integration gives area πab = 50π ≈ 157.080 square units.")
out=Path(__file__).resolve().parent.parent/"figs"/"5.1.34.png"
fig.savefig(out,dpi=300,bbox_inches="tight");print(f"Figure saved to {out}")
