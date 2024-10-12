import numpy as np


def test_f(val: np.ndarray) -> float:
    return sum((xi - i) * xi for i, xi in enumerate(val.flat))
    # return (val[0] - 5) * val[0] + (val[1] - 3) * val[1]

def fine_first(val: np.ndarray) -> float:
    return 1 / (5 - val[0] * 2 + val[1] * 3)

def fine_sec(val: np.ndarray) -> float:
    return 1 / (6 + val[0] * 3 - val[1])

def bounded_f(val: np.ndarray) -> float:
    return test_f(val) + fine_first(val) + fine_sec(val)