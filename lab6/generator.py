import numpy as np
import random as rand


def generate(size, name):
    rows = [0] * size
    res = [None] * size
    for i in range(size):
        for j in range(size):
            rows[j] = rand.randint(0, 100)
        res[i] = rows.copy()
    d = np.array(res)
    np.save(name, d)
    return
