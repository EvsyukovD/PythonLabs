import md4_base


def md4_strip(key):
    y = md4_base.extend(key, 64)
    x = md4_base.addbits(y)
    x = md4_base.addlen(x, 64)
    m = md4_base.splitbits(x)
    words = [0] * 16
    a = md4_base.A
    b = md4_base.B
    c = md4_base.C
    d = md4_base.D
    for j in range(16):
        words[j] = m[j]
    a, b, c, d = md4_base.block_f(a, b, c, d, words)
    a, b, c, d = md4_base.block_g(a, b, c, d, words)
    a = md4_base.count(a, b, c, d, md4_base.H, (words[0] + 0x6ED9EBA1) % (1 << 32), 3)
    return (a, b, c, d)


def isequal(prev_hash_vec, key, img_hash_cort):
    a, b, c, d = md4_strip(key)
    v1 = (a, b, c, d)
    if v1 != prev_hash_vec:
        return False
    y = md4_base.extend(key, 64)
    x = md4_base.addbits(y)
    x = md4_base.addlen(x, 64)
    m = md4_base.splitbits(x)
    words = [0] * 16
    for i in range(16):
        words[i] = m[i]
    a = md4_base.inv_count(a, b, c, d, md4_base.H, (words[0] + 0x6ED9EBA1) % (1 << 32), 3)
    a, b, c, d = md4_base.block_h(a, b, c, d, words)
    a += md4_base.A
    a = a % (1 << 32)
    b += md4_base.B
    b = b % (1 << 32)
    c += md4_base.C
    c = c % (1 << 32)
    d += md4_base.D
    d = d % (1 << 32)
    v1 = (a, b, c, d)
    if v1 == img_hash_cort:
        return True
    else:
        return False


def enumerate(const_32b, prev_hash, image_hash):
    N = 1 << 32
    i = 0
    c = md4_base.extend(const_32b, 32)
    while i < N:
        j = md4_base.extend(i, 32)
        key = int('0b' + j + c, 2)
        flag = isequal(prev_hash, key, image_hash)
        if flag:
            print("Прообраз найден: " + bin(key))
            return True
        i += 1
    return False
