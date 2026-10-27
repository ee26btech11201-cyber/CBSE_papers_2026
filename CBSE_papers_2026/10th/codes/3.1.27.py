"""Draw the circle, major sector, and shaded minor segment; calculate requested values."""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np
import sys

sys.path.insert(0,str(Path(__file__).resolve().parent))
from CoordGeo.conics.funcs import circ_gen

r=7.0
theta=np.deg2rad(120)
A=np.array([r*np.cos(np.deg2rad(210)),r*np.sin(np.deg2rad(210))])
B=np.array([r*np.cos(np.deg2rad(330)),r*np.sin(np.deg2rad(330))])
O=np.array([0.0,0.0])
major_perimeter=2*r+(240/360)*2*np.pi*r
minor_sector=(120/360)*np.pi*r*r
triangle_area=21.2
segment_area=minor_sector-triangle_area

fig,ax=plt.subplots(figsize=(4.6,4.2))
angles=np.linspace(np.deg2rad(210),np.deg2rad(330),100)
arc=np.column_stack((r*np.cos(angles),r*np.sin(angles)))
ax.add_patch(Polygon(arc,closed=True,facecolor="lightskyblue",alpha=.65,hatch="///",edgecolor="steelblue"))
circle=circ_gen(O.reshape(2,1),r)
ax.plot(circle[0],circle[1],color="navy",lw=1.5)
for pt in (A,B): ax.plot([0,pt[0]],[0,pt[1]],color="navy",lw=1.5)
for pt,label,off in ((A,"A",(-15,-8)),(B,"B",(5,-8)),(O,"O",(5,5))):
    ax.scatter(*pt,color="crimson",zorder=3); ax.annotate(label,pt,xytext=off,textcoords="offset points")
ax.text(-.8,-.55,"120°",fontsize=9)
ax.set(xlim=(-8.5,8.5),ylim=(-8.5,8.5),xlabel="$x$",ylabel="$y$",title="Circle, major sector OACB, and shaded segment")
ax.set_aspect("equal",adjustable="box"); ax.grid(alpha=.2); fig.tight_layout()
print(f"Major sector perimeter = 14 + 28π/3 = {major_perimeter:.3f} cm.")
print(f"Shaded segment area = 49π/3 - 21.2 = {segment_area:.3f} cm².")
out=Path(__file__).resolve().parent.parent/"figs"/"3.1.27.png"
fig.savefig(out,dpi=300,bbox_inches="tight"); print(f"Figure saved to {out}")
