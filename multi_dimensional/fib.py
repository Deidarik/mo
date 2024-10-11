from typing import Callable, Tuple
import numpy as np

def fib_pair(ratio: float) -> Tuple[float,float,int]:
    fn_1, fn = 1, 1
    count_iter = 0
    while(fn < ratio):
        count_iter += 1
        fn_1, fn = fn,fn + fn_1
    return fn, fn_1, count_iter


def fib_ref(fn_1: float,fn: float) -> Tuple[float,float]:
    return fn - fn_1, fn_1


def fibbonachi(func: Callable[[float], float], left: float, right: float, mode: int = 0,  eps: float = 1e-5, max_iters: int = 100) -> float:
    lhs, rhs = (right, left) if right[0] < left[0] else (left, right)
    dist = np.linalg.norm(rhs - lhs)
    ratio = dist / eps
    fn_plus_1, fn, count_iter = fib_pair(ratio)
    xl = lhs + (rhs - lhs) * (fn_plus_1 - fn) / fn_plus_1
    xr = lhs + (rhs - lhs) * fn / fn_plus_1
    fl = func(xl)
    fr = func(xr)
    fn, fn_plus_1 = fib_ref(fn, fn_plus_1)
    count_iterw = count_iter + 1
    while(count_iterw := count_iterw - 1):
        if(fl > fr):
            lhs = xl
            xl = xr
            fl = fr
            xr = lhs + (rhs - lhs) * fn / fn_plus_1
            fr = func(xr)
        else:
            rhs = xr
            xr = xl
            fr = fl
            xl = lhs + (rhs - lhs) * (fn_plus_1 - fn) / fn_plus_1
            fl = func(xl)
        fn, fn_plus_1 = fib_ref(fn, fn_plus_1)
    if not(mode):   
     print(f"function probes fib : {count_iter + 3}")
     print(f"arg range: {np.linalg.norm(rhs - lhs)}")
    return (lhs + rhs) * 0.5