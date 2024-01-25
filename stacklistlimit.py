class Stack:
    def __init__(self, maxSize):
        self.maxSize=maxSize
        self.list=[]
        
    #  isEmpty   # 
    def __str__(self):
        if self.list==[]:
            return True
        else:
            return False 
        
    # is full 
    def isfull(self):
        if len(self.list)==self.maxSize:
            return True
        else:
            return False 
         
    def push(self, value):
        if self.isfull():
            return 'stack is full'
        else:
            self.list.append(value)
            return 'the element has been successfully inserted'
        
    def pop(self):
        if self.isEmpty():
            return 'there is not any element in the stack'
        else:
            return self.list()        
        
    def dele(self):
        self.list=None