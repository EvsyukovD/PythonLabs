import numpy as np
from multiprocessing import Pool
import time


def split(matrix):
    n = len(matrix[0])
    n2 = n // 2
    m11 = matrix[0: n2, 0: n2]
    m12 = matrix[0: n2, n2: n]
    m21 = matrix[n2: n, 0: n2]
    m22 = matrix[n2: n, n2: n]
    return m11, m12, m21, m22


def ordinarymul(a, b):
    a11, a12, a21, a22 = split(a)
    b11, b12, b21, b22 = split(b)
    if len(a11[0]) == 1:
        s1 = (a11[0][0] + a22[0][0]) * (b11[0][0] + b22[0][0])
        s2 = (a21[0][0] + a22[0][0]) * b11[0][0]
        s3 = a11[0][0] * (b12[0][0] - b22[0][0])
        s4 = a22[0][0] * (b21[0][0] - b11[0][0])
        s5 = (a11[0][0] + a12[0][0]) * b22[0][0]
        s6 = (a21[0][0] - a11[0][0]) * (b11[0][0] + b12[0][0])
        s7 = (a12[0][0] - a22[0][0]) * (b21[0][0] + b22[0][0])
        res = np.array([[s1 + s4 - s5 + s7, s3 + s5], [s2 + s4, s1 - s2 + s3 + s6]])
        return res
    else:
        s1 = ordinarymul(a11 + a22, b11 + b22)  # (a11 + a22) * (b11 + b22)
        s2 = ordinarymul(a21 + a22, b11)  # (a21 + a22) * b11
        s3 = ordinarymul(a11, b12 - b22)  # a11 * (b12 - b22)
        s4 = ordinarymul(a22, b21 - b11)  # a22 * (b21 - b11)
        s5 = ordinarymul(a11 + a12, b22)  # (a11 + a12) * b22
        s6 = ordinarymul(a21 - a11, b11 + b12)  # (a21 - a11) * (b11 + b12)
        s7 = ordinarymul(a12 - a22, b21 + b22)  # (a12 - a22) * (b21 + b22)
        m11 = s1 + s4 - s5 + s7
        m12 = s3 + s5
        m21 = s2 + s4
        m22 = s1 - s2 + s3 + s6
        res1 = np.hstack([m11, m12])
        res2 = np.hstack([m21, m22])
        res = np.vstack([res1, res2])
        return res


def tuple_mul(tuple):
    return ordinarymul(tuple[0], tuple[1])


def multiprocmul(a, b):
    a11, a12, a21, a22 = split(a)
    b11, b12, b21, b22 = split(b)
    if len(a11[0]) == 1:
        s1 = (a11[0][0] + a22[0][0]) * (b11[0][0] + b22[0][0])
        s2 = (a21[0][0] + a22[0][0]) * b11[0][0]
        s3 = a11[0][0] * (b12[0][0] - b22[0][0])
        s4 = a22[0][0] * (b21[0][0] - b11[0][0])
        s5 = (a11[0][0] + a12[0][0]) * b22[0][0]
        s6 = (a21[0][0] - a11[0][0]) * (b11[0][0] + b12[0][0])
        s7 = (a12[0][0] - a22[0][0]) * (b21[0][0] + b22[0][0])
        res = np.array([[s1 + s4 - s5 + s7, s3 + s5], [s2 + s4, s1 - s2 + s3 + s6]])
        return res
    else:
        s = list()
        with Pool(processes=7) as pool:
            tasks = [(a11 + a22, b11 + b22),
                     (a21 + a22, b11),
                     (a11, b12 - b22),
                     (a22, b21 - b11),
                     (a11 + a12, b22),
                     (a21 - a11, b11 + b12),
                     (a12 - a22, b21 + b22)]
            for r in pool.imap(tuple_mul, tasks):
                s.append(r)
        m11 = s[0] + s[3] - s[4] + s[6]
        m12 = s[2] + s[4]
        m21 = s[1] + s[3]
        m22 = s[0] - s[1] + s[2] + s[5]
        res1 = np.hstack([m11, m12])
        res2 = np.hstack([m21, m22])
        res = np.vstack([res1, res2])
    return res


def work(a, b):
    t = time.time_ns()
    c = ordinarymul(a, b)
    t = (time.time_ns() - t) / 10 ** 9
    print("Время без распараллеливания (сек): %0.9f" % (t))
    print('Результат:')
    print(c)
    t = time.time_ns()
    c = multiprocmul(a, b)
    t = (time.time_ns() - t) / 10 ** 9
    print("Время c распараллеливанием (сек): %0.9f" % (t))
    print('Результат:')
    print(c)


def entermatrix(size):
    rows = [0] * size
    res = [None] * size
    for i in range(size):
        for j in range(size):
            print("Введите A[" + str(i) + '][' + str(j) + ']')
            rows[j] = int(input())
        res[i] = rows.copy()
    d = np.array(res)
    print("Ваша матрица:")
    print(d)
    return d
