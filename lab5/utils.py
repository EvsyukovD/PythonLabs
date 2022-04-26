import md4_base as base


def get_hash_tuple(x):
    s = base.extend(x, 128)
    a = int('0b' + s[0:32], 2)
    b = int('0b' + s[32:64], 2)
    c = int('0b' + s[64:96], 2)
    d = int('0b' + s[96:128], 2)
    return (a, b, c, d)


def read_hash_by_file(name):
    with open(name, "r") as f:
        s = f.readline().strip('\n')
        x = int(s, 16)
    return x


def get_hash(v):
    a, b, c, d = v
    s1 = base.extend(a, 32)
    s2 = base.extend(b, 32)
    s3 = base.extend(c, 32)
    s4 = base.extend(d, 32)
    return int('0b' + s1 + s2 + s3 + s4, 2)
