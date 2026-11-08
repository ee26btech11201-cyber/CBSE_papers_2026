# code by A.Chaitanya
import cvxpy as cp


def minimize_squared_ladder_lengths(height_1, height_2, case_name):
    """Minimize the sum of squared ladder lengths over the 20 m road."""
    x = cp.Variable(name="distance_from_shorter_pole")
    ladder_1_squared = height_1**2 + cp.square(20 - x)
    ladder_2_squared = height_2**2 + cp.square(x)
    problem = cp.Problem(
        cp.Minimize(ladder_1_squared + ladder_2_squared),
        [x >= 0, x <= 20],
    )
    problem.solve()

    if problem.status not in (cp.OPTIMAL, cp.OPTIMAL_INACCURATE):
        raise RuntimeError(f"CVXPY failed for {case_name}: {problem.status}")

    position = float(x.value)
    print(f"{case_name}: x = {position:.6f} m")
    print(f"    Minimum l1^2 + l2^2 = {problem.value:.6f} m^2")
    return position


# (iii)(a): pole heights are 22 m and 16 m.
x_a = minimize_squared_ladder_lengths(22, 16, "Case (a)")

# (iii)(b): both pole heights are 16 m.
x_b = minimize_squared_ladder_lengths(16, 16, "Case (b)")

print(f"Both cases place R at the road midpoint: x = {x_a:.6f} m and {x_b:.6f} m.")
