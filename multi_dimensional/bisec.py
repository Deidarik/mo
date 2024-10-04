from typing import Callable
import numpy as np

def bisect(func, left, right, eps: float = 1e-5, max_iters: int = 100):
    lhs, rhs = (right, left) if right[0] < left[0] else (left, right)
    count_iters = 0
    print((rhs-lhs)/np.linalg.norm(rhs - lhs))
    while (count_iters := count_iters + 1) < max_iters and np.linalg.norm(rhs - lhs) > 2 * eps:
        xc = (lhs + rhs) * 0.5
        if(func(xc - eps) > func(xc + eps)):
            lhs = xc
        else:
            rhs = xc
    print(f"function probes bisec : {2 * count_iters}")
    print(f"arg range: {np.linalg.norm(rhs - lhs)}")
    return (lhs + rhs) * 0.5