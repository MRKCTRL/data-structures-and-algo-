import QLL as queue

class TreeNode:
    def __init__(self, data):
        self.data=data
        self.leftchild=None
        self.rightChild=None
    

    def preOrderTraversal(rootNode):
        if not rootNode:
            return 
        print(rootNode.data)
        preOrderTraversal(rootNode.leftchild)
        preOrderTraversal(rootNode.rightchild)
        
    preOrderTraversal(newBT)

    def inOrderTraversal(rootNode):
        if not rootNode:
            return 
        inOrderTraversal(rootNode.leftchild)
        print(rootNode.data)
        inOrderTraversal(rootNode.rightchild)

    def postOrderTraversal(rootNode):
        if not rootNode:
            return 
        postOrderTraversal(rootNode.leftchild)
        postOrderTraversal(rootNode.rightchild) 

    postOrderTraversal(newBT)

    def levelOrderTraversal(rootNode):
        if not rootNode:
            return
        else:
            customQueue=queue.Queue()
            customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root=customQueue.dequeue()
            print(root.value.data)
            if (root.value.leftchild is not None):
                customQueue.enqueue(root.value.leftchild)
                
            if (root.value.rightchild is not None):
                customQueue.enqueue(root.value.rightchild)
                
    def searchBT(rootNode,nodeValue):
        if not rootNode:
            return 'the bt does not exist'
        else:
            customQueue=queue.Queue()
            customQueue.enqueue(rootNode)
            while not(customQueue.isEmpty()):
                root=customQueue.dequeue()
                if root.value.data==nodeValue:
                    return 'success'
                if (root.value.leftchild is not None):
                    customQueue.enqueue(root.value.leftchild)
                
                if (root.value.rightchild is not None):
                    customQueue.enqueue(root.value.rightchild)
            return 'not found'
        
    
    def insertNodeBT(rootNode, newNode):
        if not rootNode:
            rootNode=newNode
        else:
            customQueue=queue.Queue()
            customQueue.dequeue(rootNode)
            while not(customQueue.isEmpty()):
                root=customQueue.dequeue()
                if root.value.leftchild is not None:
                    customQueue.enqueue()
                else:
                    root.value.leftchild=newNode
                    return 'successfull inserted'
                if root.value.rightchild is not None:
                    customQueue.enqueue()
                else:
                    root.value.rightchild=newNode
                    return 'successfull inserted'
def getDeepNode(rootNode):
    if not rootNode:
        return
    else:
        customQueue=queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root=customQueue.dequeue()
            if (root.value.leftchild is not None):
                    customQueue.enqueue(root.value.leftchild)
                    
            if (root.value.rightchild is not None):
                    customQueue.enqueue(root.value.rightchild)
        deepNode=root.value
        return deepNode
def delDeepNode(rootNode, dNode):
    if not rootNode:
        return 
    else:
        customQueue=queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root=customQueue.dequeue()
            if root.value is dNode:
                root.value=None
                return 
            if root.value.rightchild:
                if root.value.rightchild is dNode:
                    root.value.rightchild=None
                    return
                else:
                    customQueue.enqueue(root.value.rigthchild)
            if root.value.leftchild:
                if root.value.leftchild is dNode:
                    root.value.leftchild=None
                    return
                else:
                    customQueue.enqueue(root.value.leftchild)
        
                
# newBT=TreeNode('drinks')
# leftchild=TreeNode('hot')
# rightchild=TreeNode('cold')
# newBT.leftchild=leftchild
# newBT.rightChild=rightchild
                

# newNode=getDeepNode()
# delDeepNode(newBT,newNode)
# levelOrderTraversal(newBT)
def delNodeBt(rootNode,node):
    if not rootNode:
        return 'the bt does not exist'
    else:
        customQueue=queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            if root.value.data == node:
                dNode=getDeepNode(rootNode)
                root.value.data=dNode.data
                delDeepNode(rootNode, dNode)
                return 'the nodehas been successfuly deleted'
            if (root.value.leftchild is not None):
                customQueue.enqueue(root.value.leftchild)
                
            if (root.value.rightchild is not None):
                customQueue.enqueue(root.value.rightchild)
        return 'failed delete'
    
    def deleteBT(tooNode):
        rootNode.data=None
        rootNode.leftchild=None
        rootNode.rightchild=None
        return 'the BT has been successfully deleted'
    
    
    
    
    
    # delNodeBt(newBT,'Tea')
    # levelOrderTraversal(newBT)
    
    # def preOrderTraversal(self, index):
    #     if index > self.lastUsedIndex:
    #         return
        
    #     print(self.customList[index])
    #     self.preOrderTraversal(index*2)
    #     self.preOrderTraversal(index*2+1)