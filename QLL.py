class Node:
    def __init__(self, value=None):
        self.value=value
        self.next=None
    def __str__(self):
        return str(self.value)
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def __iter__(self):
        curNode=self.head
        while curNode:
            yield curNode
            curNode=curNode.next
class Queue:
    def __init__(self):
        self.LinkedList=LinkedList()         
        
    def __str__(self):
        values=[str(x) for x in self.LinkedList]
        return ''.join(values)
    
    def enqueue(self, value):
        newNode=Node(value)
        if self.linkedList.head==None:
            self.LinkedList.head=newNode
            self.LinkedList.tail=newNode
        else:
            self.LinkedList.tail.next=newNode
            self.LinkedList=newNode
            
    def isEmpty(self):
        if self.LinkedList.head==None:
            return True
        else:
            return False
    def dequeue(self):
        if self.isEmpty():
            return 'thereis not any nodein the Queue'
        else:
            tempNode=self.LinkedList.head
            if self.LinkedList.head==self.LinkedList.tail:
                self.LinkedList.head=None
                self.LinkedList.tail=None
            else:
                self.LinkedList.head=self.LinkedList.head.next
            return tempNode
    def peek(self):
        if self.isEmpty():
            return 'thereis not any nodein the Queue'
        else:
            return self.linkedList.head
    def delete(self):
        self.LinkedList.head=None
        self.LinkedList=None

        
            
