from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
n=np.arange(1,10); f=n**3+2
fig,ax=plt.subplots(figsize=(4.8,3.4)); ax.scatter(n,f,s=30,label='$f(n)=n^3+2$')
for a,b in zip(n,f): ax.annotate(f'{b}',(a,b),xytext=(0,5),textcoords='offset points',ha='center',fontsize=7)
ax.set(xlabel='$n\in\mathbb{N}$',ylabel='$f(n)$',title='Integer-domain values of $n^3+2$'); ax.grid(alpha=.3); ax.legend(fontsize=8)
fig.tight_layout(); out=Path(__file__).resolve().parent.parent/'figs'/'4.1.20.png'; fig.savefig(out,dpi=250)
print('Strictly increasing on N, so one-one. Not onto: 1 is not attained (indeed f(n)≥3). Assertion true, reason false; choice (C). Figure:',out)
