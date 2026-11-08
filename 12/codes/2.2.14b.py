# code by A.Chaitanya
import numpy as np


def gauss_jordan(matrix, rhs):
    """Solve matrix @ X = rhs with Gaussian elimination and row reduction."""
    augmented = np.column_stack((matrix.astype(float), rhs.astype(float)))
    rows, columns = matrix.shape
    for pivot_col in range(columns):
        pivot_row = pivot_col + np.argmax(np.abs(augmented[pivot_col:, pivot_col]))
        if abs(augmented[pivot_row, pivot_col]) < 1e-12:
            raise ValueError("The coefficient matrix is singular.")
        augmented[[pivot_col, pivot_row]] = augmented[[pivot_row, pivot_col]]
        augmented[pivot_col] /= augmented[pivot_col, pivot_col]
        for row in range(rows):
            if row != pivot_col:
                augmented[row] -= augmented[row, pivot_col] * augmented[pivot_col]
    return augmented[:, columns:]


P = np.array([[2, -1], [3, 4]], dtype=int)
Q = np.array([[5, 2], [7, 4]], dtype=int)
R = np.array([[2, 5], [3, 8]], dtype=int)
PQ = P @ Q
S = np.rint(gauss_jordan(R, PQ)).astype(int)
print("PQ =")
print(PQ)
print("S from Gaussian elimination in R S = P Q:")
print(S)
print("Verification PQ - RS =")
print(PQ - R @ S)
