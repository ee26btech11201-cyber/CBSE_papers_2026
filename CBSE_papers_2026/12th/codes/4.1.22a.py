from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
p=np.pi/2; h=np.linspace(-.35,.35,700); x=p+h
f=np.ones_like(h); nz=np.abs(h)>1e-8; f[nz]=np.sin(h[nz])/h[nz]
fig,ax=plt.subplots(figsize=(4.8,3.4)); ax.plot(x,f,label=r'$\cos x/(\pi/2-x)$')
ax.scatter([p],[1],color='crimson',zorder=3,label='$f(\pi/2)=1$'); ax.axvline(p,color='gray',ls=':'); ax.grid(alpha=.3); ax.legend(fontsize=8)
ax.set(xlabel='$x$',ylabel='$f(x)$',title='Continuity at $x=\pi/2$'); fig.tight_layout()
out=Path(__file__).resolve().parent.parent/'figs'/'4.1.22a.png'; fig.savefig(out,dpi=250)
print('With h=π/2−x, the limit is lim(sin h/h)=1=f(π/2); continuous. Figure:',out)
