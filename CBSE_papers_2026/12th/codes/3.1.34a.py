import numpy as np

# Matrix method for voucher counts: x+y=60, x+3y=100.
A = np.array([[1, 1], [1, 3]], dtype=int)
b = np.array([60, 100], dtype=int)
adj_A = np.array([[3, -1], [-1, 1]], dtype=int)
det_A = int(round(np.linalg.det(A)))
solution = (adj_A @ b) // det_A
x, y = map(int, solution)
print(f"A^-1 = adj(A)/det(A) =\n{adj_A}/{det_A}")
print(f"Rs. 1000 vouchers = {x}; Rs. 500 vouchers = {y}")
print("Check:", x + y, "vouchers and", x + 3*y, "weighted count")
