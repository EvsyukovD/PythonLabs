from bloomfilter import BloomFilter as bf
from multiprocessing import Process
import mrmr

PROCESSES = 1


def find_offset(string, filename, patternlen):
    offset = 0
    with open(filename, "r") as f:
        f.seek(0, 0)
        while True:
            s = f.read(patternlen)
            if not s:
                return -1
            if mrmr.murmur_hash(s) == mrmr.murmur_hash(string):
                return offset
            offset = offset + 1
            f.seek(offset, 0)


def contains(filter,pattern):
    return filter.contains(pattern)

def find(filter, pattern, patternlen):
    flag = filter.contains(pattern)
    if flag:
        offset = find_offset(pattern, filter.txtfile, patternlen)
        if offset >= 0:
            print("Шаблон:" + pattern + "; отступ: " + str(offset))


def hash(pattern):
    return mrmr.murmur_hash(pattern)

def find_subs(filter, patternfile, patternlen):
    processes = [] * PROCESSES
    k = 0
    with open(patternfile, "r") as patterns:
        lines = list()
        while True:
            line = patterns.readline(patternlen)
            if not line:
                break
            if line != '\n':
                lines.append(line)
        for line in lines:
            p = Process(target=find, args=(filter, line, patternlen,))
            processes.append(p)
            p.start()
            k = k + 1
            if k == PROCESSES:
                k = 0
                for p in processes:
                    p.join()
        for i in range(k):
            processes[i].join()

