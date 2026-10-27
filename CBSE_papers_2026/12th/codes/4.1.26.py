from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
x1=np.linspace(-6,2.8,500); x2=np.linspace(3.2,9,500)
f=lambda x:(x-2)/(x-3)
fig,ax=plt.subplots(figsize=(4.8,3.4)); ax.plot(x1,f(x1),label='$f(x)=(x-2)/(x-3)$'); ax.plot(x2,f(x2),color='C0')
ax.axvline(3,color='gray',ls='--',label='excluded $x=3$'); ax.axhline(1,color='darkorange',ls=':',label='excluded $y=1$')
ax.set_ylim(-5,7); ax.grid(alpha=.3); ax.legend(fontsize=8); ax.set(xlabel='$x$',ylabel='$f(x)$',title='Bijective map from R\\{3} to R\\{1}')
fig.tight_layout(); out=Path(__file__).resolve().parent.parent/'figs'/'4.1.26.png'; fig.savefig(out,dpi=250)
print('Inverse is x=(3y−2)/(y−1), defined for every y≠1 and never equals 3; f is one-one and onto. Figure:',out)
