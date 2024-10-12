import numpy as np


def test_f(val: np.ndarray) -> float:
    return sum((xi - i) * xi for i, xi in enumerate(val.flat))
    # return (val[0] - 5) * val[0] + (val[1] - 3) * val[1]