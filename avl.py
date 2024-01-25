import queue
import QLL as Queue


class AVLNode:
    def __init__(self, data):
        self.data=data
        self.leftchild=None
        self.rightchild=None
        self.height=1
        
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
        customQueue=queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.dequeue()):
            root=customQueue.dequeue()
            print(root.value.data)
            if root.value.leftchild is not None:
                customQueue.enqueue(root.value.leftchild)
            if root.value.rightchild is not None:
                customQueue.enqueue(root.value.rightchild)
                
def searchNode(rootNode, nodeValue):
    if rootNode.data==nodeValue:
        print('the value is found')
    elif nodeValue<rootNode.data:
        if rootNode.leftchild.data==nodeValue:
            print('the value is found ')
        else:
            searchNode(rootNode.leftchild, nodeValue)
    else:
        if rootNode.rightchild.data==nodeValue:
            print('the value is found ')
        else:
            searchNode(rootNode.rightchild, nodeValue)
    
def getHead(rootNode):
    if not rootNode:
        return 0
    return rootNode.height

def rightRotate(disabledNode):
    newRoot=disabledNode.leftchild
    disabledNode.leftchild=disabledNode.leftchild.rightchild
    newRoot.right=disabledNode
    disabledNode.height = 1 + max(getHead(disabledNode.leftchild), getHead(disabledNode.rightchild))
    newRoot.height =1 + max(getHead(newRoot.leftchild), getHead(newRoot.rightchild))
    return newRoot

def leftRotate(disabledNode):
    newRoot=disabledNode.rightchild
    disabledNode.rightchild= disabledNode.rightchild.leftchild
    newRoot.leftchild=disabledNode
    disabledNode.height = 1 + max(getHead(disabledNode.leftchild), getHead(disabledNode.rightchild))
    newRoot.height =1 + max(getHead(newRoot.leftchild), getHead(newRoot.rightchild))
    return newRoot

def getBalance(rootNode):
    if not rootNode:
        return 0 
    return getHead(rootNode.leftchild) - getHead(rootNode.rightchild)

def insertNode(rootNode, nodeValue):
    if not rootNode:
        return AVLNode(nodeValue)
    elif nodeValue<rootNode.data:
        rootNode.leftchild=insertNode(rootNode.leftchild, nodeValue)
    else:
        rootNode.rightchild=insertNode(rootNode.rightchild, nodeValue)
    
    rootNode.height=1+ max(getHead(rootNode.leftchild), getHead(rootNode.right.rightchild))
    balance=getBalance(rootNode)
    if balance >1 and nodeValue<rootNode.leftchild.data:
        return rightRotate(rootNode)
    if balance>1 and nodeValue>rootNode.leftchild.data:
        rootNode.leftchild=leftchild=leftRotate(rootNode.leftchild)
        return rightRotate(rootNode)
    if balance<-1 and nodeValue>rootNode.rightchild.data:
        return leftRotate(rootNode)
    if balance<-1 and nodeValue<rooNode.rightchild.data:
        rootNode.rightchild=rightRotate(rootNode.rightchild)
        leftRotate(rootNode)
    return rootNode
def getMinValue(rootNOde):
    if rootNOde is NOne or rootNode.leftchild is None:
        return rootNode
    return getMinValue(rootNode.leftchild)

def delNode(rootNode, nodeValue):
    if not rootNode:
        return rootNode
    elif nodeValue <rootNode.data:
        rootNode.leftchild=delNode(rootNode.leftchild, nodeValue)
        
    elif nodeValue >rootNode.data:
        rootNode.rightchild=delNode(rootNode.rightchild, nodeValue)
    
    else:
        if rootNode.leftchild is None:
            temp=rootNode.rightchild
            rootNode=None
            return temp
        elif rootNode.rightchild is None:
            temp=rootNode.leftchildchild
            rootNode=None
            return temp
        temp=getMinValue(rootNode.rigthchild)
        rootNode.data=temp.data
        rootNode.rightchild=delNode(rootNode.rightchild, temp.data)
    balance=getBalance(rootNode)
    if balance>1 and getBalance(rootNode.leftchild) >=0:
        return rightRotate(rootNode)
    if balance<-1 and getBalance(rootNode.rightchild) <=0:
        return leftRotate(rootNode)
    if balance >1 and getBalance(rootNode.leftchild) <0:
        rootNode.leftchild=leftRotate(rootNode.leftchild)
        return rightRotate(rootNode)
    if balance <-1 and getBalance(rootNode.rightchild) >0:
        rootNode.rigthchild=rightRotate(rootNode.rightchild)
        return leftRotate(rootNode)
    return rootNode

def delEntNode(rootNode):
    rootNode.data=None 
    rootNode.leftchild=None
    rootNode.rightchild=None
    return 'the avl has been successfully deleted'
        
        
    
    
newAVL=AVLNode(10)