import numpy as np
from .fib import fibbonachi, fib_pair, fib_ref

def per_coord_descend(func, start_x, acc = 1e-5, max_iters=100):
    x_0 = np.copy(start_x)
    x_1 = np.copy(start_x)
    step = 1.0
    opt_coord_n = 0
    for i in range(0, max_iters):
        coord_id = i % len(x_0)
        x_1[coord_id] -= acc
        y_0 = func(x_1)
        x_1[coord_id] += 2.0 * acc
        y_1 = func(x_1)
        x_1[coord_id] -= acc
        x_1[coord_id] += step if y_0 > y_1 else  -1*step
        x_i = x_0[coord_id]
        x_1 = fibbonachi(func, x_0, x_1, acc)
        x_0 = np.copy(x_1)
        if abs(x_1[coord_id] - x_i) < 2 * acc:
            opt_coord_n+=1
            if opt_coord_n == len(x_1):
                print(f"\nper coord descend iterations number : {i} \n")
                return x_0
            continue
        opt_coord_n = 0
    print(f"per coord descend iterations number : {max_iters}")
    return x_0