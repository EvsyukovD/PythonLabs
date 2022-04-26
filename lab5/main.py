import managermodule as m
import argparse
import utils
import md4_base as base


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--c", type=int, default=None, help="Enter hash by command prompt")
    parser.add_argument("--f", type=str, default=None, help="Enter hash by file")
    args = parser.parse_args()
    if args.c != None:
        v = utils.get_hash_tuple(args.c)
        m.check_variants(v)
        return
    if args.f != None:
        x = utils.read_hash_by_file(args.f)
        v = utils.get_hash_tuple(x)
        m.check_variants(v)
        return
    print("Хеш не определён")
    return


if __name__ == '__main__':
    main()
