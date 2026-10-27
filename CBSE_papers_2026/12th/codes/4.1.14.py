from pathlib import Path
import sys
import numpy as np
import matplotlib.pyplot as plt
sys.path.insert(0,str(Path(__file__).resolve().parent))
from CoordGeo.line.funcs import line_gen
x=np.linspace(0,8,600); y1=3-3*x; y2=2*x+5
fig,ax=plt.subplots(figsize=(5,3.5)); ax.plot(x,y1,label='$3x+y=3$'); ax.plot(x,y2,label='$2x-y=-5$')
ax.fill_between(x,np.maximum(0,y1),y2,where=y2>=np.maximum(0,y1),color='lightblue',alpha=.45,label='feasible region')
ax.axhline(0,color='black',lw=.8); ax.axvline(0,color='black',lw=.8); ax.set(xlim=(0,8),ylim=(0,13),xlabel='$x$',ylabel='$y$',title='Unbounded feasible region in quadrant I'); ax.grid(alpha=.25); ax.legend(fontsize=8)
fig.tight_layout(); out=Path(__file__).resolve().parent.parent/'figs'/'4.1.14.png'; fig.savefig(out,dpi=250)
print('Region lies in the first quadrant and is unbounded; answer (A). Figure:',out)
