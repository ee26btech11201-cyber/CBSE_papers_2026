"""Numerically minimize and plot f(x)=(x-2)^2+5 on [-3,2]."""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize_scalar

f=lambda x:(x-2)**2+5
result=minimize_scalar(f,bounds=(-3,2),method="bounded",options={"xatol":1e-12})
# Include endpoints explicitly in case the bounded solver is near an endpoint.
candidates=[(-3,f(-3)),(2,f(2)),(result.x,result.fun)]
x_min,y_min=min(candidates,key=lambda item:item[1])
x=np.linspace(-3,2,500)
fig,ax=plt.subplots(figsize=(5.2,3.7))
ax.plot(x,f(x),color="navy",label=r"$f(x)=(x-2)^2+5$")
ax.scatter([x_min],[y_min],color="crimson",zorder=3)
ax.annotate(f"minimum ({x_min:.0f}, {y_min:.0f})",(x_min,y_min),xytext=(-75,12),textcoords="offset points")
ax.set(xlim=(-3,2.3),xlabel="$x$",ylabel="$f(x)$",title="Absolute minimum on the interval [-3, 2]")
ax.grid(alpha=.25);ax.legend();fig.tight_layout()
print(f"Minimum on [-3,2]: f({x_min:.0f})={y_min:.0f}; option (C).")
out=Path(__file__).resolve().parent.parent/"figs"/"5.1.9.png"
fig.savefig(out,dpi=300,bbox_inches="tight");print(f"Figure saved to {out}")
