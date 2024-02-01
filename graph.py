class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict={}
        self.gdict=gdict
    
    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)
        
    def bfs(self, vertex):
        visited=[vertex]
        queue=[vertex]
        while queue:
            deVertex=queue.pop(0)
            print(deVertex)
            for adjacentVertex in self.gdict[deVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    queue.append(adjacentVertex)
                    
    def dfc(self, vertex):
        visited=[vertex]
        stack=[vertex]
        while stack:
            popVertex=stack.pop()
            print(popVertex)
            for adjacentVertex in self.gdict[popVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    stack.append(adjacentVertex)
        
                    
        
customDict={'d':['f', 'd', 'd', 'g'],
            'd':['f', 'd', 'd', 'g'],
            'd':['f', 'd', 'd', 'g'],
            'd':['f', 'd', 'd', 'g'],
            'd':['f', 'd', 'd', 'g']
            }
                   
