class Node:
    def __init__(self, value=None):
        self.value=value
        self.next=None


class circularsinglylinkedlist:
    def __init__(self):
        self.head=None
        self.head=None
    def __iter__(self):
        node=self.head
        while node:
            yield node
            # if node.next==self.head:
            if node.next==self.next:
                break
            
    def createCSSL(self, nodeValue):
            node=Node(nodeValue) #------------------->O(1)
            node.next=node #------------------->O(1)
            self.head=node #------------------->O(1)
            self.tail=node  #------------------->O(1)
            return "the cssll has been created"#------------------->O(1)
        
        
    def insertCSSLL(self, value, location):
        if self.head is None:
            return "the head is reference is none"
        else:
            newNode=Node(value)
            if location==0:
                newNode.next=self.head
                self.head=newNode
                self.tail.next=newNode
            elif location==1:
                newNode=self.tail.next
                self.tail.next=newNode
                self.tail=newNode
            else:
                tempNode=self.head
                index=0
                while index<location-1:
                    tempNode=tempNode.next
                    index+=1
                nextnode=tempNode.next
                tempNode.next=newNode
                newNode=nextnode
            return "thr node has been successfully inserted"
        
    def travsCSLL(self):
        if self.head is None:
            print("there is not any element for traversal")
        else:
            tempNode=self.head
            while tempNode:
                print('tempnode.value')
                tempNode=tempNode.next
                if tempNode==self.tail.next:
                    break
    def searchCSLL(self, nodeValue):
        if self.head is None:
            return "there is not any node in this CSLL"
        else:
            tempNode=self.head
            while tempNode:
                if tempNode.value==nodeValue:
                    return tempNode.value
                tempNode=tempNode.next
                if tempNode==self.tail.next:
                    return "the node does not exist in this CSLL"
    def deleteNode(self, location):
        if self.head is None:
            print('there is not any node in CSLL')
        else:
            if location==0:
                if self.head==self.tail:
                    self.head.next=None
                    self.head=None
                    self.tail=None
                else:
                    self.head=self.head.next
                    self.tail.next=self.head
            elif location==1:
                if self.head==self.tail:
                    self.head.next=None
                    self.head=None
                    self.tail=None
                else:
                    node=self.head
                    while node is  not None:
                        if node.next==self.tail:
                            break
                        node=node.next
                    node.next=self.head
                    self.tail=node
            else:
                tempNode=self.head
                index=0
                while index<location-1:
                    tempNode=tempNode.next
                    index+=1
                nextNode=tempNode.next
                tempNode.next=nextNode.next
    def delEntCSSL(self):
        self.head=None
        self.tail.next=None
        self.tail=None
                
        
circularSSL=circularsinglylinkedlist()
circularSSL.createCSSL(1)
circularSSL.insertCSSLL(0,0)
circularSSL.insertCSSLL(2,1)
circularSSL.insertCSSLL(3,1)
circularSSL.insertCSSLL(4,1)
print([node.value for node in circularSSL])


circularSSL.deleteNode(0)