import sympy as sp
x=sp.symbols("x", real=True)
# Partial fractions are found by matching coefficients.
expr=sp.Rational(1,5)/(x-1)+sp.Rational(4,5)*(x+1)/(x**2+4)
F=sp.Rational(1,5)*sp.log(sp.Abs(x-1))+sp.Rational(2,5)*sp.log(x**2+4)+sp.Rational(2,5)*sp.atan(x/2)
print("Integrand decomposes as:"); sp.pprint(expr)
print("Antiderivative:"); sp.pprint(F)
