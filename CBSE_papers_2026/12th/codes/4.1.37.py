import sympy as sp
A=sp.Matrix([[1,1,-1],[2,3,1],[-3,1,7]])
b=sp.Matrix([3,10,-1])
print('A='); sp.pprint(A)
print('X=(length,breadth,height)='); sp.pprint(A.inv()*b)
print('det(A)=',A.det(),'; A is invertible:',A.det()!=0)
print('A^(-1)='); sp.pprint(A.inv())
print('A^2+7I='); sp.pprint(A**2+7*sp.eye(3))
