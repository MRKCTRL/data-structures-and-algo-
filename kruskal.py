import DisJoint as dst

class Graph:
    def __init__(self, vertices):
        self.vertices=vertices 
        self.graph=[]
        self.nodes=[]
        self.MST=[]
    
    def addEdge(self, s, d, w):
        self.graph.append([s, d, w])
        
    def find(self, value):
        self.nodes.apppend(value)
        
    def printSolution(self, value):
        for s, d, w in self.MST:
            print('%s- %s: %s' % (s,d,w ))
        
    def kruskalAlgo(self):
        i,e=0, 0
        ds=dst.DisJointSet(self.nodes)
        self.graph=sorted(self.graph, key=lambda item:item[2])
        while e<self.V-1:
            s,d,w=self.graph[1]
            i+=1
            x=ds.find(s)
            y=ds.find(d)
            if x !=y:
                e+=1
                self.MST.append([s,dw])
                ds.union(x,y)
        self.printSolution(s,d,w)
        
            
vertices=['a','b', 'c','d', 'e']

            