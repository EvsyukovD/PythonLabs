
import argparse
import binascii

from managermodule import *
import md4_base

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(dest='hash', type=str, help='Образ пароля')
    #parser.add_argument('-t', '--threads', dest='threads', type=int, default=4, help='Number of threads')
    args = parser.parse_args()
    h = args.hash
    check_variants(binascii.unhexlify(h))


if __name__ == '__main__':
    main()
