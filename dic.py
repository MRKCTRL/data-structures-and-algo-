earth=dict()


planet={}

engToZulu={'hello':'sawubona',
           'how are you': 'unjani',
           'love': 'standwa'}

engToZulu['hello']

# update/ add an element to the dictionary 
mydict={'name': 'jame', 
        'age': 25,
        'address': 'africa'}

mydict['age']=26
# time complexity:O(1)
# space complexity:O(1)


def travisD(dict):
    for key in dict: #---------------->O(n)
        print(key, dict[key]) #---------------->O(1)
        # time complexity:O(n)
# space complexity:O(1) 
        
travisD(mydict)


# searching an element
def searchD(dict,value):
    for key in dict:  #---------------->O(n)
        if dict[key]==value:  #---------------->O(1)
            return key, value  #---------------->O(1)
    return'the value does not exist'  #---------------->O(1)
    # time complexity:O(n)
# space complexity:O(1) 
print(searchD(mydict,26))    

# del/remove
mydict.pop('name')

mydict.popitem()

mydict.clear()

del mydict['age', 'address']

# dict methods

mydict.clear()

mydict.copy()

newdict={}.fromkeys([1,2,3], 0)

mydict.get('name', 'jamie')

dict.items()

dict.keys() #get all keys 

mydict.popitem()

mydict.setdefault('age', 'added')

mydict.pop('age', 86)

mydict.values() #list of all values 

update={'eh':1,
        'uhm':2,
        'pro':1}
mydict.update(update)
# mydict.update('education': 'self-taught')

'one' in mydict

'one' in mydict.values() #------------>O(1)/time complexity

for key in mydict:
    print(key, mydict[key])  #------------>O(n)
    
    
    # for password and userlogin
all(mydict)

any(mydict) #any method is true


len(mydict) #number of items

sorted(mydict, reverse=True)