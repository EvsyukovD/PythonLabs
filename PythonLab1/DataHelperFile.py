class DataHelper(object):
      hashSize = 20;#bytes
      keySize = 8;#bytes
      
      @staticmethod
      def readFile(filename) :
          f = open(filename,'rt');
          data = list();
          while(True) :
              line = f.read(DataHelper.hashSize * 2);
              if not line :
                  break;
              data.append(line);
          f.close();
          return data;
      
      @staticmethod
      def getKey(hashLine) :
          return int("0x" + str(hashLine)[0:(2 * DataHelper.keySize)],16);
      
      @staticmethod
      def rewriteFile(name,list) :
          f = open(name,'wt');
          for l in list :
              f.write(str(l));
          f.close();
          return;





