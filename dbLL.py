class Node:
    def __init__(self, value=None):
        self.value=value
        self.next=None
        self.prev=None
class DdLL:
    def __init__(self):
        self.head=None
        self.tail=None
        
    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next 
    def createDLL(self, nodeValue):
        node=Node(nodeValue)
        node.prev=None
        node.next=None
        self.head=node
        self.tail=node 
        return "the Dll is created successfully"
    
    def insertNode(self, nodeValue, location):
        if self.head is None:
            print('node cannot be inserted')
        else:
            newNode=Node(nodeValue)
            if location==0:
                newNode.prev=None
                newNode.next=self.head
                self.head.prev=newNode
                self.head=newNode
            elif location==1:
                newNode.next=None
                newNode.prev=self.tail
                self.tail.next=newNode
                self.tail=newNode
            else:
                tempNode=self.head
                index=0
                while index<location-1:
                    tempNode=tempNode.next
                    index+=1
                newNode.next=tempNode.next
                newNode.prev=tempNode
                newNode.next.prev=newNode
                tempNode.next=newNode
    def traversalDLL(self):
        if self.head is None:
            print('there is no element to traverse')
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode=tempNode.next
    
    
    def revTravDLL(self):
        if self.head is None:
            print('there is not any element to traverse')
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                tempNode=tempNode.prev
                
    def searchDDL(self, nodeValue):
        if self.head is None:
            return 'there is not any element'
        else:
            tempNode=self.head
            while tempNode:
                if tempNode.value==nodeValue:
                    return tempNode.next 
                tempNode=tempNode.next
            return 'the node does not exist in this list'
    def deleteNode(self, location):
        if self.head is None:
            print('there is not any element')
        else:
            if location==0:
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                else:
                    self.head=self.head.next
                    self.head.prev=None
            elif location==1:
                 if self.head==self.tail:
                    self.head=None
                    self.tail=None
                 else:
                    self.tail=self.tail.prev
                    self.tail.next=None
            else:
                curnNode=self.head 
                index=0
                while index<location-1:
                    curNode=curnNode.next
                    index+=1
                curnNode=curNode.next
                curnNode.next.prev=curNode
            print('the node has been successfully  deleted ')
    def deleteDLL(self):
        if self.head is None:
            print('there is not any node in dll')
        else:
            tempode=self.head
            while tempNode:
                tempNode.prev=None
                tempNode=tempNode.next 
            self.head=None
            self.tail=None
            print('the dll has been successfully deleted')            
            
        
doubleLL=DdLL()
doubleLL.createDLL(6)