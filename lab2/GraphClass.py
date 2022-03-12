class Graph(object):
    V = dict()
    def getVertexes(self):
        return self.V

    def findVertex(self,key):
        return self.V.get(key)   
    def __init__(self,V=None):
        if V != None :
           self.V = V.copy()
        return

    def addVertex(self,key):
        self.V.update({ key : list()})

    def removeVertex(self,key):
        v = selffindVertex(key)
        if v != None:
           self.V.remove(v)
           return True
        else:
           return False
    
    def addEdge(self,key1,key2):
        v1 = self.findVertex(key1)
        v2 = self.findVertex(key2)
        if v1 != None and v2 != None:
           v1.append(key2)
           v2.append(key1)
           self.V.update({key1: v1})
           self.V.update({key2: v2})
           return True
        else:
           return False
    def removeEdge(self,key1,key2):
        v1 = self.findVertex(key1)
        v2 = self.findVertex(key2)
        if v1 != None and v2 != None:
            v1.remove(key2)
            v2.remove(key1)
            self.V.update({key1: v1})
            self.V.update({key2: v2})
            return True
        else:
            return False
    def graphCpy(self):
        g = Graph()
        g.V = self.V.copy()
        return g
 