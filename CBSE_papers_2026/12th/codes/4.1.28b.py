import sympy as sp
x=sp.symbols('x', real=True)
u=(sp.sqrt(1+x**2)-sp.sqrt(1-x**2))/(sp.sqrt(1+x**2)+sp.sqrt(1-x**2))
F=sp.atan(u); G=sp.acos(x**2)
d=sp.simplify(sp.diff(F,x)/sp.diff(G,x))
print('dF/dG =',d)
