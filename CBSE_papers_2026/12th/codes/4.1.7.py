from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-1,1,800); y=np.sin(x)/x+np.cos(x)
y[np.abs(x)<1e-10]=2
fig,ax=plt.subplots(figsize=(5,3.5)); ax.plot(x,y,label=r'$\sin x/x+\cos x$')
ax.scatter([0],[2],color='crimson',zorder=4,label='defined value $k=2$')
ax.axvline(0,color='gray',lw=.7); ax.grid(alpha=.3); ax.legend(fontsize=8)
ax.set(xlabel='$x$ (radians)',ylabel='$f(x)$',title='Continuity at $x=0$')
fig.tight_layout(); out=Path(__file__).resolve().parent.parent/'figs'/'4.1.7.png'; fig.savefig(out,dpi=250)
print('lim(x→0) [sin(x)/x+cos(x)]=2, hence k=2. Figure:',out)
