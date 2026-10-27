"""Plot the determinant of a 2x2 matrix and identify the false statement."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

# A representative nonsingular family A(t) = [[t, 1], [1, 2]].
t = np.linspace(-4, 4, 500)
determinant = 2*t - 1
fig, ax = plt.subplots(figsize=(5.1, 3.6))
ax.plot(t, determinant, color="navy", label=r"$\det A(t)=2t-1$")
ax.axhline(0, color="black", lw=.8)
ax.axvline(.5, color="crimson", ls="--", label=r"singular at $t=1/2$")
ax.set(xlabel="$t$", ylabel="$\\det A(t)$", title="Determinant: nonsingular matrices have nonzero determinant")
ax.grid(alpha=.25); ax.legend(); fig.tight_layout()
print("For any nonsingular A, det(A) != 0 and A^{-1} exists. adj(A) is also nonsingular.")
print("Thus the false statement is (A): adj A is singular.")
out=Path(__file__).resolve().parent.parent/"figs"/"5.1.5.png"
fig.savefig(out,dpi=300,bbox_inches="tight"); print(f"Figure saved to {out}")
