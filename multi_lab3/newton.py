import numpy as np
from typing import Callable
from autograd import hessian
from scipy.optimize import approx_fprime

"""static numerics::vector_f64 newtone_raphson (function_nd function, const numerics::vector_f64& x_start, const F64 eps, const I32 max_iters)
{
	numerics::vector_f64 x_i(x_start);
	numerics::vector_f64 x_i_1;
	numerics::vector_f64 grad ;
	numerics::matrix_f64 hess(1, 1);
	I32 cntr = 0;
	for (; cntr <= max_iters; cntr++)
	{
		grad = numerics::vector_f64::gradient(function, x_i, eps);
		hess = numerics::matrix_f64::invert(numerics::matrix_f64::hessian(function, x_i, eps));
		x_i_1 = x_i - (hess * grad);
		if (numerics::vector_f64::distance(x_i_1, x_i) < 2 * eps) break;
		x_i = x_i_1;
	}
#if DISPLAY_PROGRES
	std::cout << "\nNewtone-Raphson method iterations number : " << cntr << "\n";
#endif
	return (x_i_1 + x_i) * 0.5;
}"""

def numerical_hessian(f, x, eps=1e-5):
    n = len(x)
    H = np.zeros((n, n))
    for i in range(n):
        def partial_i(x):
            return approx_fprime(x, lambda x: f(x), eps)[i]
        H[i] = approx_fprime(x, partial_i, eps)
    return H

def newton_raphson(func: Callable[[np.ndarray], float], start_x: np.ndarray, acc: float = 1e-5, max_iters: int = 100) -> np.ndarray:
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