import matplotlib.pyplot as plt
import numpy as np


def dbr_spectrum(n1, n2, round_trip_loss=0.1):
    r = (n1 - n2) / (n1 + n2)
    t = 2 * np.sqrt(n1 * n2) / (n1 + n2)

    t12 = 1 / t * np.matrix([[1, r], [r, 1]])
    t22 = 1 / t * np.matrix([[1, -r], [-r, 1]])
    return t12, t22
