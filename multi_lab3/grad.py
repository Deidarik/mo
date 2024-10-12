import numpy as np
from typing import Callable
from .fib import fibbonachi
from scipy.optimize import approx_fprime
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
    x_i_1 = np.empty(shape= x_i.shape, dtype = float)
    grad = np.empty(shape= x_i.shape, dtype = float)
    cntr: int = 0
    for cntr in range(0, max_iters):
        grad = approx_fprime(x_i, func, acc)
        x_i_1 = x_i - grad
        x_i_1 = fibbonachi(func, x_i, x_i_1, 1)
        if(np.sum((x_i_1 - x_i) / np.linalg.norm(x_i_1 - x_i)) < 2 * acc): break
        x_i = np.copy(x_i_1)
    print(f"gradient descend iterations number : {cntr} \n")
    return (x_i_1 + x_i) * 0.5



"""import numpy as np
from scipy.optimize import approx_fprime

# Определение функции
def function(val):
    return (val[0] - 5) * val[0] + (val[1] - 3) * val[1]

# Массив значений x
val = np.array([2.0, 4.0])

# Задаем небольшое значение eps для вычисления градиента
eps = np.sqrt(np.finfo(float).eps)

# Вычисляем градиент с помощью конечных разностей
grad_val = approx_fprime(val, function, eps)

print("Численный градиент в точке val:", grad_val)
"""