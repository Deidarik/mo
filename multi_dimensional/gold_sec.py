from typing import Callable
PSI = 0.61803398874989484820


def gold_sec(func: Callable[[float], float], lhs: float, rhs: float, eps: float = 1e-6, max_iters: int = 100) -> float:
    lhs, rhs = (rhs, lhs) if rhs < lhs else (lhs, rhs)
    count_iter = 0
    xl = rhs - (rhs - lhs) * PSI
    xr = lhs + (rhs - lhs) * PSI
    fl = func(xl)
    fr = func(xr)
    while(count_iter := count_iter + 1) < max_iters and rhs - lhs > 2 * eps:
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
    print(f"arg range: {rhs - lhs}")
    return (lhs + rhs) * 0.5
