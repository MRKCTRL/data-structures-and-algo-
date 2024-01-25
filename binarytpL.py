class BinaryTree:
    def __init__(self, size):
        self.customList=size*[None]
        self.lastUsedIndex=0
        self.maxSize=size
        
        
    def insertNode(self, value):
        if self.lastUsedIndex+1==self.maxSize:
            return 'the binary tree is full'
        self.customList[self.lastUsedIndex+1]=value
        self.lastUsedIndex+=1
        return 'the value has been successfully inserted'
    
    def searchNode(self, nodeValue):
        for i in range(len(self.customList)):
            if self.customList[i]==nodeValue:
                return 'success'
            return 'not found'
    
    def preOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return 
        print(self.customList[index])
        self.preOrderTraversal(index*2)
        self.preOrderTraversal(index*2+1)
    
    
    def inOrderTravesal(self, index):
        if index > self.lastUsedIndex:
            return
        self.inOrderTravesal(index*2)
        print(self.customList[index])
        self.inOrderTravesal(index*2+1)
        
    def postOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return 
        self.postOrderTraversal(index*2)
        self.postOrderTraversal(index*2+1)
        print(self.customList[index])
    
    def levelOrderTraversal(self, index):
        for i in range(index, self.lastUsedIndex+1):
            print(self.customList[i])
            
    def delnode(self, value):
        if self.lastusedindex==0:
            return 'there is not any node'
        for i in range(1, self.lastUsedIndex+1):
            if self.customList[i]==value:
                self.customList[i]=self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex]=None
                self.lastUsedIndex-=1
                return 'the node has been successfullly deleted'
            
    def delBT(self):
        self.customList=None
        return 'the bt has been successfully deleted'
            
    

newBT=BinaryTree(8)
newBT.insertNode('drinks')
newBT.insertNode('hot')

newBT.insertNod('cold')