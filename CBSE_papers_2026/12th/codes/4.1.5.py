import sympy as sp
x=sp.symbols('x', real=True)
f=sp.exp(sp.exp(x))
df=sp.diff(f,x)
print('d/dx(e^(e^x)) =', sp.simplify(df))
print('Correct choice: (C) e^x e^(e^x)')
