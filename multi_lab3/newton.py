import numpy as np
from typing import Callable
from autograd import hessian
from scipy.optimize import approx_fprime


def numerical_hessian(f:Callable[[np.ndarray], float], x: np.ndarray, eps: float = 1e-5) -> np.ndarray:
    n = len(x)
    H = np.zeros((n, n))
    for i in range(n):
        def partial_i(x):
            return approx_fprime(x, lambda x: f(x), eps)[i]
        H[i] = approx_fprime(x, partial_i, eps)
    return H

def newton_raphson(func: Callable[[np.ndarray], float], start_x: np.ndarray,
                    acc: float = 1e-5, max_iters: int = 100) -> np.ndarray:
    x_i = np.copy(start_x)
    x_i_1 = np.empty(shape= x_i.shape, dtype = float)
    grad = np.empty(shape= x_i.shape, dtype = float)
    hess = np.empty(shape=(1,1), dtype=float)
    cntr: int = 0
    for cntr in range(0, max_iters):
        grad = approx_fprime(x_i_1, func, acc)
        hess = np.linalg.inv(numerical_hessian(func, x_i))
        print(hess.shape, " ", grad.shape, (hess * grad).shape, " ", (grad * hess).shape)
        x_i_1 = x_i - (hess.dot(grad))
        if(np.sum((x_i_1 - x_i) / np.linalg.norm(x_i_1 - x_i)) < 2 * acc): break
        x_i = np.copy(x_i_1)
    print(f"Newtone-Raphson method iterations number : {cntr} \n")
    return (x_i_1 + x_i) * 0.5