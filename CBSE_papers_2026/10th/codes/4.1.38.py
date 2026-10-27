"""Plot the Jaipur points and calculate the requested distances and ratios."""
from pathlib import Path
import sys
import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from CoordGeo.line.funcs import line_gen

A = np.array([[-4.0], [2.0]])
B = np.array([[4.0], [-4.0]])
C = np.array([[4.0], [3.0]])
D = np.array([[-5.0], [-2.0]])
O = np.zeros((2, 1))

def distance(P, Q):
    return float(np.linalg.norm(P-Q))

round_trip = 2 * distance(C, A)
bc = distance(B, C)
bd = distance(B, D)

fig, ax = plt.subplots(figsize=(6.0, 5.2))
for P, Q, style, color, label in (
    (A, D, "-", "darkorange", "AD (x-axis crossing)"),
    (B, C, "-", "seagreen", "BC"),
    (B, D, "-", "purple", "BD"),
    (A, O, "--", "gray", "A-O-B collinearity check"),
    (O, B, "--", "gray", "_nolegend_"),
):
    ax.plot(*line_gen(P, Q), linestyle=style, color=color, label=label)
for P, name, place in ((A,"A",(-12,7)), (B,"B",(7,-13)), (C,"C",(7,5)),
                       (D,"D",(-12,-14)), (O,"O",(5,5))):
    ax.scatter(P[0,0], P[1,0], color="crimson", zorder=4)
    ax.annotate(f"{name} ({P[0,0]:.0f}, {P[1,0]:.0f})", (P[0,0],P[1,0]),
                xytext=place, textcoords="offset points", fontsize=8)
ax.axhline(0, color="black", lw=.8); ax.axvline(0, color="black", lw=.8)
ax.set(xlim=(-7,6), ylim=(-6,5), xlabel="x", ylabel="y",
       title="Jaipur locations on the Cartesian plane")
ax.set_aspect("equal", adjustable="box"); ax.grid(alpha=.25)
ax.legend(fontsize=7, loc="upper left"); fig.tight_layout()

print(f"Heera Bagh to Court and back = 2*sqrt(65) = {round_trip:.2f} map units")
print("AD is divided by the x-axis in ratio 1:1")
print(f"BC = {bc:.0f}; BD = sqrt(85) = {bd:.2f}; Birla Mandir is not equidistant from C and D")
print("A, O, B are not collinear (slopes AO = -1/2 and OB = -1).")
out = Path(__file__).resolve().parent.parent / "figs" / "4.1.38.png"
fig.savefig(out, dpi=300, bbox_inches="tight")
print(f"Figure saved to {out}")
