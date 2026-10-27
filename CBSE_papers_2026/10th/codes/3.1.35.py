"""Plot the kite configuration and calculate height and ground distance."""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import sys

sys.path.insert(0,str(Path(__file__).resolve().parent))
from CoordGeo.line.funcs import line_gen

sqrt3_approx=1.73
kite_height=60*np.sin(np.deg2rad(30))
first_to_kite=60*np.cos(np.deg2rad(30))
kite_to_building=kite_height-20  # 45 degree angle from the 20 m roof
ground_distance=first_to_kite+kite_to_building
first=np.array([[0.0],[0.0]])
kite=np.array([[first_to_kite],[kite_height]])
base=np.array([[ground_distance],[0.0]])
roof=np.array([[ground_distance],[20.0]])

fig,ax=plt.subplots(figsize=(5.7,3.8))
for U,V,color,style in ((first,kite,"navy","-"),(base,roof,"dimgray","-"),(roof,kite,"darkorange","--"),(first,base,"seagreen","-")):
    pts=line_gen(U,V); ax.plot(pts[0],pts[1],color=color,ls=style,lw=1.7)
for Q,name,off in ((first,"First boy",(-8,-17)),(kite,"Kite",(5,3)),(base,"Building base",(5,-17)),(roof,"Roof (20 m)",(5,2))):
    ax.scatter(Q[0,0],Q[1,0],color="crimson",zorder=3); ax.annotate(name,Q[:,0],xytext=off,textcoords="offset points",fontsize=8)
ax.text(first_to_kite/2,8,"60 m, 30°",fontsize=8,rotation=30)
ax.text(ground_distance-13,25,"45°",fontsize=8)
ax.set(xlim=(-8,ground_distance+14),ylim=(-4,37),xlabel="Horizontal distance (m)",ylabel="Height (m)",title="Kite seen from ground and rooftop")
ax.grid(alpha=.22); fig.tight_layout()
print(f"Kite height = 60 sin 30° = {kite_height:g} m.")
print(f"Ground distance = 60 cos 30° + (30−20) ≈ {30*sqrt3_approx + 10:.2f} m using √3=1.73.")
out=Path(__file__).resolve().parent.parent/"figs"/"3.1.35.png"
fig.savefig(out,dpi=300,bbox_inches="tight"); print(f"Figure saved to {out}")
