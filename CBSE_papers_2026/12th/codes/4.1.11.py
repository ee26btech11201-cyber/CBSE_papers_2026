from pathlib import Path
import sys
import numpy as np
import matplotlib.pyplot as plt
sys.path.insert(0,str(Path(__file__).resolve().parent))
from CoordGeo.line.funcs import line_gen
P=np.array([[0.],[0.]]); Q=np.array([[2.],[2.]])
curve=line_gen(P,Q)
fig,ax=plt.subplots(figsize=(4.8,3.4)); ax.plot(curve[0],curve[1],lw=2,label='$y=x$')
ax.plot([-0.2,2.2],[0,0],color='black',lw=1); ax.axvline(0,color='black',lw=.8); ax.axvline(2,color='gray',ls='--')
xx=np.linspace(0,2,200); ax.fill_between(xx,0,xx,alpha=.25,color='skyblue',label='bounded region')
ax.set(xlim=(-.2,2.2),ylim=(-.2,2.3),xlabel='$x$',ylabel='$y$',title='Area under $y=x$ on $[0,2]$'); ax.grid(alpha=.25); ax.legend(fontsize=8)
fig.tight_layout(); out=Path(__file__).resolve().parent.parent/'figs'/'4.1.11.png'; fig.savefig(out,dpi=250)
print('Area = ∫₀² x dx = 2 square units. Figure:',out)
