from typing import Callable
import numpy as np

PSI = 0.61803398874989484820


def gold_sec(func: Callable[[np.ndarray], float], lhs: np.ndarray, rhs: np.ndarray,
              eps: float = 1e-5, max_iters: int = 100) -> np.ndarray:
    count_iter = 0
    xl = rhs - (rhs - lhs) * PSI
    xr = lhs + (rhs - lhs) * PSI
    fl = func(xl)
    fr = func(xr)
    while(count_iter:=count_iter+1) < max_iters and np.linalg.norm(rhs - lhs) > 2 * eps:
        if(fl > fr):
            lhs = xl
            xl = xr
            fl = fr
            xr = lhs + (rhs - lhs) * PSI
            fr = func(xr)
        else:
            rhs = xr
            xr = xl
            fr = fl
            xl = rhs - (rhs - lhs) * PSI
            fl = func(xl)
    print(f"function probes golden ratio : {2 + count_iter}")
    print(f"arg range: {np.linalg.norm(rhs - lhs)}")
    return (lhs + rhs) * 0.5