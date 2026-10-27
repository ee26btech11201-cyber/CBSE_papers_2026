from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(.02,1.5,700); y=x**x; c=1/np.e
fig,ax=plt.subplots(figsize=(4.8,3.4)); ax.plot(x,y,label='$x^x$'); ax.scatter([c],[c**c],color='crimson',zorder=3,label='$x=1/e$')
ax.axvline(c,color='gray',ls='--'); ax.grid(alpha=.3); ax.legend(fontsize=8)
ax.set(xlabel='$x>0$',ylabel='$f(x)$',title='$x^x$ decreases then increases'); fig.tight_layout()
out=Path(__file__).resolve().parent.parent/'figs'/'4.1.23.png'; fig.savefig(out,dpi=250)
print('f\'(x)=x^x(1+ln x); increasing when x>1/e. Figure:',out)
