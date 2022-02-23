from SortFile import Sort as s;
from DataHelperFile import DataHelper as dh;
from multiprocessing import Process;
import time;

if __name__ == "__main__" :
    print('Введите имя файла:');
    name = input();
    data = dh.readFile(name);
    print('File : %s' %(name));
    
    qsDown = Process(target= s.quickSort,args=(data,0,len(data) - 1,False));#3,2,1
    msUp = Process(target= s.mergeSort,args=(data,0,len(data) - 1,True));#1,2,3
    msDown = Process(target= s.quickSort,args=(data,0,len(data) - 1,False));#3,2,1
    qsUp = Process(target= s.quickSort,args=(data,0,len(data) - 1,True));#1,2,3
    
    t = time.time_ns();
    qsDown.start();
    qsDown.join();
    print('Time qsDown(s) : %0.5f' %((float)(time.time_ns() - t) / 1000000000.0));
    
    t = time.time_ns();
    msUp.start();
    msUp.join();
    print('Time msUp(s) : %0.5f' %((float)(time.time_ns() - t) / 1000000000.0));
    
    t = time.time_ns();
    msDown.start();
    msDown.join();
    print('Time msDown(s) : %0.5f' %((float)(time.time_ns() - t) / 1000000000.0));
    
    t = time.time_ns();
    qsUp.start();
    qsUp.join();
    print('Time qsUp(s) : %0.5f' %((float)(time.time_ns() - t) / 1000000000.0));