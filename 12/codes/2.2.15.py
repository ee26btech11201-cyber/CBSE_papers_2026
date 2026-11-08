# code by A.Chaitanya
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import numpy as np
import matplotlib.pyplot as plt
from CoordGeo.line.funcs import line_gen

fig = plt.figure(figsize=(9, 4.3))
ax1 = fig.add_subplot(121, projection="3d")
ax2 = fig.add_subplot(122, projection="3d")

# (a) Solve p1 + t*d1 = p2 + s*d2 using least squares, then check the residual.
p1, d1 = np.array([-3., 1., 5.]), np.array([-3., 1., 5.])
p2, d2 = np.array([-1., 2., 5.]), np.array([-1., 2., 5.])
t, s = np.linalg.lstsq(np.column_stack((d1, -d2)), p2 - p1, rcond=None)[0]
intersection_1 = p1 + t * d1
intersection_2 = p2 + s * d2
if not np.allclose(intersection_1, intersection_2):
    print(f"(a) The lines do not intersect; closest-point residual = {np.linalg.norm(intersection_1 - intersection_2):.6g}")
else:
    intersection = (intersection_1 + intersection_2) / 2
    print(f"(a) Intersection parameters: t = {t:.0f}, s = {s:.0f}")
    print(f"    Intersection point: ({intersection[0]:.0f}, {intersection[1]:.0f}, {intersection[2]:.0f})")
for p, d, color, label in [(p1, d1, "tab:blue", r"$L_1$"), (p2, d2, "tab:orange", r"$L_2$")]:
    # Extend each displayed segment so the computed intersection is visible.
    pts = line_gen(p - 2 * d, p + d)
    ax1.plot(*pts, color=color, label=label)
ax1.scatter(*intersection, color="crimson", s=25, label="computed intersection")
ax1.set_title("2.2.15(a): intersecting lines")
ax1.legend(fontsize=7)

# (b) Compute the perpendicular separation, area, and unknown direction ratio.
a1 = np.array([1., 2., -4.]); a2 = np.array([3., 3., -5.]); b = np.array([2., 3., 6.])
v = a2 - a1
u = v - (v @ b) / (b @ b) * b  # perpendicular separation between lines
side = np.linalg.norm(u)
area = side**2
other_direction = np.array([-3., 6., 0.])
p_value = -(other_direction @ b) / b[2]
print(f"(b) Square side length = {side:.6f} (exactly sqrt(293)/7)")
print(f"    Square area = {area:.6f} (exactly 293/49)")
print(f"    Perpendicular direction ratio p = {p_value:.0f}")
edge = b / np.linalg.norm(b) * side
corners = np.array([a1, a1 + u, a1 + u + edge, a1 + edge, a1])
ax2.plot(*corners.T, color="tab:green", marker="o")
ax2.set_title(rf"2.2.15(b): square; area {area:.3f}, $p={p_value:.0f}$")
for ax in (ax1, ax2):
    ax.set_xlabel("x"); ax.set_ylabel("y"); ax.set_zlabel("z")
fig.tight_layout(); out = Path(__file__).resolve().parent.parent / "figs" / "2.2.15.png"
fig.savefig(out, dpi=220)
