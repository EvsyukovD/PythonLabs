import numpy as np
import matrix as m
import argparse
import generator as gen


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(dest='mode', default=None, type=str, help='Какой режим работы: '
                                                                  'с : сохранить матрицу из командной строки в .npy,'
                                                                  'f : считать матрицы из файлов типа .npy'
                                                                  'g : сгенерировать матрицу заданного разиера')
    args = parser.parse_args()
    if args.mode == 'g':
        n = int(input("Введите размер\n"))
        filename = input('Введите название файла\n')
        if n < 0 or n % 2 == 1:
            print("Размер неправильный")
            return
        gen.generate(n, filename)
        return
    if args.mode == 'c':
        size = int(input("Введите размер\n"))
        if size % 2 == 1 or size < 0:
            print('Размер неправильный')
            return
        res = m.entermatrix(size)
        filename = input('Введите название файла\n')
        np.save(filename, res)
        return
    if args.mode == 'f':
        name1 = input("Имя 1-го файла\n")
        name2 = input("Имя 2-го файла\n")
        a = np.load(name1)
        b = np.load(name2)
    m.work(a, b)
    return


if __name__ == '__main__':
    main()
