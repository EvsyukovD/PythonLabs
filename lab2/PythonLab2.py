from GraphClass import Graph as Gr
import pickle
import argparse
def EilerGraphCriteria(G):
    V = G.getVertexes();
    for i in V.keys():
        l = V.get(i)
        if len(l) % 2 == 1:
            return False;
    return True

def findEilerCycle(G):
    g = G.graphCpy()
    stack = list()
    res = list()   
    stack.append(list(g.V.keys())[0])

    while len(stack) != 0:
        v = stack[len(stack) - 1]
        if len(g.findVertex(v)) == 0:
           res.append(v)
           stack.pop()
        else:
           key = g.V.get(v)[0]
           g.removeEdge(v,key)
           stack.append(key)
    return res

def arrayHas(x,a):
    for i in range(len(a)):
        if x == a[i]:
            return True
    return False

def hamiltonCycle(G):
    V = list(G.V.keys())
    n = len(V)
    vis = {}
    for i in G.V.keys() :
        vis.update({i : False})
    visited = [False] * n
    path = []
    def hamilton(curr):
        path.append(curr)
        if len(path) == n:
            if arrayHas(path[-1],G.findVertex(path[0])):
                return True
            else:
                path.pop()
                return False
        vis.update({curr: True})
        for next in G.V.get(curr):
            if not vis.get(next):
                if hamilton(next):
                    return True
        vis.update({curr: False})
        path.pop()
        return False
    res = hamilton(V[0])
    if res:
        path.append(path[0])
        return path
    else:
        return None




def eilerCycle(G):
    if EilerGraphCriteria(G):
       return findEilerCycle(G)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Программа ищет эйлеровы/гамильтоновы циклы в графе.')
    parser.add_argument(dest = 'filename',type=str, help='Имя pickle-файла с графом')
    parser.add_argument(dest = 'mode',type=str, help='Какой цикл искать: ключ е - ищем эйлеров цикл, h - гамильтонов')
    args = parser.parse_args()
   
    with open(args.filename,'rb') as f:
        gr = Gr(pickle.load(f))
        print("Считанный граф:")
        print(gr.V)
    if args.mode == 'h':
       res = hamiltonCycle(gr)
       print("Гамильтоновский цикл :")
       if res != None:
          print(res)
       else:
          print("Нет цикла")
    else:
        res = eilerCycle(gr)
        print("Эйлеровский цикл :")
        if res != None:
           print(res)
        else:
           print("Нет цикла")
