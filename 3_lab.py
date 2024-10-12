from multi_lab3 import gold_sec, bisect,test_f, bounded_f, fibbonachi, per_coord_descend, newton_raphson, conj_gradient_descend, gradient_descend
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
    init_x_ar = np.array([0, 0], dtype = float)
    next_x_ar = np.array([5, 3], dtype = float)
    x_start = np.array([-14, -33.98], dtype = float)
    x_nr_start = np.array([-12.0, -15.0], dtype = float)
    print(bisect(test_f, next_x_ar, init_x_ar))
    print(gold_sec(test_f, next_x_ar, init_x_ar))
    print(fibbonachi(test_f, next_x_ar, init_x_ar, 0))
    print(per_coord_descend(test_f, x_start))
    print(gradient_descend(test_f, x_start))
    print(conj_gradient_descend(test_f, x_start))
    print(newton_raphson(bounded_f, x_nr_start))
    #meme = fibbonachi(test_f, next_x_ar, init_x_ar)
    #print(draw_graph(test_f, next_x_ar, init_x_ar, 100, [(meme, test_f(meme))]))