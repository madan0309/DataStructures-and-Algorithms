'''
Created on Mar 11, 2018

@author: kur4ve
'''
class Vertex:
    def __init__(self, id):
        self.id = id
        self.visited = False
    
    def setVertexID(self, id):
        self.id = id
        
    def getVertexID(self):
        return self.id
    
    def addNeighbor(self, neighbor, G):
        G.addEdge(self.id, neighbor)
        
    def getConnections(self, G):
        return G.adjMatrix[self.id]
    
    def setVisited(self):
        self.visited = True
    
    def __str__(self):
        return str(self.id)

class Graph:
    def __init__(self, numVertices, cost=0):
        self.adjMatrix = [[-1]*numVertices for _ in range(numVertices)]
        self.numVertices = numVertices
        self.vertices = []
        for i in range(numVertices):
            new_vertex = Vertex(i)
            self.vertices.append(new_vertex)
            
    def setVertex(self, vtx, id):
        if 0<=vtx< self.numVertices:
            self.vertices[vtx].setVertexID(id)
            
    def getVertex(self, id):
        for vertex in range(0, self.numVertices):
            if self.vertices[vertex].getVertexID()==id:
                return vertex
        return -1
    
    def addEdge(self, frm, to, cost=0):
        if self.getVertex(frm)!= -1 and self.getVertex(to)!=-1:
            self.adjMatrix[self.getVertex(frm)][self.getVertex(to)] = cost
    
    def getVertices(self):
        vertices = []
        for vertex in self.vertices:
            vertices.append(vertex.getVertexID())
        return vertices
    
    def printMatrix(self):
        for u in range(0, self.numVertices):
            row = []
            for v in range(0, self.numVertices):
                row.append(self.adjMatrix[u][v])
            print row
            
if __name__ == '__main__':
    G = Graph(4)
    G.setVertex(0, 'a')
    G.setVertex(1, 'b')
    G.setVertex(2, 'c')
    G.setVertex(3, 'd')
    
    G.addEdge('a', 'b', 10)
    G.addEdge('a', 'd', 10)
    G.addEdge('c', 'a', 20)
    G.addEdge('b', 'c', 10)
    G.addEdge('c', 'd', 10)
    print "Matrix"
    print G.printMatrix()
    print " Edges"
    