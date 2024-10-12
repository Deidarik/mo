import numpy as np
from typing import Callable
from .fib import fibbonachi
"""
static numerics::vector_f64 gradient_descend
(function_nd function, const numerics::vector_f64& x_start, const F64 eps, const I32 max_iters)
{
	numerics::vector_f64 x_i(x_start);
	numerics::vector_f64 x_i_1;
	numerics::vector_f64 grad;
	I32 cntr = 0;
	for(; cntr <= max_iters; cntr++)
	{
		grad  = numerics::vector_f64::gradient(function, x_i, eps);
		x_i_1 = x_i - grad;
		x_i_1 = fibonacci(function, x_i, x_i_1, eps);
		if (numerics::vector_f64::distance(x_i_1, x_i) < 2 * eps) break;
		x_i = x_i_1;
	}
#if DISPLAY_PROGRES
	std::cout << "\ngradient descend iterations number : " << cntr << "\n";
#endif
	return (x_i_1 + x_i) * 0.5;
}
"""

def gradient_descend(func: Callable[[np.ndarray], float], start_x: np.ndarray, acc: float = 1e-5, max_iters: int = 100) -> np.ndarray:
    x_i = np.copy(start_x)
    x_i_1 = np.empty(dtype = float)
    grad = np.empty(dtype = float)
    cntr: int = 0
    for cntr in range(o, max_iters):
        grad = np.gradient(func, start_x, edge_order=acc)
        x_i_1 = x_i - grad
        x_i_1 = fibbonachi(func, x_i, x_i_1, 1)
        if(np.sum((x_i - x_i_1) / np.linalg.norm(x_i - x_i_1))): break
        x_i = np.copy(x_i_1)
        print(f"\ngradient descend iterations number : {cntr}\n")
        return (x_i_1 + x_i) * 0.5
