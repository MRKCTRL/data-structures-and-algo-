class Heap:
    def __init__(self, size):
        self.customList=(size+1) * [None]
        self.heapsize=0
        self.maxSize=size+1 
        
def peekOfHeap(rootNode):
    if not rootNode:
        return 
    else:
        return rootNode.customList[1]
    
def sizeOfHeap(rootNode):
    if not rootNode:
        return 
    else:
        return rootNode.heapsize
    
def traversalOfBH(rootNode):
    if not rootNode:
        return 
    else:
        for i in range(1, rootNode.heapsize+1):
            print(rootNode.customList[i])

def heapifyTreeinsert(rootNode, index, heapType):
    parentIndex=int(index/2)
    if index <=1:
        return 
    if heapType=='Min':
        if rootNode.customList[index]<rootNode.customList[parentIndex]:
            temp=rootNode.customList[index]
            rootNode.customList[index]=rootNode.customList[parentIndex]
            rootNode.customList[parentIndex]=temp
        heapifyTreeinsert(rootNode,parentIndex, heapType)
    elif heapType=='Max':
        if rootNode.customList[index]>rootNode.customList[parentIndex]:
            temp=rootNode.customList[index]
            rootNode.customList[index]=rootNode.customList[parentIndex]
            rootNode.customList[parentIndex]=temp
        heapifyTreeinsert(rootNode, parentIndex, heapType)


def insertNode(rootNode,nodeValue, heapType ):
    if rootNode.heapsize+1==rootNode.maxsize:
        return 'the binary heap is full'
    rootNode.customList[rootNode.heapSize +1]=nodeValue
    rootNode.heapSize+=1
    heapifyTreeinsert(rootNode, rootNode.heapSize, heapType)
    return 'the value has been successfly inserted'
        
 
def heapifyTreeExtract(rootNode, index, heapType):
    leftIndex=index*2
    rightidex=index*2+1
    swapchild=0
    
    if rootNode.heapSize<leftIndex:
        return 
    elif rootNode.heapSize==leftIndex:
        if heapType=='Min':
            if rootNode.customList[index]>rootNode.customList[leftIndex]:
                temp=rootNode.customList[index]
                rootNode.customList[index]=rootNode.customList[leftIndex]
                rootNode.customList[leftIndex]=temp 
            return 
        else:
            if rootNode.customList[index]<rootNode.customList[leftIndex]:
                temp=rootNode.customList[index]
                rootNode.customList[index]=rootNode.customList[leftIndex]
                rootNode.customList[leftIndex]=temp 
            return 

    else:
        if heapType=='Min':
            if rootNode.customList[leftIndex]<rootNode.customList[rightidex]:
                swapchild=leftIndex
            else:
                swapchild=rightidex
            if rootNode.customList[index]> rootNode.customList[swapchild]:
                temp=rootNode.customList[index]
                rootNode.customList[index]=rootNode.customList[swapchild]
                rootNode.customList[swapchild]=temp 
        else:
            if rootNode.customList[leftIndex]>rootNode.customList[rightidex]:
                swapchild=leftIndex
            else:
                swapchild=rightidex
            if rootNode.customList[index]> rootNode.customList[swapchild]:
                temp=rootNode.customList[index]
                rootNode.customList[index]=rootNode.customList[swapchild]
                rootNode.customList[swapchild]=temp  
        heapifyTreeExtract(rootNode, swapchild, heapType)
def extractNode(rootNode, heapType):
    if rootNode.heapsize==0:
        return 
    else:
        extractNode=rootNode.customList[1]
        rootNode.customList[1]=rootNode.customList[rootNode.heapSize]
        rootNode.customList[rootNode.heapSize]=None
        rootNode.heapSize-=1
        heapifyTreeExtract(rootNode,1, heapType)
        return extractNode
    
def delEntBH(rootNode):
    rootNode.customList=Nonestring      
            

newBH=Heap(6)
insertNode(newBH, 4, 'max')
