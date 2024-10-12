import numpy as np
from typing import Callable
from .fib import fibbonachi

"""
static numerics::vector_f64 conj_gradient_descend(function_nd function, const numerics::vector_f64& x_start, const F64 eps, const I32 max_iters)
{
	numerics::vector_f64 x_i(x_start);
	numerics::vector_f64 x_i_1;
	numerics::vector_f64 s_i = numerics::vector_f64::gradient(function, x_i, eps)*(-1.0), s_i_1;
	F64 omega;
	I32 cntr = 0;
	for (; cntr <= max_iters; cntr++)
	{
		x_i_1 = x_i + s_i;
		if (numerics::vector_f64::distance(x_i_1, x_i) < 2 * eps) break;
		x_i_1 = fibonacci(function, x_i, x_i_1, eps);
		s_i_1 = numerics::vector_f64::gradient(function, x_i_1, eps);
		omega = std::pow(s_i_1.magnitude(), 2) / std::pow(s_i.magnitude(), 2);
		s_i = s_i * omega - s_i_1;
		x_i = x_i_1;
	}
#if DISPLAY_PROGRES
	std::cout << "\nconj gradient descend iterations number : " << cntr << "\n";
#endif
	return (x_i_1 + x_i) * 0.5;
}

"""

def conj_gradient_descend(func: Callable[[np.ndarray], float], start_x: np.ndarray, acc: float = 1e-5, max_iters: int = 100) -> np.ndarray:
    x_i = np.copy(start_x)
    x_i_1 = np.empty(dtype = float)
    s_i = np.gradient(func, x_i_1, edge_order=acc)*(-1.0)
    x_i_1 = np.empty(dtype = float)
    omega: float
    cntr: int = 0
    for cntr in range(0, max_iters):
        x_i_1 = x_i + s_i
        if(np.sum((x_i - x_i_1) / np.linalg.norm(x_i - x_i_1))): break
        x_i_1 = fibbonachi(func, x_i, x_i_1, 1)
        s_i_1 = np.gradient(func, x_i_1, edge_oredr=acc)
        omega = np.linalg.norm(s_i_1)**2 / np.linalg.norm(s_i)**2
        s_i = s_i * omega - s_i_1
        x_i = np.copy(x_i_1)
    print(f"\nconj gradient descend iterations number :  {cntr}\n")
    return (x_i_1 + x_i) * 0.5
