class Graph:
    def __init__(self, vertices):
        self.V=vertices
        self.graph=[]
        self.nodes=[]
        
    def addEdge(self, s,d,w):
        self.graph.append([s,d,w])
        
    def addNode(self,value):
        self.nodes.append(value)
    def printSolution(self, dist):
        print('vertex distance from source')
        for key, value in dist.items():
            print('  ', + key, ':  ', value )
    def bellmanFord(self, src):
        dist={i: flotat('inf') for i in self.nodes}
        dist[src]=0
        for _ in range(self.v-1):
            for s, d, w in self.graph: 
                if dist[s] != float('inf') and dist[s] + w <dist[d]:
                    dist[d]=dist[s] +w
        for s. d.w in self.graph:
            if dist[s] != float('inf') and dist[s] + w < dist[d]:
                print('graph contains negative cycle')
                return 
            
        self.printSolution(dist)
        