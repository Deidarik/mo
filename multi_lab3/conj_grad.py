import numpy as np
from typing import Callable
from .fib import fibbonachi
from scipy.optimize import approx_fprime


def conj_gradient_descend(func: Callable[[np.ndarray], float],
                           start_x: np.ndarray, acc: float = 1e-5, max_iters: int = 100) -> np.ndarray:
    x_i = np.copy(start_x)
    x_i_1 = np.empty(shape= x_i.shape, dtype = float)
    s_i = approx_fprime(x_i, func, acc)*(-1.0)
    x_i_1 = np.empty(shape= x_i.shape, dtype = float)
    omega: float
    cntr: int = 0
    for cntr in range(0, max_iters):
        x_i_1 = x_i + s_i
        if(np.sum((x_i_1 - x_i) / np.linalg.norm(x_i_1 - x_i)) < 2 * acc): break
        x_i_1 = fibbonachi(func, x_i, x_i_1, 1)
        s_i_1 = approx_fprime(x_i_1, func, acc)
        omega = np.linalg.norm(s_i_1)**2 / np.linalg.norm(s_i)**2
        s_i = s_i * omega - s_i_1
        x_i = np.copy(x_i_1)
    print(f"conj gradient descend iterations number :  {cntr} \n")
    return (x_i_1 + x_i) * 0.5
