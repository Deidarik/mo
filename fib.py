from typing import Callable

from tests import test_f

def fib_pair(ratio: float)->list[int,int,int]:
    fn_1,fn=1,1
    iter=0
    while(fn<ratio):
        iter+=1
        fn_1,fn=fn,fn+fn_1
    return fn, fn_1, iter

def fib_ref(fn_1: int,fn: int)->list[int,int]:
    return fn-fn_1, fn_1
def fibbonachi(func: Callable[[float], float], lhs: float, rhs: float, eps: float = 1.5e-6, max_iters: int = 100) -> float:
    if(lhs>rhs): lhs,rhs=rhs,lhs
    ratio=(rhs-lhs)/eps
    fn_plus_1,fn,count_iter=fib_pair(ratio)
    xl=lhs+(rhs-lhs)*(fn_plus_1-fn)/fn_plus_1
    xr=lhs+(rhs-lhs)*fn/fn_plus_1
    fl=func(xl)
    fr=func(xr)
    fn,fn_plus_1=fib_ref(fn,fn_plus_1)
    count_iterw=count_iter+1
    while(count_iterw := count_iterw - 1):
        if(fl>fr):
            lhs=xl
            xl=xr
            fl=fr
            xr=lhs+(rhs-lhs)*fn/fn_plus_1
            fr=func(xr)
        else:
            rhs=xr
            xr=xl
            fr=fl
            xl=lhs+(rhs-lhs)*(fn_plus_1-fn)/fn_plus_1
            fl=func(xl)
        fn,fn_plus_1=fib_ref(fn,fn_plus_1)
    print(f"function probes golden ratio : {3 + count_iter}")
    print(f"arg range: {rhs-lhs}")
    return (lhs+rhs)*0.5