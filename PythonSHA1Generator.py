import hashlib;

def rand(seed) :
    while(seed > 0) :
        yield seed;
        seed = (seed ** 2 + 1) % 50;

def createHashList(n,seed) :
    c = rand(seed);
    hashList = list();
    for i in range(n) :
        hash = hashlib.sha1(str(c.__next__()).encode());
        hashList.append(hash.hexdigest());
    return hashList;

def listToFile(name,list) :
    f = open(name + '.txt','wt');
    for i in list :
        f.write(i);
    f.close();
    return;

def main() :
    seed = 50;
    '''
    print("Введите имя файла:");
    name = input();
    print("Введите количество хешей:");
    n = input();
    '''
    for i in range(0,1) :        
        listToFile('Hash' + str(i),createHashList(1000 + i * 100,seed));
    return;

if __name__ == "__main__" :
   main();