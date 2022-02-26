from SortFile import Sort as s
from DataHelperFile import DataHelper as dh
class Check(object) :
      def biggerThenOrEqual(hash1,hash2) :
          return dh.getKey(hash1) >= dh.getKey(hash2)
      def lowerThenOrEqual(hash1,hash2) :
          return dh.getKey(hash1) <= dh.getKey(hash2)
      def equal(hash1,hash2) :
          return dh.getKey(hash1) == dh.getKey(hash2)
      def checkSort(data,flag) :
          if flag == 0 :
             for i in range(len(data) - 1) :
                 if not Check.biggerThenOrEqual(data[i],data[i + 1]) :
                     return False
          if flag == 1 :
             for i in range(len(data) - 1) :
                 if not Check.lowerThenOrEqual(data[i],data[i + 1]) :
                     return False
          return True
      @staticmethod
      def checkSorts() :
          name = 'Hash00.txt'
          data = dh.readFile(name)
          s.quickSort(data,0,len(data) - 1,True)
          with open("Быстрая сортировка по возр.txt",'wt') as f:
               for l in data :
                   f.writelines(str(l) + '\n');
          print('Быстрая сортировка по возр : ' + str(Check.checkSort(data,1)))
          s.quickSort(data,0,len(data) - 1,False)
          with open("Быстрая сортировка по убыв.txt",'wt') as f:
               for l in data :
                   f.writelines(str(l) + '\n');
          print('Быстрая сортировка по убыв : ' + str(Check.checkSort(data,0)))
          s.mergeSort(data,0,len(data) - 1,True)
          with open("Cортировка слиянием по возр2.txt",'wt') as f:
               for l in data :
                   f.writelines(str(l) + '\n');
          print('Cортировка слиянием по возр : ' + str(Check.checkSort(data,1)))
          s.mergeSort(data,0,len(data) - 1,False)
          with open("Cортировка слиянием по убыв2.txt",'wt') as f:
               for l in data :
                   f.writelines(str(l) + '\n');
          print('Cортировка слиянием по убыв : ' + str(Check.checkSort(data,0)))
          return

if __name__ == "__main__" :
    Check.checkSorts();

          
      
          