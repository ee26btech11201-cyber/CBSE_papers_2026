from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.insert(0,str(Path(__file__).resolve().parent))
from CoordGeo.line.funcs import line_gen
# First line: (1,2,3)+t(2,3,4); second: (4,1,0)+s(5,2,1)
t=s=-1.0; P=np.array([-1.,-1.,-1.]); d1=np.array([2.,3.,4.]); d2=np.array([5.,2.,1.]); d=np.array([3.,2.,-8.])
L1=line_gen((P-.8*d1).reshape(3,1),(P+.8*d1).reshape(3,1)); L2=line_gen((P-.8*d2).reshape(3,1),(P+.8*d2).reshape(3,1)); L3=line_gen((P-.8*d).reshape(3,1),(P+.8*d).reshape(3,1))
fig=plt.figure(figsize=(5.2,4)); ax=fig.add_subplot(111,projection='3d')
ax.plot(*L1,color='steelblue',label='line 1'); ax.plot(*L2,color='darkorange',label='line 2'); ax.plot(*L3,color='green',label='required line')
ax.scatter(*P,color='crimson'); ax.text(*P,'intersection (-1,-1,-1)',fontsize=7)
ax.set(xlabel='$x$',ylabel='$y$',zlabel='$z$',title='Intersection and required parallel line'); ax.legend(fontsize=8); ax.set_box_aspect((1,1,1)); fig.tight_layout()
out=Path(__file__).resolve().parent.parent/'figs'/'4.1.35.png'; fig.savefig(out,dpi=250)
print('The given lines intersect at (-1,-1,-1). Required line: r=(-i-j-k)+λ(3i+2j−8k). Figure:',out)
