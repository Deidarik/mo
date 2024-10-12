from typing import Callable
import numpy as np
import numba

#@numba.njit(fastmath=True)
def bisect(func: Callable[[np.ndarray], float], lhs: np.ndarray, rhs: np.ndarray, eps: float = 1e-5, max_iters: int = 100) -> np.ndarray:
    count_iters = 0
    dist = np.sum((rhs-lhs)*eps/np.linalg.norm(rhs - lhs))
    while (count_iters := count_iters + 1) < max_iters and np.linalg.norm(rhs - lhs) > 2 * eps:
        xc = (lhs + rhs) * 0.5
        if(func(xc - dist) > func(xc + dist)):
            lhs = xc
        else:
            rhs = xc
    print(f"function probes bisec : {2 * count_iters}")
    print(f"arg range: {np.linalg.norm(rhs - lhs)}")
    return (lhs + rhs) * 0.5