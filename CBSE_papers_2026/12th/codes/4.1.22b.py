from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
x1=np.linspace(1,2,200,endpoint=False); x2=np.linspace(2,3,200)
fig,ax=plt.subplots(figsize=(4.8,3.4)); ax.plot(x1,x1-1,label='$x-1$ for $x<2$'); ax.plot(x2,2*x2-3,label='$2x-3$ for $x\\geq2$')
ax.scatter([2],[1],color='crimson',zorder=4,label='$f(2)=1$'); ax.grid(alpha=.3); ax.legend(fontsize=8)
ax.set(xlabel='$x$',ylabel='$f(x)$',title='Piecewise function at $x=2$'); fig.tight_layout()
out=Path(__file__).resolve().parent.parent/'figs'/'4.1.22b.png'; fig.savefig(out,dpi=250)
print('Continuous at 2, but left derivative=1 and right derivative=2; not differentiable. Figure:',out)
