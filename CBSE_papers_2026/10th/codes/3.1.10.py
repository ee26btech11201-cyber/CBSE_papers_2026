"""Plot the quadratic for both equal-root values of k."""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

root3=np.sqrt(3)
k_values=(-np.sqrt(24),np.sqrt(24))
x=np.linspace(-4,4,700)
fig,ax=plt.subplots(figsize=(5.8,4.2))
for k in k_values:
    y=root3*x**2-k*x+2*root3
    ax.plot(x,y,label=rf"$k={k:.3f}$")
    double_root=k/(2*root3)
    ax.scatter([double_root],[0],zorder=3)
    ax.annotate(rf"$x={double_root:.2f}$",(double_root,0),xytext=(5,8),
                textcoords="offset points",fontsize=8)
ax.axhline(0,color="black",lw=.8)
ax.set(xlim=(-4,4),ylim=(-2,32),xlabel="x",ylabel="y",
       title=r"$y=\sqrt{3}x^2-kx+2\sqrt{3}$ for equal roots")
ax.grid(alpha=.3); ax.legend(); fig.tight_layout()
print("Discriminant = k^2 - 24 = 0, so k = ±sqrt(24). Correct option: (A).")
out=Path(__file__).resolve().parent.parent/"figs"/"3.1.10.png"
fig.savefig(out,dpi=300,bbox_inches="tight")
print(f"Figure saved to {out}")
