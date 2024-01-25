class Node:
    def __init__(self, value=None):
        self.value=value
        self.next=None


class SLinkedList:
    def __init__(self):
        self.head=None
        self.head=None
    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next
            
    def inertSLL(self, value, location):
        newNode=Node(value)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
        else:
            if location==0:
                newNode.next=self.head
                self.head=newNode
            elif location==1:
                newNode.next=Node
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
    
    def travSLL(self):
        if self.head is None:
            print("the singly linked does not exist")
        else:
            node=self.head
            while node is not None:
                print(node.value)
                node=node.next
    def searchSLL(self, nodeValue):
        if self.head is None:
            return "the list does not exist"
        else:
            node=self.head 
            while node is not None:
                if node.value==nodeValue:
                    return node.value        
            node=node.next
            return 'THE VALUE DOES NOT EXIST IN THE LIST' 
    
    def delNode(self, location):
        if self.head is None:
            print('the sll does not exist')
        else:
            if location==0:
                if self.head==self.tail:
                    self.head=None 
                    self.head=None 
                else:
                    self.head=self.head.next 
            elif location==11: 
                if self.head==self.tail:
                    self.head=None 
                    self.head=None
                else:
                    node=self.head 
                    while node is not None:
                        if node.next==self.tail:
                            break 
                        node=node.next 
                    node.next=None 
                    self.tail=node
            else:
                tempNode=self.head
                index=0
                while index<location-1:
                    tempNode=tempNode.next
                    index+=1
                nextNode=tempNode.next
                tempNode.next=nextNode.next
                
        def deleteEntireSSL(self):
            if self.head is None:
                print('the sll does not exist')
            else:
                self.head=None 
                self.tail=None
            # print()
        
        

# circularSSL=create
    