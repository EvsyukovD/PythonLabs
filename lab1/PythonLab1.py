from SortFile import Sort as s;
from DataHelperFile import DataHelper as dh;
from multiprocessing import Process;
import time;
from Check import Check as ch
def quickSort(data) :
    t = time.time_ns();
    s.quickSort(data, 0, len(data) - 1, False);
    with open("QuickSort_upToDown.txt",'wt') as f:
        for l in data :
             f.writelines(str(l) + '\n');
    s.quickSort(data, 0, len(data) -  1, True);
    with open("QuickSort_downToUp.txt",'wt') as f:
         for l in data :
             f.writelines(str(l) + '\n');
    print('Time qs(s) : %0.5f' %((float)(time.time_ns() - t) / 1000000000.0));

def mergeSort(data) : 
    t = time.time_ns();
    s.mergeSort(data, 0, len(data) - 1, False);
    with open("MergeSort_upToDown.txt",'wt') as f:
         for l in data :
             f.writelines(str(l) + '\n');
    s.mergeSort(data, 0, len(data) -  1, True);
    with open("MergeSort_downToUp.txt",'wt') as f:
         for l in data :
             f.writelines(str(l) + '\n');
    print('Time qs(s) : %0.5f' %((float)(time.time_ns() - t) / 1000000000.0));

if __name__ == "__main__" :
    print('Введите имя файла:');
    name = input();
    data = dh.readFile(name);
    print('File : %s' %(name));
    dataCopy = data.copy();
    
    qs = Process(target=quickSort,args=(data,));
    ms = Process(target=mergeSort,args=(dataCopy,));
    qs.start();
    ms.start();
    qs.join();
    ms.join();