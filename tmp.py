import numpy as np

init_x_ar = np.array([[0, 0]], dtype = float)
next_x_ar = np.array([[5, 3]], dtype = float)
x_start = np.array([[-14, -33.98]], dtype = float)
init_x_ar = np.reshape(init_x_ar, (2, 1))
next_x_ar = np.reshape(next_x_ar, (2, 1))
x_start = np.reshape(x_start, (2, 1))

print(x_start)