def murmur_hash(key, seed=0):
    l = len(key)
    m = 0x5bd1e995
    r = 24
    h = seed ^ l
    data = list(key)
    i = 0
    while l >= 4:
        k = ord(data[i])
        k |= ord(data[i + 1]) << 8
        k |= ord(data[i + 2]) << 16
        k |= ord(data[i + 3]) << 24

        k *= m
        k ^= k >> r
        k *= m

        h *= m
        h ^= k
        i += 4
        l -= 4

    if l == 3:
        h ^= ord(data[2]) << 16
    if l == 2:
        h ^= ord(data[1]) << 8
    if l == 1:
        h ^= ord(data[0])
    h *= m

    h ^= h >> 13
    h *= m
    h ^= h >> 15

    return h
