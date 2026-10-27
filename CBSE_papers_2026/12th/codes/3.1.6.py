import numpy as np

# B(adj B) = det(B) I, so the diagonal entries give det(B).
B_adj_B = np.diag([1/3, 1/3, 1/3])
det_B = float(B_adj_B[0, 0])
det_B_inverse = 1 / det_B
print(f"det(B) = {det_B:g}")
print(f"det(B^(-1)) = 1/det(B) = {det_B_inverse:g}")
