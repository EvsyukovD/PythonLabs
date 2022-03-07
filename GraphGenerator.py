import random 
from GraphClass import Graph as Gr
import pickle
def generateGraph(n) :
    gr = Gr()
    for i in range(n) :
        gr.addVertex(i)
        if i > 0 :
           gr.addEdge(0,i)
    for i in range(1,n) :
        for j in range(i,n) :
            if i != j and random.randint(0,1) == 1 :
                gr.addEdge(i,j)
    return gr.getVertexes()

if __name__ == "__main__" :
   print("Введите число вершин:")
   n = int(input())
   gr = generateGraph(n)
   with open('Graph_' + str(n) + '.pickle','wb') as f :
       pickle.dump(gr,f)
