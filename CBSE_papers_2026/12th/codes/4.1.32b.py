import math
import numpy as np
I=(4-math.pi)/(4*math.sqrt(2))
x=np.linspace(0,1,200001)
quad=np.trapezoid(x*np.arctan(x)/(1+x*x)**1.5,x)
print(f"Exact value = (4−π)/(4√2) = {I:.10f}")
print(f"Numerical trapezoidal check = {quad:.10f}")
