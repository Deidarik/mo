from typing import Callable


def bisect(func: Callable[[float], float], lhs: float, rhs: float, eps: float = 1e-6, max_iters: int = 100) -> float:
    if(lhs > rhs): lhs, rhs = rhs, lhs
    count_iters = 0
    while (count_iters := count_iters + 1) < max_iters and rhs - lhs > 2 * eps:
        xc = (lhs + rhs) * 0.5
        if(func(xc - eps) > func(xc + eps)):
            lhs = xc
        else:
            rhs = xc
    print(f"function probes bisec : {2 * count_iters}")
    print(f"arg range: {rhs - lhs}")
    return (lhs + rhs) * 0.5