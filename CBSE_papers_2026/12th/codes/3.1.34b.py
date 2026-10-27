import numpy as np

P = np.array([[2, -1], [3, 4]], dtype=int)
Q = np.array([[5, 2], [7, 4]], dtype=int)
R = np.array([[2, 5], [3, 8]], dtype=int)
# PQ - RS = 0 implies S = R^{-1}PQ.
S = np.linalg.solve(R, P @ Q)
S = np.rint(S).astype(int)
print("S =")
print(S)
print("Verification PQ - RS =")
print(P @ Q - R @ S)
