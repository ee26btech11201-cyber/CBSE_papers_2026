"""Plot the polynomial in the correct option for Question 3.1.14."""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-4, 4, 500)
y = -3*x**2 - x - 6

fig, ax = plt.subplots(figsize=(5.4, 3.7))
ax.plot(x, y, color="navy", label=r"$p(x)=-3x^2-x-6$")
ax.axhline(0, color="black", lw=.8)
ax.axvline(0, color="black", lw=.8)
ax.set(xlabel="$x$", ylabel="$p(x)$", title="Polynomial matching the given sum and product")
ax.grid(alpha=.25); ax.legend(); fig.tight_layout()
print("For ax^2+bx+c, sum=-b/a=-1/3 and product=c/a=2; option (D).")
out = Path(__file__).resolve().parent.parent / "figs" / "3.1.14.png"
fig.savefig(out, dpi=300, bbox_inches="tight")
print(f"Figure saved to {out}")
