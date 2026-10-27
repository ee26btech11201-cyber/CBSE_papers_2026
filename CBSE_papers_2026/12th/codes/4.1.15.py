from pathlib import Path
import sys
import numpy as np
import matplotlib.pyplot as plt
sys.path.insert(0,str(Path(__file__).resolve().parent))
from CoordGeo.line.funcs import line_gen
A=np.array([[0.],[5.]]); B=np.array([[3.],[4.]])
ab=line_gen(A,B)
x=np.linspace(-.5,4,200); z=3*x+15 # objective slope -1/3, through A and B
fig,ax=plt.subplots(figsize=(4.8,3.5)); ax.plot(ab[0],ab[1],lw=3,label='optimal edge AB')
ax.plot(x,5-x/3,'--',label='parallel objective line')
for P,n in [(A,'A(0,5)'),(B,'B(3,4)')]: ax.scatter(*P[:,0],zorder=3); ax.annotate(n,P[:,0],xytext=(5,6),textcoords='offset points')
ax.axhline(0,color='black',lw=.8); ax.axvline(0,color='black',lw=.8); ax.grid(alpha=.25); ax.set(xlim=(-.2,4),ylim=(3.5,5.7),xlabel='$x$',ylabel='$y$',title='Objective lines parallel to AB'); ax.legend(fontsize=8)
fig.tight_layout(); out=Path(__file__).resolve().parent.parent/'figs'/'4.1.15.png'; fig.savefig(out,dpi=250)
print('slope(AB)=(4-5)/(3-0)=-1/3=-p/q, so q=3p; answer (C). Figure:',out)
