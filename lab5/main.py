import managermodule as m
import argparse
import utils


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--c", type=str, default=None, help="Enter hash by command prompt")
    parser.add_argument("--f", type=str, default=None, help="Enter hash by file")
    args = parser.parse_args()
    if args.c != None:
        y = int(args.c, 16)
        v = utils.get_hash_tuple(y)
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
