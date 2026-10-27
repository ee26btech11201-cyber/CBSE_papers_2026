import sympy as sp
A=sp.Matrix([[3,2,0],[1,4,0],[0,0,5]])
result=A**2-7*A+10*sp.eye(3)
print('A^2 - 7A + 10I =')
sp.pprint(result)
