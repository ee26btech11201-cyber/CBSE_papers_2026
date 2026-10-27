from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from CoordGeo.conics.funcs import parab_gen
from CoordGeo.line.funcs import line_gen

# p(x)=-0.0025x^2-0.025x+136, expressed around its vertex.
a, b, c = -0.0025, -0.025, 136.0
xA = -b/(2*a)
yA = a*xA*xA+b*xA+c
roots = np.sort(np.roots([a,b,c]).astype(float))
x = np.linspace(roots[0], roots[1], 700)
t = x - xA
# parab_gen(t,1/a) returns t^2/(1/a) = a*t^2.
y = parab_gen(t, 1/a) + yA
P = np.array([roots[0], 0.]); Q = np.array([roots[1], 0.]); A = np.array([xA, yA])
baseline = line_gen(P, Q)
fig, ax = plt.subplots(figsize=(9,5))
ax.plot(x,y,color='royalblue',lw=2,label=r'$p(x)=-0.0025x^2-0.025x+136$')
ax.plot(baseline[0],baseline[1],color='gray',lw=1)
ax.scatter([P[0],Q[0],A[0]],[P[1],Q[1],A[1]],color=['darkorange','darkorange','crimson'],zorder=3)
ax.annotate(f'P({P[0]:.2f}, 0)',P,xytext=(0,-20),textcoords='offset points',ha='center')
ax.annotate(f'Q({Q[0]:.2f}, 0)',Q,xytext=(0,-20),textcoords='offset points',ha='center')
ax.annotate(f'A({A[0]:.0f}, {A[1]:.4f})',A,xytext=(0,9),textcoords='offset points',ha='center')
ax.set(xlabel='x (m)',ylabel='height (m)',title='Parabolic bridge arch',
       xlim=(roots[0]-10, roots[1]+10), ylim=(-18, 160))
ax.grid(True,ls=':',alpha=.6); ax.legend(fontsize=8)
fig.tight_layout()
out=Path(__file__).resolve().parent.parent/'figs'/'5.1.36.png'
out.parent.mkdir(exist_ok=True)
fig.savefig(out,dpi=300,bbox_inches='tight')
