class BSTNode:
    def __init__(self, data):
        self.data=data
        self.leftchild=None
        self.rightchild=None
        
def insertNode(rootNode, nodeValue):
    if rootNode.data==None:
        rootNode.data=nodeValue
    elif nodeValue<=rootNode.data:
        if rootNode.leftchild is None:
            rootNode.leftchild=BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftchild, nodeValue)
    else:
        if rootNode.rightchild is None:
            rootNode.rightchild=BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightchild, nodeValue)
    return ' the node has been successfully inserted'

def preOrderTravesal(rootNode):
    if not rootNode:
        return 
    print(rootNode.data)
    preOrderTravesal(rootNode.leftchild)
    preOrderTravesal(rootNode.rightchild)
    
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

def levelOrderTraversal(rootNode):
     if not rootNode:
        return
    else:
        customQueue= queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root=customQueue.dequeue()
            print(root.value.data)
            if root.value.leftchild is not None:
                customQueue.enqueue(root.value.leftchild)
                
            if root.value.leftchild is not None:
                customQueue.enqueue(root.value.right child)

        
def searchNode(rootNode,nodeValue):
    if rootNode.data==nodeValue:
        print('the value is found')
    elif nodeValue<rootNode.data:
        if rootNode.leftchild.data==nodeValue:
            print('the value is found')
        else:
            searchNode(rootNode.leftchild, nodeValue)
    else:
        if rootNode.rightchild.data==nodeValue:
            print('the value is found')
        else:
            searchNode(rootNode.rightchild, nodeValue)
            
def minValueNode(bstNode):
    current=bstNode
    while (current.leftchild is not None):
        current=current.leftchild
    return current 

def delNode(rooNode, nodeValue):
    if rootNode is None:
        return rootNode
    if nodeValue<rootNode.data:
        rootNode.leftchild=delNode(rootNode.leftchild, nodeValue)
    elif nodeValue>rootNode.data:
        rootNode.leftchild=delNode(rootNode.leftchild, nodeValue)
    else: 
        if rootNode.leftchild is None:
            temp=rootNode.rightchild 
            rootNode=None
            return temp 
        
        if rootNode.rightchild is None:
            temp=rootNode.leftchild 
            rootNode=None
            return temp 
        
        temp=minValueNode(rootNode.rightchild)
        rootNode.data=temp.data
        rootNode.rightchild=delNode(rootNode.rightchild, temp.data)
    return rootNode
        
def delBst(rootNode):
    rootNode.data=None
    rootNode.leftchild=None
    rootNode.rightcjo;d=None 
    return 'the bst has been successfully delete'
    
newBST=BSTNode(None)