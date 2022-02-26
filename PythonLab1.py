from SortFile import Sort as s;
from DataHelperFile import DataHelper as dh;
from multiprocessing import Process;
import time;

def quickSort(data,name) :
    s.quickSort(data, 0, len(data) - 1, False);
    dh.appendToFile(name, data);
    dh.appendToFile(name, ['\n']);
    s.quickSort(data, 0, len(data) -  1, True);
    dh.appendToFile(name, data);
    dh.appendToFile(name,['\n']);

def mergeSort(data,name) : 
    s.mergeSort(data, 0, len(data) - 1, False);
    dh.appendToFile(name, data);
    dh.appendToFile(name, ['\n']);
    s.mergeSort(data, 0, len(data) -  1, True);
    dh.appendToFile(name, data);
    dh.appendToFile(name,['\n']);

if __name__ == "__main__" :
    print('Введите имя файла:');
    name = input();
    data = dh.readFile(name);
    print('File : %s' %(name));
    dataCopy = data.copy();

    name = 'Sort.txt'; 
    f = open(name,'wt');
    f.write('QuickSort: \n');
    f.close();
    
    qs = Process(target=quickSort,args=(data,name));
    t = time.time_ns();
    qs.start();
    qs.join();
    print('Time qs(s) : %0.5f' %((float)(time.time_ns() - t) / 1000000000.0));
    
    f = open(name,'at');
    f.write('MergeSort: \n');
    f.close();
    
    ms = Process(target=mergeSort,args=(dataCopy,name));
    t = time.time_ns();
    ms.start();
    ms.join();
    print('Time ms(s) : %0.5f' %((float)(time.time_ns() - t) / 1000000000.0));