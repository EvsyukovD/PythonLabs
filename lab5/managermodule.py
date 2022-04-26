import md4_base as base
import countmodule as co
from multiprocessing import Pool

CORES_NUMBER = 4


def md4_part_inv(img_hash, key):
    resa, resb, resc, resd = img_hash
    y = base.extend(key, 64)
    x = base.addbits(y)
    x = base.addlen(x, 64)
    m = base.splitbits(x)
    words = [0] * 16
    N = 1 << 32
    for i in range(16):
        words[i] = m[i]
    resd = (resd - base.D) % N
    resc = (resc - base.C) % N
    resb = (resb - base.B) % N
    resa = (resa - base.A) % N
    resa, resb, resc, resd = base.inv_block_h(resa, resb, resc, resd, words)
    return (resa, resb, resc, resd)


def work(v):
    i, prev_hash, image_hash = v
    f = co.enumerate(i, prev_hash, image_hash)
    return f


def check_variants(image_hash):
    N = 1 << 32
    i = 0
    end_flag = False
    args = [None] * CORES_NUMBER
    while i < N and not end_flag:
        with Pool(processes=CORES_NUMBER) as pool:
            for j in range(CORES_NUMBER):
                prev_hash = md4_part_inv(image_hash, i)
                args[j] = (i, prev_hash, image_hash)
                i += 1
            for r in pool.imap_unordered(work, args):
                if r:
                    pool.terminate()
                    end_flag = True
                    break
    if not end_flag:
        print('Прообраз не найден')
    return 0
