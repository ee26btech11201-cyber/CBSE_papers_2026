# code by A.Chaitanya
import cvxpy as cp

# The vector equations reduce to ||b||^2 = 2. Let r = ||b|| >= 0.
r = cp.Variable(nonneg=True, name="norm_b")
problem = cp.Problem(cp.Maximize(r), [cp.square(r) <= 2])
problem.solve()

if problem.status not in (cp.OPTIMAL, cp.OPTIMAL_INACCURATE):
    raise RuntimeError(f"CVXPY did not find an optimum: {problem.status}")

print(f"||b|| = {r.value:.6f}")
print("The matching choice is b): ||b|| = sqrt(2).")
