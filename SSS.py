class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict={}
        self.gdict=gdict
    def bfs(self,start, end):
        queue=[]
        queue.append([start])
        while queue:
            path=queue.pop(0)
            node=path[-1]
            if node==end:
                return path 
            for adjacent in self.gdict.get(node, []):
                newPath=list(path)
                newPath.append(adjacent)
                queue.append(newPath)
                
customDict={
    'a':['a','f'],
    'a':['a','f'],
    'a':['a','f'],
    'a':['a','f'],
    'a':['a','f'],
    'a':['a','f'],
    'a':['a','f'],
    
}