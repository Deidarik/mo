from multi_dimensional import gold_sec, bisect, test_f, fibbonachi
import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple


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

if __name__ == "__main__":
    print(bisect(test_f, -2.0, 2.0))
    print(gold_sec(test_f, -2.0, 2.0))
    meme = fibbonachi(test_f, -2.0, 2.0)
    print(fibbonachi(test_f, -2.0, 2.0))
    print(draw_graph(test_f, -2.0, 2.0, 100, [(meme, test_f(meme))]))