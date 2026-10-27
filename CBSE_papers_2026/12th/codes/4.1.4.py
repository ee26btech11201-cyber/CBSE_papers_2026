from pathlib import Path
import sys
import numpy as np
import matplotlib.pyplot as plt
sys.path.insert(0, str(Path(__file__).resolve().parent))
from CoordGeo.line.funcs import line_gen
A=np.array([[2.],[3.]])
B=np.array([[0.],[4.]])
p=4.0
C=np.array([[p],[2.]])
line=line_gen(np.array([[-1.],[4.5]]),np.array([[5.],[1.5]]))
fig,ax=plt.subplots(figsize=(5,4))
ax.plot(line[0],line[1],color='steelblue',label='Line through A, B, C')
for P,label in [(A,'A(2,3)'),(B,'B(0,4)'),(C,'C(4,2)')]:
    ax.scatter(*P[:,0],s=45); ax.annotate(label,P[:,0],xytext=(5,7),textcoords='offset points')
ax.axhline(0,color='black',lw=.7); ax.axvline(0,color='black',lw=.7)
ax.grid(alpha=.3); ax.set(xlim=(-1,5),ylim=(0,5),xlabel='x',ylabel='y',title='Collinear points')
ax.legend(fontsize=8); fig.tight_layout()
out=Path(__file__).resolve().parent.parent/'figs'/'4.1.4.png'; fig.savefig(out,dpi=250)
print(f'p={p:g}; the collinear third point is C=({p:g},2). Figure: {out}')
