import modmath as mm
import argparse


def main():
    parser = argparse.ArgumentParser(description='Программа раскладывает натуральное число на множители')
    parser.add_argument(dest='mode', type=str, help='способ записи числа: h - 16-ричный,oc - 8-ричный, dec - 10-ричный')
    parser.add_argument(dest='num', type=str, help='Число')
    args = parser.parse_args()
    p = 10
    if args.mode == 'h':
        p = 16
    if args.mode == 'oc':
        p = 8
    primes = mm.factorize(int(args.num, p))
    print(primes)
    return


if __name__ == '__main__':
    main()
