from DataHelperFile import DataHelper;
class Sort(object):
      def swap(a, i, j) :
          x = a[i];
          a[i] = a[j];
          a[j] = x;
          return;

      def partition(a, p, r, downToUpFlag) :
          x = a[r];
          i = p - 1;
          if downToUpFlag :
              for j in range(p, r) :
                  if DataHelper.getKey(a[j]) <= DataHelper.getKey(x) :
                     i = i + 1;
                     Sort.swap(a, i, j);
              Sort.swap(a, i + 1, r);
              return i + 1;
          else :
              for j in range(p, r) :
                  if DataHelper.getKey(a[j]) >= DataHelper.getKey(x) :
                     i = i + 1;
                     Sort.swap(a, i, j);
              Sort.swap(a, i + 1, r);
              return i + 1;

      @staticmethod
      def quickSort(a, p, r,downToUpFlag) :
          if p < r :
             q = Sort.partition(a, p, r, downToUpFlag);
             Sort.quickSort(a, p, q - 1, downToUpFlag);
             Sort.quickSort(a, q + 1, r, downToUpFlag);
          return;

      def merge(a, low, middle, high, downToUpFlag) :
          right = list();
          left = list();
          for i in range(low,high + 1) :
              if i <= middle :
                 left.append(a[i]);
              else :
                 right.append(a[i]);
          N = middle - low + 1;
          M = high - middle;
          i = 0;
          j = 0;
          k = low;#middle;
          if downToUpFlag :
             while(i < N and j < M) :
                   if DataHelper.getKey(left[i]) <= DataHelper.getKey(right[j]) :
                      a[k] = left[i];
                      i = i + 1;
                   else :
                      a[k] = right[j];
                      j = j + 1;
                   k = k + 1;
          else :
              while(i < N and j < M) :
                   if DataHelper.getKey(left[i]) >= DataHelper.getKey(right[j]) :
                      a[k] = left[i];
                      i = i + 1;
                   else :
                      a[k] = right[j];
                      j = j + 1;
                   k = k + 1;
          while(i < N) :
                a[k] = left[i];
                i = i + 1;
                k = k + 1;
          while(j < M) :
                a[k] = right[j];
                j = j + 1;
                k = k + 1;
          return;

      @staticmethod
      def mergeSort(a,low,high, downToUpFlag) :
          if high <= low :
             return;
          q = (int)((low + high) / 2);
          Sort.mergeSort(a, low, q, downToUpFlag);
          Sort.mergeSort(a, q + 1, high, downToUpFlag);
          Sort.merge(a, low, q, high, downToUpFlag);
          return;