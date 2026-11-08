# code by A.Chaitanya
import numpy as np


def gauss_jordan(matrix, rhs):
    """Solve matrix @ X = rhs by row operations on [matrix | rhs]."""
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


# Matrix system for voucher counts: x+y=60, x+3y=100.
A = np.array([[1, 1], [1, 3]], dtype=float)
b = np.array([60, 100], dtype=float)
solution = gauss_jordan(A, b)
x, y = np.rint(solution[:, 0]).astype(int)
print("Solution from Gaussian elimination:", x, y)
print(f"Rs. 1000 vouchers = {x}; Rs. 500 vouchers = {y}")
print("Check:", x + y, "vouchers and", x + 3*y, "weighted count")
