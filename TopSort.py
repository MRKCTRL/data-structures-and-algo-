from collections import defaultdict 

class Graph:
    def __init__(self, numOfVert):
        self.graph=defaultdict(list)
        self.numbOfVert=numOfVert
    def edge(self, vertex, edge):
        self.graph[vertex].append(egde)
        
    
    def topSortUtil(self, v, visited, stack):
        visited.append(v)
        for i in self.graph[v]:
            if i not in visited:
                self.topSortUtil(i,visited, stack)
                
        stack.insert(0,v)
    
    def topSort(self):
        visited=[]
        stack=[]
        for k in list(self.graph):
            if k not in visited: 
                self.topSortUtil(k, visited, stack)
        print(stack)
                