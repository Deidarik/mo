from multi_lab3 import gold_sec, bisect,test_f, bounded_f, fibbonachi, per_coord_descend, newton_raphson, conj_gradient_descend
from multi_lab3 import  gradient_descend, fine_first, fine_sec, PenaltyFunction
import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple

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
    target = PenaltyFunction()
    target.target = test_f
    target.add_bound(fine_first)
    target.add_bound(fine_sec)
    print(newton_raphson(target.__call__, x_nr_start))
    target.clear_boundaries