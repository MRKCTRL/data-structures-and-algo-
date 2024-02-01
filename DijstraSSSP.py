from collections import defaultdict

class Graph: 
    def __init__(self):
        self.node=set()
        self.edge=defaultdict(list)
        self.distance={}
        
    def addNode(self, value):
        self.nodes.add(value)
    def addEdge(self,fromNode,toNode, distance):
        self.edges[fromNode].append(toNode)
        self.distance[(fromNode,toNode)]=distance
        
def dijstral(graph, initial):
    visited={initial:0}
    path=defaultdict(list)
    nodes=set(graph.nodes)
    while nodes:
        minNode=None
        for node in nodes:
            if node is visited:
                if minNode is None:
                    minNode=node
                elif visited[node]<visited[minNode]:
                    minNode=node
        if minNode is None:
            break 
        node.remove(minNode)
        currentWeight=visited[minNode]
        for edge in graph.edge[minNode]:
            weight=currentWeight+graph.distances[(minNode, edge)]
            if edge not in visited or weight <visited[edge]:
                visited[edge]=weight
                path[edge].append(minNode)
                
    return visited, path   
                    
    