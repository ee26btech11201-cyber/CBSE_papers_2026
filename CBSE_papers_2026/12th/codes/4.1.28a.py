import sympy as sp
x,y=sp.symbols('x y', positive=True); yp=sp.symbols("y'")
# Log-differentiate xy = exp(x-y), then solve for y'.
solution=sp.solve(sp.Eq(1/x+yp/y,1-yp),yp)[0]
print("dy/dx =",sp.factor(solution))
