class TrieNode:
    def __init__(self):
        self.children={}
        self.endOfString=False
        

class Trie: 
    def __init__(self):
        self.root=TrieNode()
        
    def insertString(self, word):
        current=self.root
        for i in word:
            ch=i 
            code=current.children.get(ch)
            if node==None:
                node=TrieNode()
                current.childrend.update({ch:node})
            current=node
        current.endOfString=True 
        print('successfully inserted')
    
    def searchString(self, word):
        currentNode=self.root
        for i in word:
            node = currentNode.children.get(i)
            if node==None:
                return False 
            currentNode=node
        
        if currentNode.endOfString==True:
            return True
        else:
            return False 
    
def delete(root, word, index):
    ch=word[index]
    currentNode= root.children.get(ch)
    canthisbedel=False
    if len(currentNode.children)>1:
        delete(currentNode, word, index+1)
        return False
    if index == len(word) -1:
        if len(currentNode)==False: 
            return False 
    else: 
        root.children.pop(ch)
        return True
    if currentNode.endOfString==True:
        delete(currentNode, word, index+1)
        return False 
    canthisbedel=delete(currentNode, word, index+1)
    if canthisbedel==True: 
        root.children.pop(ch)
        return True
    else: 
        return False


    

            