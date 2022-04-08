from bloomfilter import BloomFilter as bf
import mrmr, countmodule
from multiprocessing import Process

PROCESSES = 4
def find_offset(string, filename, patternlen):
    offset = 0
    with open(filename, "r") as f:
        f.seek(0, 0)
        while True:
            s = f.read(patternlen)
            if not s:
                return -1
            if countmodule.hash(s) == countmodule.hash(string):
                return offset
            offset = offset + 1
            f.seek(offset, 0)

def find(filter, pattern, patternlen):
    flag = countmodule.contains(filter,pattern)
    if flag:
        offset = find_offset(pattern, filter.txtfile, patternlen)
        if offset >= 0:
            print("Шаблон:" + pattern + "; отступ: " + str(offset))

def work(textfile, patternfile, patternlen):
    filter = bf(textfile,0.001,patternlen)
    processes = [] * PROCESSES
    k = 0
    with open(patternfile,"r") as patterns:
       while True:
            line = patterns.readline(patternlen)
            if not line:
                break
            if line != '\n':
                p = Process(target=find, args=(filter, line, patternlen,))
                processes.append(p)
                k = k + 1
                p.start()
            if k == PROCESSES:
                k = 0
                for p in processes:
                    p.join()
       for i in range(k):
           processes[i].join()


