from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(4,8,500); y=np.abs(x-6); area=4.0
fig,ax=plt.subplots(figsize=(4.8,3.4)); ax.plot(x,y,color='navy',lw=2,label='$y=|x-6|$'); ax.axhline(0,color='black',lw=.8); ax.fill_between(x,0,y,alpha=.3,color='skyblue')
ax.axvline(4,color='gray',ls='--'); ax.axvline(8,color='gray',ls='--'); ax.scatter([6],[0],color='crimson')
ax.set(xlim=(3.7,8.3),ylim=(-.2,2.5),xlabel='$x$',ylabel='$y$',title=f'Enclosed area = {area:.1f}'); ax.grid(alpha=.25); ax.legend(fontsize=8); fig.tight_layout()
out=Path(__file__).resolve().parent.parent/'figs'/'4.1.33.png'; fig.savefig(out,dpi=250)
print(f'Area = ∫₄⁸|x−6|dx = {area:g} square units. Figure: {out}')
