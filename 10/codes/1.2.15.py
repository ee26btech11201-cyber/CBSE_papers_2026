# code by A.Chaitanya
"""Plot the kite configuration and calculate height and ground distance."""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
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

fig,ax=plt.subplots(figsize=(7.2,4.0))
for U,V,color,style in ((first,kite,"navy","-"),(base,roof,"dimgray","-"),(roof,kite,"darkorange","--"),(first,base,"seagreen","-")):
    pts=line_gen(U,V); ax.plot(pts[0],pts[1],color=color,ls=style,lw=1.7)
for Q,name,off in ((first,"First boy",(-8,-17)),(kite,"Kite",(5,3)),(base,"Building base",(5,-17)),(roof,"Roof (20 m)",(5,2))):
    ax.scatter(Q[0,0],Q[1,0],color="crimson",zorder=3); ax.annotate(name,Q[:,0],xytext=off,textcoords="offset points",fontsize=8)

# Show each angle at the observer, relative to a horizontal reference ray.
ax.plot([0,7],[0,0],color="gray",ls=":",lw=1.1)
ax.add_patch(Arc((0,0),6,6,theta1=0,theta2=30,color="black",lw=1.2))
ax.text(5.1,1.3,"30°",fontsize=8,ha="center",va="center",bbox={"facecolor":"white","edgecolor":"none","pad":1})
roof_x,roof_y=roof[:,0]
ax.plot([roof_x-7,roof_x],[roof_y,roof_y],color="gray",ls=":",lw=1.1)
ax.add_patch(Arc((roof_x,roof_y),6,6,theta1=135,theta2=180,color="black",lw=1.2))
ax.text(roof_x-4.5,roof_y+1.9,"45°",fontsize=8,ha="center",va="center",bbox={"facecolor":"white","edgecolor":"none","pad":1})
ax.text(first_to_kite*.48,kite_height*.48+1.5,"60 m",fontsize=8,rotation=30,rotation_mode="anchor",bbox={"facecolor":"white","edgecolor":"none","pad":1})
ax.set(xlim=(-7,ground_distance+9),ylim=(-4,kite_height+6),xlabel="Horizontal distance (m)",ylabel="Height (m)",title="Kite seen from ground and rooftop")
ax.set_aspect("equal",adjustable="box")
ax.grid(alpha=.22); fig.tight_layout()
print(f"Kite height = 60 sin 30° = {kite_height:g} m.")
print(f"Ground distance = 60 cos 30° + (30−20) ≈ {30*sqrt3_approx + 10:.2f} m using √3=1.73.")
out=Path(__file__).resolve().parent.parent/"figs"/"1.2.15.png"
fig.savefig(out,dpi=300,bbox_inches="tight"); print(f"Figure saved to {out}")
