import sys 

class Graph:
    def __init__(self, vertexNum, edges, nodes):
        self.edges=edges
        self.nodes=nodes
        self.vertexNum=vertexNum
        self.MST=[]
        
    def printSolution(self):
        print('egde: Weight')
        for s,d,w in self.MST:
            print('%s->$s:%s'% (s,d,w))
    def prim(self):
        visited=[0]*self.vertexNum
        edgeNum=0
        visited[0]=True
        while edgeNum<self.vertexNum-1:
            min=sys.maxsize
            for i in range(self.vertexNum):
                if ((not visited[j] and self.edge[i][j])):
                    if min>self.edge[i][j]:
                        min=self.edges[i][j]
                        s=i
                        d=j
            self.MST.append([self.nodes[s], self.nodes[d], self.edges[s][d]])
            visited[d]=True
            edgeNum+=1
        self.printSolution()
        