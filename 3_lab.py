from multi_dimensional import gold_sec, bisect, bounded_f, fibbonachi, per_coord_descend, newton_raphson, conj_gradient_descend, gradient_descend
import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple

"""
def draw_graph(func, x0, x1, nsteps=100, points:Tuple[Tuple[float,float], ...] = None):
    xs = np.linspace(x0, x1, nsteps)
    ys = np.array(tuple(func(x)for x in xs.flat))
    plt.plot(xs, ys)
    if points:
        for x,y in points:
            plt.plot(x, y, 'o')
    plt.xlabel('x')
    plt.xlabel('y')
    plt.show()
"""

if __name__ == "__main__":
    init_x_ar = np.array([0, 0, 0], dtype = float)
    next_x_ar = np.array([0, 5, 10], dtype = float)
    x_start = np.array([-1, -2, 3.0], dtype = float)
    # init_x_ar = np.reshape(init_x_ar, (2, 1))
    # next_x_ar = np.reshape(next_x_ar, (2, 1))
    # x_start = np.reshape(x_start, (2, 1))
    print(bisect(bounded_f, next_x_ar, init_x_ar))
    print(gold_sec(bounded_f, next_x_ar, init_x_ar))
    print(fibbonachi(bounded_f, next_x_ar, init_x_ar, 0))
    print(per_coord_descend(bounded_f, x_start))
    #meme = fibbonachi(test_f, next_x_ar, init_x_ar)
    #print(draw_graph(test_f, next_x_ar, init_x_ar, 100, [(meme, test_f(meme))]))