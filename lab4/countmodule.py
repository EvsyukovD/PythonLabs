import mrmr


def contains(filter, pattern):
    return filter.contains(pattern)


def hash(pattern):
    return mrmr.murmur_hash(pattern)
