from md4_base import *


def enumerate(j, ph, h):
    for i in range(1 << 32):
        k = struct.pack('<I', i) + struct.pack('<I', j)
        if compare(k, ph, h):
            print('Прообраз найден: ', k.hex())
            return True
    return False


def compare(k, ph, h):
    a, b, c, d = md4_strip(k)
    if (a, b, c, d) != ph:
        return False
    s = addbits(k)
    w = [Mod32(i) + Mod32(0x6ED9EBA1) for i in struct.unpack('<16I', s)]
    a = count_inv(H, a, b, c, d, w[0], 3)
    a, b, c, d = md4_round([a, b, c, d], H, w, [3, 9, 11, 15], lambda j: [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15][j])
    a += A
    b += B
    c += C
    d += D
    return (a, b, c, d) == h


def md4_strip(k):
    s = addbits(k)
    w = [Mod32(i) for i in struct.unpack('<16I', s)]
    a, b, c, d = A, B, C, D
    a, b, c, d = md4_round([a, b, c, d], F, w, [3, 7, 11, 19], lambda j: j)
    a, b, c, d = md4_round([a, b, c, d], G, [i + Mod32(0x5A827999) for i in w], [3, 5, 9, 13], lambda j: j // 4 + 4 * (j % 4))
    a = count(H, a, b, c, d, w[0] + Mod32(0x6ED9EBA1), 3)
    return a, b, c, d

