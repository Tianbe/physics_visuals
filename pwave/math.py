import numpy as np


def calc_distance(x, y, x0, y0):
    return np.sqrt((x - x0) ** 2 + (y - y0) ** 2)
