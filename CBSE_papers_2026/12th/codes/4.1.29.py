from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
# constraints: y<=300-x, y<=600-3x, y<=x+100, x,y>=0
verts=np.array([[0,0],[0,100],[100,200],[150,150],[200,0]],float)
val=200*verts[:,0]+120*verts[:,1]; k=int(np.argmax(val)); opt=verts[k]
fig,ax=plt.subplots(figsize=(5,3.7)); x=np.linspace(0,320,500)
ax.plot(x,300-x,label='$x+y=300$'); ax.plot(x,600-3*x,label='$3x+y=600$'); ax.plot(x,x+100,label='$x-y=-100$')
poly=np.vstack([verts,verts[0]]); ax.fill(poly[:,0],poly[:,1],alpha=.25,color='lightblue',label='feasible region')
ax.scatter(verts[:,0],verts[:,1],s=24,color='black')
for X,Y in verts: ax.annotate(f'({X:g},{Y:g})',(X,Y),xytext=(4,4),textcoords='offset points',fontsize=7)
ax.scatter(*opt,color='crimson',zorder=4,label=f'maximum Z={val[k]:g}')
ax.set(xlim=(-10,320),ylim=(-10,340),xlabel='$x$',ylabel='$y$',title='Graphical solution of the LPP'); ax.grid(alpha=.25); ax.legend(fontsize=7); fig.tight_layout()
out=Path(__file__).resolve().parent.parent/'figs'/'4.1.29.png'; fig.savefig(out,dpi=250)
print('Vertices:',verts.tolist()); print(f'Max Z={val[k]:g} at ({opt[0]:g},{opt[1]:g}). Figure: {out}')
