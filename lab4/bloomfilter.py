import math, os, mrmr


class BloomFilter(object):
    n = 1  # число входных строк длины шаблона
    m = 1  # размер фильтра(байт)
    p = 1  # вероятность ложного положительного ответа
    k = 1  # кол-во хеш-функций
    patternlen = 0  # длина шаблона
    txtfile = None
    FILTERFILE = "filter.txt"
    hasharray = None

    def __init__(self, textfile, p, patternlen):
        self.txtfile = textfile
        self.p = p
        self.patternlen = patternlen
        self.init_params()
        self.init_file()

    def getoffset(self, string):
        hashes = self.hash(string)
        offset = [0] * self.k
        for i in range(self.k):
            offset[i] = hashes[i] % self.m
        return offset

    def contains(self, pattern):
        offset = self.getoffset(pattern)
        with open(self.FILTERFILE, "rt") as filter:
            for i in offset:
                filter.seek(i, 0)
                c = filter.read(1)
                if c == '0':
                    return False
        return True

    def hash(self, string):
        hashes = [0] * self.k
        for i in range(self.k):
            hashes[i] = mrmr.murmur_hash(string, i * 167)
        return hashes

    def init_file(self):
        j = 0
        with open(self.FILTERFILE, "w+") as filter:
            filter.truncate(self.m)
            filter.seek(0, 0)
            with open(self.txtfile, "r") as txt:
                while j <= self.n - 1:
                    txt.seek(j, 0)
                    t = txt.tell()
                    line = txt.read(self.patternlen)
                    j = j + 1
                    if not line:
                        break
                    offset = self.getoffset(line)
                    for i in range(self.k):
                        filter.seek(offset[i], 0)
                        char = filter.read(1)
                        if char != '1':
                            filter.seek(filter.tell() - 1, 0)
                            filter.write(''.join('1'))
            filter.seek(0, 0)
            for i in range(self.m):
                filter.seek(i, 0)
                char = filter.read(1)
                if char != '1':
                    filter.seek(filter.tell() - 1, 0)
                    filter.write(''.join('0'))

    def init_params(self):
        N = os.path.getsize(self.txtfile)  # кол-во символов в тексте
        self.n = N - self.patternlen + 1
        l = math.log(float(1 / self.p))
        l2 = math.log(2)
        self.m = (self.n * l) / (l2 ** 2)
        self.m = math.ceil(self.m)
        self.k = math.ceil(l / l2)
