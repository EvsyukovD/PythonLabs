from multiprocessing import Pool

import countmodule
from md4_base import *
CORES_NUMBER = 4

def md4_part_inv(a, b, c, d, k):
    s = b'\0'*4 + struct.pack('<I', k)
    s = addbits(s)
    w = list(map(Mod32, struct.unpack('<16I', s)))
    a = Mod32(a) - A
    b = Mod32(b) - B
    c = Mod32(c) - C
    d = Mod32(d) - D
    return block_h_inv(a, b, c, d, w)


def block_h_inv(a, b, c, d, w):
    w = [w[i] + Mod32(0x6ED9EBA1) for i in range(16)]
    for i in (3, 1, 2, 0):
        b = count_inv(H, b, c, d, a, w[i + 12], 15)
        c = count_inv(H, c, d, a, b, w[i + 4], 11)
        d = count_inv(H, d, a, b, c, w[i + 8], 9)
        if i:
            a = count_inv(H, a, b, c, d, w[i], 3)
    return a, b, c, d


def work(argv):
    return countmodule.enumerate(*argv)


def check_variants(h):
    h = struct.unpack('<4I', h)
    argv = [None] * CORES_NUMBER
    i = 0
    while i < (1 << 32):
        with Pool(processes=CORES_NUMBER) as p:
            for j in range(CORES_NUMBER):
                ph = md4_part_inv(*h, i)
                argv[j] = (i, ph, h)
                i += 1
            for t in p.imap_unordered(work, argv):
                if t:
                    p.terminate()
                    return 0
    print('Прообраз не найден')
    return -1

