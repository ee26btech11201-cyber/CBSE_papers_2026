"""Plot the marks relationships and solve Question 4.1.26(a)."""
from pathlib import Path
import sys
import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from CoordGeo.line.funcs import line_gen

# x = Kevin's marks; y = Veer's marks. The total is 36 because one
# additional mark would make the stated total 40.
x = np.array([[-1.0], [16.0]])
veer_relation = 2 * x + 6
total_relation = 36 - x
line1 = line_gen(np.vstack((x[0], veer_relation[0])),
                 np.vstack((x[1], veer_relation[1])))
line2 = line_gen(np.vstack((x[0], total_relation[0])),
                 np.vstack((x[1], total_relation[1])))
kevin, veer = np.linalg.solve(np.array([[-2, 1], [1, 1]]), np.array([6, 36]))

fig, ax = plt.subplots(figsize=(5.6, 4.2))
ax.plot(line1[0], line1[1], label=r"Veer = 2(Kevin) + 6", color="royalblue")
ax.plot(line2[0], line2[1], label=r"Veer + Kevin = 36", color="darkorange")
ax.scatter([kevin], [veer], color="crimson", zorder=3)
ax.annotate(f"({kevin:.0f}, {veer:.0f})", (kevin, veer), xytext=(7, 7),
            textcoords="offset points")
ax.set(xlim=(0, 16), ylim=(0, 40), xlabel="Kevin's marks",
       ylabel="Veer's marks", title="Graphical solution for the marks")
ax.grid(alpha=.3); ax.legend(fontsize=8); fig.tight_layout()
print(f"Kevin = {kevin:.0f} marks; Veer = {veer:.0f} marks")
out = Path(__file__).resolve().parent.parent / "figs" / "4.1.26.1.png"
fig.savefig(out, dpi=300, bbox_inches="tight")
print(f"Figure saved to {out}")
