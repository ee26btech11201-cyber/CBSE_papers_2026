"""Plot f(x)=(x-3)/(x+1) and its excluded vertical asymptote."""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

x1=np.linspace(-8,-1.05,500);x2=np.linspace(-.95,8,500)
f=lambda x:(x-3)/(x+1)
fig,ax=plt.subplots(figsize=(5.3,3.8))
ax.plot(x1,f(x1),color="navy",label=r"$f(x)=\frac{x-3}{x+1}$")
ax.plot(x2,f(x2),color="navy")
ax.axvline(-1,color="crimson",ls="--",label=r"$x=-1$ excluded")
ax.axhline(1,color="gray",ls=":",label=r"horizontal asymptote $y=1$")
ax.set(xlim=(-8,8),ylim=(-8,8),xlabel="$x$",ylabel="$f(x)$",title=r"$f'(x)=4/(x+1)^2>0$ on each domain interval")
ax.grid(alpha=.25);ax.legend(fontsize=8);fig.tight_layout()
print("f'(x)=4/(x+1)^2>0 for all x != -1; f is increasing on (-∞,-1) and (-1,∞).")
out=Path(__file__).resolve().parent.parent/"figs"/"5.1.23.png"
fig.savefig(out,dpi=300,bbox_inches="tight");print(f"Figure saved to {out}")
