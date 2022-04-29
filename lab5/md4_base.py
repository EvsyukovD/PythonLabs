A = 0x76543210
B = 0xfedcba98
C = 0x98abcdef
D = 0x01234567


def invert(x):
    res = (1 << 32) - x - 1
    return res


def F(x, y, z):
    return (x & y) | (invert(x) & z)


def G(x, y, z):
    return (x & y) | (x & z) | (y & z)


def H(x, y, z):
    return x ^ y ^ z


def addbits(strbits):
    l = len(strbits) % 512
    # strbits = bin(bits).strip('0b')
    res = strbits + '1'
    if l < 448:
        d = 447 - l
        for i in range(d):
            res += '0'
    else:
        d = l - 448
        for i in range(511 - d):
            res += '0'
    return res


def addlen(strbits, l):
    # l - length in bits
    res = strbits
    lbin = bin(l)[2: len(bin(l))]
    length = len(lbin)
    d = 64 - length
    if d < 0:
        d = 64
    for i in range(d):
        res += '0'
    if d >= 0:
        res += lbin
    return res


def splitbits(strbits):
    b = list()
    n = (int)(len(strbits) / 32)
    j = 0
    for i in range(n):
        j = i * 32
        b.append(int('0b' + strbits[j:j + 32], 2))
    return b


def extend(x, bits):
    b = bin(x)[2:len(bin(x))]
    d = bits - len(b)
    res = ''
    if d >= 0:
        for i in range(d):
            res += '0'
        res += b
    else:
        res = b[len(b) - bits:len(b)]
    return res


def rot_left(x, s):
    bits = list(x)
    for i in range(s):
        y = bits.pop(0)
        bits.append(y)
    res = ''
    for e in bits:
        res += e
    return int('0b' + res, 2)


def rot_right(x, s):
    bits = list(x)
    for i in range(s):
        y = bits.pop()
        bits.insert(0, y)
    res = ''
    for e in bits:
        res += e
    return int('0b' + res, 2)


def count(a, b, c, d, R, xk, s):
    res = (a + R(b, c, d) + xk) % (1 << 32)
    res = extend(res, 32)
    res = rot_left(res, s)
    return res


def inv_count(y, b, c, d, R, xk, s):
    f = extend(y, 32)
    prev_y = (rot_right(f, s) - R(b, c, d) - xk) % (1 << 32)
    return prev_y


def block_f(a, b, c, d, w):
    words = w.copy()
    resa = a
    resb = b
    resc = c
    resd = d
    for i in range(4):
        resa = count(resa, resb, resc, resd, F, words[4 * i], 3)
        resd = count(resd, resa, resb, resc, F, words[4 * i + 1], 7)
        resc = count(resc, resd, resa, resb, F, words[4 * i + 2], 11)
        resb = count(resb, resc, resd, resa, F, words[4 * i + 3], 19)
    return (resa, resb, resc, resd)


def block_g(a, b, c, d, w):
    words = w.copy()
    for i in range(16):
        words[i] = (words[i] + 0x5A827999) % (1 << 32)
    resa = a
    resb = b
    resc = c
    resd = d
    for i in range(4):
        resa = count(resa, resb, resc, resd, G, words[i], 3)
        resd = count(resd, resa, resb, resc, G, words[i + 4], 5)
        resc = count(resc, resd, resa, resb, G, words[i + 8], 9)
        resb = count(resb, resc, resd, resa, G, words[i + 12], 13)
    return (resa, resb, resc, resd)


def block_h(a, b, c, d, w):
    words = w.copy()
    for i in range(16):
        words[i] = (words[i] + 0x6ED9EBA1) % (1 << 32)
    resa = a
    resb = b
    resc = c
    resd = d
    for i in [0, 2, 1, 3]:
        resa = count(resa, resb, resc, resd, H, words[i], 3)
        resd = count(resd, resa, resb, resc, H, words[i + 8], 9)
        resc = count(resc, resd, resa, resb, H, words[i + 4], 11)
        resb = count(resb, resc, resd, resa, H, words[i + 12], 15)
    return (resa, resb, resc, resd)


def inv_block_h(ra, rb, rc, rd, w):
    resa = ra
    resb = rb
    resc = rc
    resd = rd
    words = w.copy()
    for i in range(16):
        words[i] = (words[i] + 0x6ED9EBA1) % (1 << 32)
    for i in [3, 1, 2, 0]:
        resb = inv_count(resb, resc, resd, resa, H, words[i + 12], 15)
        resc = inv_count(resc, resd, resa, resb, H, words[i + 4], 11)
        resd = inv_count(resd, resa, resb, resc, H, words[i + 8], 9)
        if i != 0:
            resa = inv_count(resa, resb, resc, resd, H, words[i], 3)
    return (resa, resb, resc, resd)


def md4(key, keylen=64):
    y = extend(key, keylen)
    x = addbits(y)
    x = addlen(x, keylen)
    m = splitbits(x)
    words = [0] * 16
    n = (int)(len(m) / 16)
    a = A  # a0
    b = B  # b0
    c = C  # c0
    d = D  # d0
    for i in range(n):
        for j in range(16):
            words[j] = m[i * 16 + j]
        aa = a  # ai-1
        bb = b  # bi-1
        cc = c  # ci-1
        dd = d  # di-1
        a, b, c, d = block_f(a, b, c, d, words)
        a, b, c, d = block_g(a, b, c, d, words)
        a, b, c, d = block_h(a, b, c, d, words)
        a += aa  # a2 = a1bl + a0 (ai+1 = aibl + ai-1, i = 1,2,3,...)
        a = a % (1 << 32)
        b += bb  # b1bl + b0
        b = b % (1 << 32)
        c += cc  # c1bl + c0
        c = c % (1 << 32)
        d += dd  # d1bl + d0
        d = d % (1 << 32)
    return (a, b, c, d)


def get_hash_tuple(x):
    s = bin(x)[2:len(bin(x))]
    a = int('0b' + s[0:32])
    b = int('0b' + s[32:64])
    c = int('0b' + s[64:96])
    d = int('0b' + s[96:128])
    return (a, b, c, d)
