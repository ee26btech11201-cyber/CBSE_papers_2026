"""Draw the two-circle tangent configuration and calculate Question 4.1.33."""
from pathlib import Path
import sys
import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from CoordGeo.conics.funcs import circ_gen
from CoordGeo.line.funcs import line_gen

# Match the diagram data using Q=(0,0), B=(35,0), M=(0,13), N=(35,8).
Q=np.array([[0.],[0.]])
B=np.array([[35.],[0.]])
M=np.array([[0.],[13.]])
N=np.array([[35.],[8.]])
rM,rN=13.,8.
# Unit normal for the shared upper tangent: n.(N-M)=rM-rN=5.
d=(N-M).ravel(); perp=np.array([-d[1],d[0]])
unit_n=(5/(d@d))*d + np.sqrt(1-25/(d@d))*perp/np.linalg.norm(perp)
# Tangency points on each circle, both on the same common tangent.
P=M+rM*unit_n.reshape(2,1)
A=N+rN*unit_n.reshape(2,1)
# Intersection of the common upper tangent with the base tangent (schematic).
x_intercept=(unit_n @ M.ravel() + rM)/unit_n[0]
T=np.array([[x_intercept],[0.]])

fig,ax=plt.subplots(figsize=(6.2,4.2))
for C,r,col in ((M,rM,"steelblue"),(N,rN,"darkorange")):
    cc=circ_gen(C,r); ax.plot(cc[0],cc[1],color=col,lw=1.7)
ax.plot(*line_gen(Q,T),color="black",lw=1.5)
ax.plot(*line_gen(P,T),color="black",lw=1.5)
ax.plot(*line_gen(M,N),color="seagreen",ls="--",label=r"$MN$")
for p,name,off in ((P,"P",(-8,7)),(A,"A",(5,5)),(Q,"Q",(-12,-14)),(B,"B",(4,-14)),(T,"T",(5,-14)),(M,"M",(-14,2)),(N,"N",(4,2))):
    ax.scatter(p[0],p[1],s=17,color="crimson",zorder=4)
    ax.annotate(name,p,xytext=off,textcoords="offset points")
ax.text(2,6.5,"13 cm"); ax.text(36,3.5,"8 cm"); ax.text(15,-1.8,"35 cm")
ax.set_title("Common tangents to two circles")
ax.set_aspect("equal",adjustable="box"); ax.set_xlim(-15,98); ax.set_ylim(-3,29)
ax.axis("off"); ax.legend(loc="upper right"); fig.tight_layout()

tb=80-35
mn=float(np.linalg.norm(N-M))
pa=80-tb
print("(i) MQBN is a right trapezium.")
print(f"(ii) MN is not parallel to PA: their perpendicular distances to the common tangent are 5 cm apart (13 != 8).")
print(f"(iii) TB = TQ - BQ = 80 - 35 = {tb} cm")
print(f"(iv) MN = sqrt(35^2 + (13-8)^2) = {mn:.2f} cm = 25*sqrt(2) cm")
print(f"Consistency check: the circles and common tangents in the diagram imply TQ about {x_intercept:.1f} cm, not the printed 80 cm.")
out=Path(__file__).resolve().parent.parent/"figs"/"4.1.33.png"
fig.savefig(out,dpi=300,bbox_inches="tight")
print(f"Figure saved to {out}")
